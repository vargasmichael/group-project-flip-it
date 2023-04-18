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
class Player(db.Model,SerializerMixin):
    __tablename__ = 'players'
    serialize_rules = ()
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)
    total_wins = db.Column(db.Integer)
    total_games = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
class Game(db.Model,SerializerMixin):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    tile_id = db.Column(db.Integer, db.ForeignKey('tiles.id'))

class Tile(db.Model,SerializerMixin):
    __tablename__ = 'tiles'
    serialize_rules = ()
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Url)


class hall_of_fame(db.Model,SerializerMixin):
    __tablename__ = 'hall_of_fames'
    serialize_rules = ()
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))


   
