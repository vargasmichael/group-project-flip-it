#!/usr/bin/env python3

# Local imports

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
# these imports are for the websocket 
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)


# this is the websocket route
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('my_event', {'data': 'Connected'})

@socketio.on('my_event')
def test_message(message):
    emit('my_response', {'data': 'Hello, World!'})

# if __name__ == '__main__':
#     socketio.run(app)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
