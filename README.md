# Project Space Chasing Game

---

## About this project
In this game, player has to control the player's spaceship to dodge enemy ships that are chasing the player.
Which during the game will have item drops for player to collect. If player collides with enemy it will make the game over.
After that the game will show top 5 scoreboard and update score into the `scoredata.json` file

***
## Project overview and features
The main program will ask user for player name which will be collected with player score in `scoredata.json`
### Main features
* User can control player spaceship by using arrow keys
* Score is count by seconds -every 1 second = 1 score-
* Enemy spaceships with chasing player
* Enemy will spawn every 10 seconds, and it's speed also increase
* Player can collect item
* item "Nuke" will clear all enemy
* item "Ender pearl" will teleport player to anywhere on the screen
* Scoreboard with top 5 high score
* ester egg

***
## Requirement
### Module
* `turtle`
* `os`
* `json`
* `time`
* `random`

please download font `Consolas` into your computer.

***
## Code structure
My application have 6(+1) main file which are `character.py`, `scoreboard.py`,
`screen.py`, `item.py`, `secret.json`, `app.py`, `scoredata.json`

### 1.`character.py`
This module contains `Character` class for creating character object, 
`Player` class that is a subclass of `Character` for create and control player, 
`Enemy` class that is a subclass of `Character` for create enemy and chase player and 
`WriteScreen` class that is a subclass of `Character` for screen writer.
`Item` class that is a subclass of `Character` for create item and check that player collect item or not.

### 2.`scoreboard.py`
This module contains the `Score` class for creating and sorting a score database file.

### 3.`screen.py`
This module contains `GameScreen` class for creating screen,
`Border` class that is a subclass of `GameScreen` for create a border surrounding map, 
`RunScreen` class that is a subclass of `GameScreen` for use of all the modules above and combine all functions to run entire game. 

### 4.`item.py`
This module contains `Nuke` class that is a subclass of `Item` from `character.py` for create nuke item and 
`EnderPearl` class that is a subclass of `Item` class for create ender pearl item

### 5.`secret.json`
json file for collecting ester egg data

### 6.`app.py`
This module implements an application that demonstrates the use of screen modules.

### 7.`scoredata.json`
json file for collecting player score from `scoreboard.py`

-This file auto generate by `scoreboard.py`- 

;)
