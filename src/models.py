from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Planet {self.planet_name}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class FavoritePlanet(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=False, primary_key=True)
    insertion_date = db.Column(db.Date, default=datetime.datetime.now())
  
    planet = db.relationship('Planet', backref="favorite_planets")
    user = db.relationship('User', backref="favorite_planets")

    def __repr__(self):
        return f'<Planet {self.user.email} likes {self.planet.planet_name} on date {self.insertion_date}>'