from character import Player, Enemy
from turtle import Turtle, Screen
background = Screen()
background.screensize(600, 600)
background.bgcolor("black")
p = Player()
e = Enemy()
e.turtle.setposition(e.x, e.y)
p.control()
e.chase(p)
background.mainloop()

