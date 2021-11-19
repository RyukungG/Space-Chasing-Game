from character import Player, Enemy
from scoreboard import Score
from screen import GameScreen
from turtle import Turtle, Screen
import time


background = GameScreen(600, 600)
background.create_screen()
player_name = background.screen.textinput("Player Name", "Enter your name")
p = Player()
e = Enemy()
scoreboard = Score("scoreboard")

e.turtle.setposition(e.x, e.y)


p.control()
e.chase(p, player_name)

background.mainloop()

