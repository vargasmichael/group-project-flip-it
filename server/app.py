#!/usr/bin/env python3

# Local imports

from flask import Flask, request, make_response, jsonify, session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError

# from config import app, api
from models import db, Player, Game, Tile, Game_tile

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Signup(Resource):
    def post(self):
        print('starting')
        request_json = request.get_json()

        username = request_json.get("username")
        password = request_json.get('password')
        
        player = Player(
            username = username
        )

        player.password_hash = password

        print('first')
        
        try:
            print('here')

            db.session.add(player)
            db.session.commit()

            session ['player_id'] = player.id

            print(player.to_dict(), 201)
        
        except IntegrityError:

            print ("no, here!")

            return {'error': '422 Unprocessable Entity'}, 422
api.add_resource(Signup, '/signup', endpoint='signup')



class CheckSession(Resource):
    
    def get(self):
        if session.get('player_id'):
            player = Player.query.filter(Player.id == session['player_id']).first()
            return player.to_dict(), 200
        
        return {'error': '401 Unauthorized'}, 401

api.add_resource(CheckSession, '/check_session', endpoint='check_session')

class Login(Resource):

    def post(self):

        request_json = request.get_json()

        username = request_json.get('username')
        password = request_json.get('password')

        player = Player.query.filter(Player.username == username).first()

        if player:
            if player.authenticate(password):
                print("authenticat")
                session['user_id'] = player.id
                return player.to_dict(), 200
        
        return make_response({'error': '401 Unauthorized'},401) 

api.add_resource(Login, '/login', endpoint='login')


class Logout(Resource):
    
    def delete(self):

        if session.get('player_id'):
            session['player_id'] = None
            return {}, 204
        
        return {'error': '401 Unauthorized'}, 401

api.add_resource(Logout, '/logout', endpoint='logout')



class All_Players(Resource):
    def get(self):
        all_players = Player.query.all()
        player_list = []
        
        for player in all_players:
            new_player = {
                'id': player.id,
                'username': player.username,
                'player_image': player.player_image,
                'total_wins': player.total_wins,
                'total_games': player.total_games
            }
            player_list.append(new_player)
        return make_response(jsonify(player_list), 200)
    
    
    def post(self):
        data = request.get_json()
        new_player = Player(
            username = data['username'],
            player_image = data['player_image'],
            total_wins = data['total_wins'],
            total_games = data['total_games']
        )
        db.session.add(new_player)
        db.session.commit()
        return make_response(new_player.to_dict(), 201)
    
api.add_resource(All_Players, '/players')



class Player_By_Id(Resource):
    def get(self, id):
        player = Player.query.filter_by(id=id).first()
        if not player:
            return make_response(jsonify({'error': 'Player not found'}), 404)
        response = make_response(player.to_dict(), 200)
        return response
    
    def delete(self, id):
        player = Player.query.filter_by(id=id).first()
        if not player:
            return make_response(jsonify({'error': 'Player not found'}), 404)
        db.session.delete(player)
        db.session.commit()
        return make_response(jsonify({'message': 'Boy Bye!'}), 200)
    
    
api.add_resource(Player_By_Id, '/players/<int:id>')



class All_Tiles(Resource):
    def get (self):
        all_tiles = Tile.query.all()
        tile_list = []
        
        for tile in all_tiles:
            new_tile = {
                'id': tile.id,
                'image': tile.image
            }
            tile_list.append(new_tile)
        return make_response(jsonify(tile_list), 200)
    
api.add_resource(All_Tiles, '/tiles')


class Player_by_id(Resource):
    def get(self, id):
game = Game.query.filter(Game.id == session["game_id"]).first()
playerA = Player.query.filter(Player.id == game.playerA).first()
playerB = Player.query.filter(Player.id == game.playerB).first()

# a way to get both players and the game

if __name__ == '__main__':
    app.run(debug=True)