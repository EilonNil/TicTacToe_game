import pygame

IMAGE = "images\\circle.png"


class Circle(pygame.sprite.Sprite):
    pygame.init()

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.image = pygame.image.load(IMAGE).convert()

    def get_pos(self):
        return self.x, self.y
