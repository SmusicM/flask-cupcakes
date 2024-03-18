"""Flask app for Cupcakes"""
from flask import Flask, request, render_template,  redirect, flash, session,jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db,Cupcake
from forms import CupcakeForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
#app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
from models import db

connect_db(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home_page():
    #cupcake = Cupcake.query.all()
    form = CupcakeForm()
    return render_template("cupcake_home.html",form=form)

@app.route('/api/cupcakes')
def show_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def show_single_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())
    
@app.route('/api/cupcakes',methods=["POST"])
def create_cupcake():
    
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']
    new_cupcake = Cupcake(flavor=flavor,size=size,rating=rating,image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return(response_json,201)

@app.route('/api/cupcakes/<int:id>',methods=['PATCH'])
def edit_cupcake(id):
    """updates cupcake at certain id"""
    cupcake = Cupcake.query.get_or_404(id)
    #we do these request.json.get(key or key ,value of field) so if not filed out
    #...reverts to the previous value
    cupcake.flavor = request.json.get("flavor",cupcake.flavor)
    cupcake.size = request.json.get("size",cupcake.size)
    cupcake.rating = request.json.get("rating",cupcake.rating)
    cupcake.image = request.json.get("image",cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>',methods=['DELETE'])
def delete_cupcake(id):
    """deletes a cupcake at id route"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="cupcake deleted")