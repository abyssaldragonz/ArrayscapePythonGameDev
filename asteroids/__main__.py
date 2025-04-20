# ASTEROIDS
# Arrayscape Gaming 2025
# Developed by Josephine Lee
# Inspiration: https://realpython.com/asteroids-game-python/
###################################################################################################
# This file runs the main game! Run this file as your Python program to start the game!
####################################################################################################

from game import AsteroidsGame

if __name__ == "__main__":
    space_rocks = AsteroidsGame()
    space_rocks.main_loop()