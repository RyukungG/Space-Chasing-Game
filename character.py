from turtle import Turtle, Screen
import random

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

class Player(Character):
    def __init__(self):
        super().__init__("white", 10)

    def walk_forward(self):
        self.turtle.forward(5)

    def walk_backwards(self):
        self.turtle.backward(5)

    def turn_left(self):
        self.turtle.left(10)

    def turn_right(self):
        self.turtle.right(10)

    def control(self):
        self.screen.onkeypress(self.walk_forward, "Up")
        self.screen.onkeypress(self.walk_backwards, "Down")
        self.screen.onkeypress(self.turn_right, "Right")
        self.screen.onkeypress(self.turn_left, "Left")
        self.screen.listen()
        self.x, self.y = self.turtle.pos()

class Enemy(Character):
    def __init__(self):
        super().__init__("red", 5, random.randint(-400, 400), random.randint(-400, 400))

    def chase(self, player):
        self.turtle.setheading(self.turtle.towards(player.turtle.pos()))
        self.turtle.forward(5)
        self.screen.ontimer(self.chase(player), 1)

