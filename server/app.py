#!/usr/bin/env python3

# Local imports

from flask import session, make_response, request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, api
from models import In_Play, Game, PGT, Player, Card



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


if __name__ == '__main__':
    app.run(port=5555, debug=True)
