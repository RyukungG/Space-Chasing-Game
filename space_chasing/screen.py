from turtle import Screen
from character import Player, Enemy, WriteScreen
from scoreboard import Score
import item
import time
import os
import json
import random


class GameScreen:
    """
    Define a game screen with width, and height.
    """
    def __init__(self, width, height):
        """
        initialize new border
        :param width: float
        :param height: float
        """
        self.width = width
        self.height = height
        self.screen = Screen()

    @property
    def width(self):
        """
        get or set value of the width
        """
        return self.__width

    @width.setter
    def width(self, w):
        # check if width is int or float or not and width is less than zero or not
        if not isinstance(w, (int, float)):
            raise TypeError("width must be a number")
        if w <= 0:
            raise ValueError("width must be greater than zero")
        self.__width = w

    @property
    def height(self):
        """
        get or set value of the height
        """
        return self.__height

    @height.setter
    def height(self, h):
        # check if height is int or float or not and height is less than zero or not
        if not isinstance(h, (int, float)):
            raise TypeError("height must be a number")
        if h <= 0:
            raise ValueError("height must be greater than zero")
        self.__height = h

    def create_screen(self):
        """
        create program screen
        """
        self.screen.screensize(self.width, self.height)
        self.screen.setworldcoordinates(-300, -300, 300, 300)
        self.screen.bgcolor("black")


class Border(GameScreen):
    """
    Define a border in 2D space with the lower-left corner, width, and height.
    """
    def __init__(self, width, height):
        """
        initialize new border
        :param width: float
        :param height: float
        """
        super().__init__(width, height)
        self.x = -300
        self.y = -300

    @property
    def left(self):
        """
        get value on the left side of the border
        """
        return self.x

    @property
    def right(self):
        """
        get value on the right side of the border
        """
        return self.x + self.width

    @property
    def bottom(self):
        """
        get value on the bottom side of the border
        """
        return self.y

    @property
    def top(self):
        """
        get value on the top side of the border
        """
        return self.y + self.height


class RunScreen(GameScreen):
    """
    Define a run program screen.
    """
    def __init__(self, width, height, logo):
        """
        initialize new game screen
        :param width: float
        :param height: float
        :param logo: file logo name(string)
        """
        super().__init__(width, height)
        self.logo = logo
        self.url = ""
        self.player_name = ""
        self.score = Score("scoredata")
        self.border = Border(self.width, self.height)
        self.create_screen()

    def play(self):
        """
        It is a function that run the game and check whether the player collides with the border or not.
        Spawn enemy every 10 seconds, spawn item(nuke and ender pearl) and show player name
        and score on the top right corner
        """
        self.screen.addshape("resource/nuke.gif")
        self.screen.addshape("resource/Ender_Pearl.gif")
        tao_write = WriteScreen("circle", 0.1)
        tao_write_score = WriteScreen("circle", 0.1)
        tao_write_score.turtle.goto(300 - (len(self.player_name) * 7), 270)
        p = Player()
        all_enemy = []
        all_item = []
        score = 0

        tao_write.turtle.goto(250 - (len(self.player_name) * 7), 290)
        tao_write.turtle.write(f"Name: {self.player_name}", True,
                               align="left", font=("Consolas", 13, "bold"))
        tao_write.turtle.goto(250 - (len(self.player_name) * 7), 270)
        tao_write.turtle.write("Score: ", True,
                               align="left", font=("Consolas", 13, "bold"))
        # run game
        while True:
            p.control()

            # check player hit border or not
            if p.y <= self.border.bottom:
                p.turtle.goto(p.x, self.border.bottom)
            if p.y >= self.border.top:
                p.turtle.goto(p.x, self.border.top)
            if p.x <= self.border.left:
                p.turtle.goto(self.border.left, p.y)
            if p.x >= self.border.right:
                p.turtle.goto(self.border.right, p.y)

            score = int(time.time() - p.lifetime)
            tao_write_score.turtle.clear()
            tao_write_score.turtle.write(f"{score}",
                                         align="left", font=("Consolas", 13, "bold"))

            # enemy part
            if score % 10 == 0:
                new_e = Enemy()
                all_enemy.append(new_e)
            for e in all_enemy:
                e.chase(p, self.player_name, score/10)
            if any(e.hit_p for e in all_enemy):
                break

            # item part
            if score % 60 == 0 and score != 0 and len(all_item) == 0:
                nuke = item.Nuke(all_enemy)
                all_item.append(nuke)
            if score % 25 == 0 and score != 0 and len(all_item) == 0:
                ender_pearl = item.EnderPearl(p)
                all_item.append(ender_pearl)
            for i in all_item:
                i.collect(p, all_item)

            self.screen.update()

    def scoreboard(self):
        """
        create and show top 5 scoreboard
        """
        self.screen.bgcolor("black")
        all_score = self.score.sort_score()
        tao_write = WriteScreen("circle", 0.1)
        tao_write.turtle.goto(0, 200)
        tao_write.turtle.write("ScoreBoard",
                               align="center", font=("Consolas", 40, "bold"))

        if len(all_score) < 5:
            r = range(1, len(all_score) + 1)
        else:
            r = range(1, 6)
        for i in r:
            tao_write.turtle.goto(-145, (200 - (i * 70)))
            tao_write.turtle.color("white")
            tao_write.turtle.write(f"{all_score[i - 1][0]}: ", True,
                                   align="left", font=("Consolas", 40, "bold"))
            tao_write.turtle.color("cyan")
            tao_write.turtle.write(f"{all_score[i - 1][1]}",
                                   align="left", font=("Consolas", 40, "bold"))
        tao_space = WriteScreen("circle", 0.1)
        tao_space.turtle.goto(0, (200 - ((r[-1] + 1) * 70)))
        tao_space.turtle.write(f"Press Space bar to continue",
                               align="center", font=("Consolas", 30, "bold"))
        tao_space.turtle.goto(0, (200 - ((r[-1] + 2) * 70)))
        tao_space.turtle.write(f"Press esc to quit",
                               align="center", font=("Consolas", 30, "bold"))

        self.screen.onkey(self.menu, "space")
        self.screen.onkey(self.quit_game, "Escape")
        self.screen.listen()
        self.screen.mainloop()

    def quit_game(self):
        """
        quit game and run an ester egg
        """
        with open("secret.json", "r") as secret:
            data = json.load(secret)
        if self.player_name not in data:
            key = "normal"
        else:
            key = self.player_name
        self.url = data[key][random.randint(0, len(data[key])-1)]  # random ester egg link
        # check that this computer is window or mac os
        if os.name == "nt":
            os.system(f"start \"\" {self.url}")
        else:
            os.system(f"open \"\" {self.url}")

        exit()

    def menu(self):
        """
        create menu start game with logo
        """
        self.screen.reset()
        self.screen.addshape(self.logo)
        logo = WriteScreen(self.logo, 0.1)
        logo.turtle.goto(0, 130)
        logo.turtle.showturtle()
        logo = WriteScreen("circle", 0.1)
        logo.turtle.goto(0, -100)
        logo.turtle.write(f"Press Space bar to start",
                          align="center", font=("Consolas", 30, "bold"))
        self.screen.onkey(self.start, "space")
        self.screen.listen()
        self.screen.mainloop()

    def start(self):
        """
        combine all function to run game
        """
        self.screen.clear()
        self.create_screen()
        self.player_name = self.screen.textinput("Player Name", "Enter your name").upper()
        self.play()
        self.scoreboard()
