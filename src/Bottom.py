import pygame as pg
from src.consts_and_paths import *


class Bottom:
    def __init__(self, size: tuple, image, color, coord):
        self.size = size
        self.image = pg.transform.scale(image, self.size)
        self.color = color
        self.rect = self.image.get_rect(topleft=coord)

    def blit(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, self.rect)
