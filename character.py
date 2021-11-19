from turtle import Turtle, Screen
from scoreboard import Score
import random
import time


class Character:
    def __init__(self, color, speed, x=0, y=0):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.turtle = Turtle()
        self.screen = Screen()
        self.turtle.penup()
        self.turtle.speed(self.speed)
        self.turtle.color(self.color)

    @property
    def hitbox(self):
        return [[self.x - 5, self.x + 5], [self.y - 5, self.y + 5]]


class Player(Character):
    def __init__(self):
        super().__init__("white", 10)
        self.lifetime = time.time() # start time

    def walk_forward(self):
        self.turtle.forward(5)
        self.x, self.y = self.turtle.pos()

    def walk_backward(self):
        self.turtle.backward(5)
        self.x, self.y = self.turtle.pos()

    def turn_left(self):
        self.turtle.left(10)
        self.x, self.y = self.turtle.pos()

    def turn_right(self):
        self.turtle.right(10)
        self.x, self.y = self.turtle.pos()

    def quit(self):
        self.screen.bye()

    def control(self):
        self.screen.onkeypress(self.walk_forward, "Up")
        self.screen.onkeypress(self.walk_backward, "Down")
        self.screen.onkeypress(self.turn_right, "Right")
        self.screen.onkeypress(self.turn_left, "Left")
        self.screen.onkey(self.quit, "q")
        self.screen.listen()



class Enemy(Character):
    def __init__(self):
        super().__init__("red", 5, random.randint(-400, 400), random.randint(-400, 400))
        self.score = Score("scoreboard")

    def hit(self, player, player_name):
        if player.hitbox[0][0] <= self.x <= player.hitbox[0][1] \
                and player.hitbox[1][0] <= self.y <= player.hitbox[1][1]:
            stop = time.time()  # stop time
            score = stop - player.lifetime
            self.score.insert(player_name, int(score))
            exit()


    def chase(self, player, player_name):
        self.turtle.setheading(self.turtle.towards(player.turtle.pos()))
        self.turtle.forward(5)
        self.x, self.y = self.turtle.pos()
        if player.hitbox[0][0] <= self.x <= player.hitbox[0][1] \
                and player.hitbox[1][0] <= self.y <= player.hitbox[1][1]:
            self.hit(player, player_name)
        self.screen.ontimer(self.chase(player, player_name), 1)


