from turtle import Turtle, Screen
from character import Player, Enemy, WriteScreen
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
        tao_write = WriteScreen()
        p = Player()
        all_enemy = []

        tao_write.turtle.penup()
        tao_write.turtle.goto(300, 300)
        tao_write.turtle.write("Name: ", True, align="left", font=("Consolas", 13, "bold"))
        tao_write.turtle.write(f"{player_name}", True, font=("Consolas", 13, "bold"))
        tao_write.turtle.goto(300, 280)
        tao_write.turtle.write("Score: ", True, align="left", font=("Consolas", 13, "bold"))

        while True:
            p.control()

            score = time.time() - p.lifetime
            tao_write.turtle.write(f"{int(score)}", align="left", font=("Consolas", 13, "bold"))
            if int(score) % 10 == 0:
                new_e = Enemy(p, player_name)
                all_enemy.append(new_e)
            for e in all_enemy:
                e.chase(p, player_name)

            self.screen.update()
