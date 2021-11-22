from turtle import Turtle, Screen
from character import Player, Enemy
import time

class GameScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = Screen()
        self.turtle = Turtle()
        self.create_screen()

    def create_screen(self):
        self.screen.screensize(600, 600)
        self.screen.bgcolor("black")

    def play(self):
        player_name = self.screen.textinput("Player Name", "Enter your name")
        p = Player()
        all_enemy = []
        while True:
            p.control()

            score = time.time() - p.lifetime
            print(int(score))
            if int(score) % 10 == 0:
                new_e = Enemy(p, player_name)
                all_enemy.append(new_e)
            for e in all_enemy:
                e.chase(p, player_name)

            self.screen.update()
