from turtle import Turtle, Screen

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 10
        self.turtle = Turtle()
        self.screen = Screen()
        self.turtle.penup()

    def player_speed(self):
        self.turtle.speed(self.speed)

    def walk_forward(self):
        self.turtle.forward(1)

    def walk_backwards(self):
        self.turtle.backward(1)

    def turn_left(self):
        self.turtle.left(1)

    def turn_right(self):
        self.turtle.right(1)

    def control(self):
        self.screen.onkeypress(self.walk_forward, "Up")
        self.screen.onkeypress(self.walk_backwards, "Down")
        self.screen.onkeypress(self.turn_right, "Right")
        self.screen.onkeypress(self.turn_left, "Left")
        self.screen.listen()
        self.screen.mainloop()
        self.x, self.y = self.turtle.pos()

