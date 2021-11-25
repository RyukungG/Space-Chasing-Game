from turtle import Turtle, Screen
from scoreboard import Score
import random
import time


class Character:
    """
    Define a Character with position, color and speed
    """
    def __init__(self, color, speed, x=0, y=0):
        """
        initialize new character
        :param color: string
        :param speed: int
        :param x: number
        :param y: number
        """
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
    def x(self):
        """
        get or set value of x
        """
        return self.__x

    @x.setter
    def x(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("The x attribute must be a number")
        self.__x = num

    @property
    def y(self):
        """
        get or set value of y
        """
        return self.__y

    @y.setter
    def y(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("The y attribute must be a number")
        self.__y = num

    @property
    def color(self):
        """
        get or set color
        """
        return self.__color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self.__color = color

    @property
    def speed(self):
        """
        get or set speed
        """
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, int):
            raise TypeError("speed must be a integer")
        self.__speed = speed

    @property
    def hitbox(self):
        """
        create character hitbox
        :return: list of character hitbox
        """
        return [[self.x - 5, self.x + 5], [self.y - 5, self.y + 5]]


class Player(Character):
    """
    Define a Player with life time
    """
    def __init__(self):
        """
        initialize new player
        """
        super().__init__("white", 10)
        self.lifetime = time.time() # start time

    def walk_forward(self):
        """
        Move the player forward
        """
        self.turtle.forward(5)

    def walk_backward(self):
        """
        Move the player backward
        """
        self.turtle.backward(5)

    def turn_left(self):
        """
        Turn player left
        """
        self.turtle.left(10)

    def turn_right(self):
        """
        Turn player right
        """
        self.turtle.right(10)

    def quit(self):
        """
        quit the game
        """
        self.screen.bye()

    def control(self):
        """
        control the player and update player position
        """
        self.screen.onkeypress(self.walk_forward, "Up")
        self.screen.onkeypress(self.walk_backward, "Down")
        self.screen.onkeypress(self.turn_right, "Right")
        self.screen.onkeypress(self.turn_left, "Left")
        self.screen.onkey(self.quit, "q")
        self.x, self.y = self.turtle.pos()
        self.screen.listen()


class Enemy(Character):
    """
    Define a Enemy with random position
    """
    def __init__(self):
        """
        initialize new enemy
        """
        super().__init__("red", 0, random.randint(-400, 400), random.randint(-400, 400))
        self.score = Score("scoreboard")
        self.turtle.setposition(self.x, self.y)
        self.hit_p = False

    def hit(self, player, player_name):
        """
        check that enemy hit player hitbox or not
        :param player: Player Object
        :param player_name: string
        """
        if player.hitbox[0][0] <= self.x <= player.hitbox[0][1] \
                and player.hitbox[1][0] <= self.y <= player.hitbox[1][1]:
            stop = time.time()  # stop time
            score = stop - player.lifetime
            self.score.insert(player_name, int(score))
            self.screen.clear()
            self.hit_p = True

    def chase(self, player, player_name):
        """
        find and go to player position
        :param player: Player Object
        :param player_name: string
        """
        self.turtle.setheading(self.turtle.towards(player.turtle.pos()))
        self.turtle.forward(7)
        self.x, self.y = self.turtle.pos()
        self.hit(player, player_name)


class WriteScreen(Character):
    """
    Define a screen writer
    """
    def __init__(self, shape, size):
        """
        initialize new WriteScreen
        :param shape: string
        :param size: float
        """
        super().__init__("white", 0)
        self.turtle.shape(shape)
        self.turtle.shapesize(size)
        self.turtle.penup()
        self.turtle.hideturtle()





