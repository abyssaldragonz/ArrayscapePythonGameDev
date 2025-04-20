# This file manages 
####################################################################################################
import pygame # the main module for python game dev
import random # a built-in module for random choice

from models import GameObject # import the GameObject class from models.py
from utils import load_sprite # import load_sprite function from the utils.py file

# GAME CLASS ###################################################################################################
class AsteroidsGame:
    def __init__(self): # create a new game
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600)) # create a display
        self.background = load_sprite("space", False) # set the background
        self.clock = pygame.time.Clock()
        self.spaceship = GameObject((400,300), load_sprite("spaceship"), (0,0)) # create a new spaceship (player)


    def main_loop(self): # run the game
        while True:
            self._handle_input() # handle any user input
            self._process_game_logic() # process the logic behind the game
            self._draw() # draw the sprites and output


    def _init_pygame(self): # start the game display 
        pygame.init()
        pygame.display.set_caption("Asteroids by Arrayscape")


    def _handle_input(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # exit the game by pressing the close window [X] button
                quit()


    def _process_game_logic(self):
        self.spaceship.move()
    

    def _draw(self): # update the display with sprites
        self.screen.blit(self.background, (0, 0)) # this is the background for the game

        self.spaceship.draw(self.screen)

        pygame.display.flip() # used to update the display
        self.clock.tick(60)
