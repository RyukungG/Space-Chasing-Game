from character import Player, Enemy
from scoreboard import Score
from turtle import Turtle, Screen
import time


background = Screen()
background.screensize(600, 600)
background.bgcolor("black")
player_name = background.textinput("Player Name", "Enter your name")
p = Player()
e = Enemy()
scoreboard = Score("scoreboard")

e.turtle.setposition(e.x, e.y)

e.hit(p, player_name)
p.control()
e.chase(p)

background.mainloop()



