#!/usr/bin/env python3

from random import randint, choice as rc


from app import app
from models import db, Player, Game, Tile, Game_tile



with app.app_context():
    db.drop_all()
    db.create_all()
    
    print("Deleting data...")
    Player.query.delete()
    Game.query.delete()
    Tile.query.delete()
    Game_tile.query.delete()
    

    # Create some player data
    print("Creating player data...")
    p1 = Player(username = 'Dylan', _password_hash = 'null', player_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4JZfpQ6mVj8ln6iivtg2ozj3BlLfD4aXRZg&usqp=CAU', total_wins = 0, total_games = 0)
    p2 = Player(username = 'Ben', _password_hash = 'null', player_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfUpKuFE2IyiOg93GdJfY7YL0iXGnRfdkBHw&usqp=CAU', total_wins = 0, total_games = 0)
    p3 = Player(username = 'Abby', _password_hash = 'null', player_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNECPASq1pw7Xma3LjngqyS0438ZWubBT6_A&usqp=CAU', total_wins = 0, total_games = 0)
    p4 = Player(username = "Michael", _password_hash = 'null', player_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRj8dNYETUxRctek5phC5h1RuPnyybW21FpqQ&usqp=CAU', total_wins = 0, total_games = 0)
    players = [p1, p2, p3, p4]
    db.session.add_all(players)
    db.session.commit()
    
    print("Creating game data...")
    g1 = Game(playerA = p1.id, playerB = p2.id)
    g2 = Game(playerA = p3.id, playerB = p4.id)
    games = [g1, g2]
    db.session.add_all(games)
    db.session.commit()
    
    print("Creating tile data...")
    t1 = Tile(image ='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShE_ulBMMi7j6WzQOABxEXuwPR_InXAfO7-g&usqp=CAU')
    t2 = Tile(image ='https://www.alamy.com/stock-photo-nicolas-cage-who-is-an-american-actor-may-1987-20135664.html?imageid=E32C2975-F6A6-4AA5-964D-E56E3E97E3D6&p=62486&pn=1&searchId=f327ae3a17a670e3166d7f5e453c7a6f&searchtype=0')
    t3 = Tile(image ='https://www.alamy.com/stock-photo-nicolas-cage-visits-live-with-regis-and-kelly-taping-out-and-about-38193934.html?imageid=9184C68A-7963-45F9-A352-07242930F02F&p=96050&pn=1&searchId=f327ae3a17a670e3166d7f5e453c7a6f&searchtype=0')
    t4 = Tile(image ='https://www.alamy.com/stock-photo-spiel-auf-zeit-snake-eyes-nicolas-cage-rick-santoro-nicolas-cage-laesst-52949774.html?imageid=C930FF2C-F4E8-4A19-B8CC-927FC83493A4&p=1238264&pn=1&searchId=f327ae3a17a670e3166d7f5e453c7a6f&searchtype=0')
    t5 = Tile(image ='https://www.alamy.com/stock-photo-celebbrity-fight-night-a-firenze-nicolas-cage-120487947.html?imageid=AB588B6F-4B58-4B1A-919C-A7671B1F9BD8&p=312144&pn=2&searchId=8bbcd091b3a38f793f2bb14ff6a66e3f&searchtype=0')
    t6 = Tile(image ='https://www.alamy.com/stock-photo-jo-kinsey-hair-and-colour-artist-at-madame-tussauds-puts-the-finishing-106617286.html?imageid=D631FABE-47BC-418A-AB91-6300854E65B4&p=309285&pn=2&searchId=8bbcd091b3a38f793f2bb14ff6a66e3f&searchtype=0')
    tiles = [t1, t2, t3, t4, t5, t6]
    db.session.add_all(tiles)
    db.session.commit()
    
    
   
    
   
   