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
        tao_write = WriteScreen("circle", 0.1)
        tao_write_score = WriteScreen("circle", 0.1)
        tao_write_score.turtle.goto(360-(len(player_name)*5), 280)
        p = Player()
        all_enemy = []

        tao_write.turtle.goto(300-(len(player_name)*5), 300)
        tao_write.turtle.write("Name: ", True, align="left", font=("Consolas", 13, "bold"))
        tao_write.turtle.write(f"{player_name}", True, font=("Consolas", 13, "bold"))
        tao_write.turtle.goto(300-(len(player_name)*5), 280)
        tao_write.turtle.write("Score: ", True, align="left", font=("Consolas", 13, "bold"))

        while True:
            p.control()

            score = time.time() - p.lifetime
            tao_write_score.turtle.clear()
            tao_write_score.turtle.write(f"{int(score)}", align="left", font=("Consolas", 13, "bold"))
            if int(score) % 10 == 0:
                new_e = Enemy(p, player_name)
                all_enemy.append(new_e)
            for e in all_enemy:
                e.chase(p, player_name)

            self.screen.update()

    def menu(self):
        pass

