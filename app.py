from character import Player, Enemy
from scoreboard import Score
from screen import GameScreen
from turtle import Turtle, Screen
import time


background = GameScreen(600, 600)
player_name = background.screen.textinput("Player Name", "Enter your name")
p = Player()
all_enemy = []
scoreboard = Score("scoreboard")

while True:
    p.control()

    score = time.time() - p.lifetime
    print(int(score))
    if int(score) % 10 == 0:
        new_e = Enemy(p, player_name)
        all_enemy.append(new_e)
    for e in all_enemy:
        e.chase(p, player_name)
    background.screen.update()
