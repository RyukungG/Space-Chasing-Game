from turtle import Turtle, Screen

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
