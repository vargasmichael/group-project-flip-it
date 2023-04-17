# flask db init
#flask db revision --autogenerate -m'message'
# flask db upgrade
# python db/seed.py


from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt

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

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

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
    
class Card(db.Model,SerializerMixin):
    __tablename__ = 'cards'
    serialize_rules = ()
    id = db.Column(db.Integer, primary_key=True)
    values = db.Column(db.Integer)
    suits = db.Column(db.String)
    status = db.Column(db.Integer)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))