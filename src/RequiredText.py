import pygame as pg
import pyjokes
from src.consts_and_paths import *
import random


class RequiredText:
    def __init__(self):
        self.rect_bg = None
        self.rect = None
        self.text_bg = None
        self.text = None
        self.font = pg.font.SysFont('georgia', text_size, False,
                                    False)  # font and size of output text(joke)
        self.output_text = 'Are you ready?'  # output text before start
        self.text_set()

    def text_set(self):
        self.text = self.font.render(self.output_text, True, 'yellow')  # output text character
        self.text_bg = self.font.render(self.output_text, True, 'black')  # output text tint character
        self.rect = self.text.get_rect(center=(size_of_screen[0] // 2, 105))  # 105 is coord_y of joke
        self.rect_bg = self.text_bg.get_rect(center=(size_of_screen[0] // 2 + 1, 106))  # 106 is coord_y of joke's tone

    def blit(self, screen):
        screen.blit(self.text_bg, self.rect_bg)
        screen.blit(self.text, self.rect)

    def get_text(self):
        pass

    def update(self, new_text):
        self.output_text = new_text
        self.text_set()


class Joke(RequiredText):
    def get_text(self):
        self.output_text = pyjokes.get_joke(language='en', category='all')
        self.output_text = self.output_text[:90]
        print(self.output_text)
        self.text_set()


class Wiki(RequiredText):
    def get_text(self):
        f = open('src/wiki.txt')
        rand = random.randint(0, 273)
        self.output_text = str(f.readlines()[rand])
        self.output_text = self.output_text[:-2]
        self.output_text = self.output_text[:90]
        self.output_text.strip()
        print(self.output_text)
        self.text_set()
        f.close()
