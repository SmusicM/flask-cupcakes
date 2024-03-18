"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Cupcake model"""
    __tablename__ = "cupcake"

    id = db.Column(db.Integer,primary_key=True,autoincrement = True)

    flavor = db.Column(db.Text,nullable=False,unique=False)

    size = db.Column(db.Text,nullable = False,unique=False)

    rating = db.Column(db.Float,nullable = False,unique=False)

    image = db.Column(db.Text,
                          nullable = True,
                          unique = False,
                          default = "https://tinyurl.com/demo-cupcake")

    def serialize(self):
            """serialize cupcake data for json"""
            return {
                'id': self.id,
                'flavor': self.flavor,
                'size': self.size,
                'rating': self.rating,
                "image": self.image
            }

    def __repr__(self):
        return f"<Cupcake {self.id} flavor={self.flavor} size={self.size} rating={self.rating} image={self.image}>"
