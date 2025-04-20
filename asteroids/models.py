# This file manages all the game objects like the spaceship (player), the asteroids, and the bullets
####################################################################################################
from pygame.math import Vector2

# general template to follow for game objects
class GameObject:
    def __init__(self, position, sprite, velocity): # initialize the game object
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface): # draw the sprite of the game object
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self): # move the game object to a new position
        self.position = self.position + self.velocity

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius # returns whether the game object has collided with another