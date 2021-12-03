from character import Item
import random


class Nuke(Item):
    """
    Define a Nuke item
    """
    def __init__(self, e_list):
        """
         initialize new nuke
        :param e_list: list of enemy
        """
        super().__init__("resource/nuke.gif", 30)
        self.e_list = e_list

    def clear_map(self):
        """
        clear all enemy object on the map
        """
        for e in self.e_list:
            e.turtle.ht()
            e.turtle.clear()
            e.turtle.goto(1000, 1000)
            self.x, self.y = self.turtle.pos()
        self.e_list.clear()

    def activate(self):
        """
        activate function
        """
        self.clear_map()


class EnderPearl(Item):
    """
    Define a EnderPearl item
    """
    def __init__(self, player):
        """
         initialize new EnderPearl
        :param player: Player object
        """
        super().__init__("resource/Ender_Pearl.gif", 20)
        self.player = player
        self.player_x = random.randint(-290, 290)
        self.player_y = random.randint(-290, 290)

    def teleport(self):
        """
         teleport player around the map
        """
        self.player.turtle.setposition(self.player_x, self.player_y)
        self.player.x, self.player.y = self.turtle.pos()

    def activate(self):
        """
        activate function
        """
        self.teleport()
