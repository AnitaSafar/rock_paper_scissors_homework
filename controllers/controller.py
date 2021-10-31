from flask import render_template
from app import app
from models.game import Game
from models.player import Player



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<p1_choice>/<p2_choice>')
def game_outcome(p1_choice, p2_choice):
    player1 = Player("Erin", p1_choice)
    player2 = Player("Helen", p2_choice)
    winner = Game().winning_player(player1, player2)
    return render_template("index.html", p1_choice=p1_choice, p2_choice=p2_choice, winner=winner)
