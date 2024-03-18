from flask_wtf import FlaskForm
from wtforms import StringField, FloatField,BooleanField,IntegerField,RadioField,SelectField
from wtforms.validators import InputRequired, Optional, Email,NumberRange,URL

class CupcakeForm(FlaskForm):
    flavor = StringField("Flavor Cupcake",validators=[InputRequired(message="Flavor Name is required")])
    size = StringField("Cupcake Size",validators=[InputRequired(message="size is required")])
    rating = FloatField("Rating",validators=[InputRequired(),NumberRange(min=0.0,max=10.0)])
    image = StringField("Image",validators=[Optional(),URL(message="must be url")],default = "https://tinyurl.com/demo-cupcake")
#CAN MAKE SIZE A SELECT WITH 3 OPTIONS SMALL MEDIUM LARGE