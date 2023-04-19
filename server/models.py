# flask db init
# flask db revision --autogenerate -m'message'
# flask db upgrade
# python db/seed.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import Bcrypt

from config import db, bcrypt

# metadata = MetaData(naming_convention={
#     "ix": "ix_%(column_0_label)s",
#     "uq": "uq_%(table_name)s_%(column_0_name)s",
#     "ck": "ck_%(table_name)s_`%(constraint_name)s`",
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
#     "pk": "pk_%(table_name)s"
#     })

# db = SQLAlchemy()



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
    player_image = db.Column(db.String)
    total_wins = db.Column(db.Integer)
    total_games = db.Column(db.Integer)

    serialize_rules = ('-password_hash',)
    
    @hybrid_property
    def password_hash(self):
        return self._password_hash
        # raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8')
        )
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8')
        )

    def __repr__(self):
        return f'<User {self.username}>'


    
class Game(db.Model,SerializerMixin):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    playerA = db.Column(db.Integer, db.ForeignKey('players.id'))
    playerB = db.Column(db.Integer, db.ForeignKey('players.id'))
    ended = db.Column(db.Boolean)
  
    # players = db.relationship('Player', backref='game')
    
    
    
    serialize_rules = ('-password_hash', '-total_wins', '-total_games')    

class Tile(db.Model,SerializerMixin):
    __tablename__ = 'tiles'
    serialize_rules = ()
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    

class Game_tile(db.Model, SerializerMixin):
    __tablename__ = 'game_tiles'
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    tile_id = db.Column(db.Integer, db.ForeignKey('tiles.id'))

    games = db.relationship('Game', backref='game_tile')
    tiles = db.relationship('Tile', backref='game_tile')
   
    serialize_rules = ('-password_hash', '-player_image', '-total_wins', '-total_games')
