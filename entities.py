import pygame

pygame.init()

class enemy:
    def __init__(self, img, x, y, speed, is_dead, x_change, y_change):
        self.img = img
        self.x = x
        self.y = y
        self.speed = speed
        self.hitbox = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        self.is_dead = is_dead
        self.x_change = x_change
        self.y_change = y_change

class player:
    def __init__(self,img, x, y, x_change, speed):
        self.img = img
        self.x = x
        self.y = y
        self.x_change = x_change
        self.speed = speed

class bullet:
    def __init__(self, img, x, y, speed, y_change, state):
        self.img = img
        self.x = x
        self.y = y
        self.speed = speed
        self.y_change = y_change
        self.state = state