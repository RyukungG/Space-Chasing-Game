from turtle import Turtle, Screen

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 10
        self.color = "white"
        self.turtle = Turtle()
        self.screen = Screen()
        self.turtle.penup()
        self.turtle.speed(self.speed)
        self.turtle.color(self.color)

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
        self.screen.mainloop()
        self.x, self.y = self.turtle.pos()

