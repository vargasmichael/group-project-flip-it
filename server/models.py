# flask db init
#flask db revision --autogenerate -m'message'
# flask db upgrade
# python db/seed.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# from sqlalchemy.orm import validates
# from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy()



# More boilerplate! We need to import THE SAME bcrypt we created in app
# from sqlalchemy.ext.hybrid import hybrid_property
# from services import bcrypt,db
#

class In_Play(db.Model,SerializerMixin):
    __tablename__ = 'in_plays'
    serialize_rules = ()
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))
    
    game = db.relationship('Game', backref='in_plays')
    

class Game(db.Model,SerializerMixin):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer)

class PGT(db.Model,SerializerMixin):
    __tablename__ = 'pgts'
    serialize_rules = ()
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))

class Player(db.Model,SerializerMixin):
    __tablename__ = 'players'
    serialize_rules = ()
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)
    # we need to create a _password_hash = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

   
class Card(db.Model,SerializerMixin):
    __tablename__ = 'cards'
    serialize_rules = ()
    id = db.Column(db.Integer, primary_key=True)
    values = db.Column(db.Integer)
    suits = db.Column(db.String)
    status = db.Column(db.Integer)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))