from screen import RunScreen
from turtle import title

# create RunScreen object
background = RunScreen(600, 600, "resource/SPACE_CHASING.gif")

# run game
title("SPACE CHASING")
background.menu()
