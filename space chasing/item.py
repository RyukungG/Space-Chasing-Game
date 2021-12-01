from character import Item
import random


class Nuke(Item):
    def __init__(self, e_list):
        super().__init__("resource/nuke.gif")
        self.e_list = e_list

    def clear_map(self):
        for e in self.e_list:
            e.turtle.ht()
            e.turtle.clear()
            e.turtle.goto(1000, 1000)
            self.x, self.y = self.turtle.pos()
        self.e_list.clear()

    def activate(self):
        self.clear_map()


class EnderPearl(Item):
    def __init__(self, player):
        super().__init__("resource/Ender_Pearl.gif")
        self.player = player
        self.player_x = random.randint(-250, 250)
        self.player_y = random.randint(-250, 250)

    def teleport(self):
        self.player.turtle.setposition(self.player_x, self.player_y)
        self.player.x, self.player.y = self.turtle.pos()

    def activate(self):
        self.teleport()
