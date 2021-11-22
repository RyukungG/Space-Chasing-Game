from character import Player, Enemy
from scoreboard import Score
from screen import GameScreen
from turtle import Turtle, Screen
import time


background = GameScreen(600, 600)

scoreboard = Score("scoreboard")

background.play()
