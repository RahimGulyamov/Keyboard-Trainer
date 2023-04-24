import pygame as pg
from src.consts_and_paths import *
import time


class Key:
    def __init__(self, let, col='white'):
        self.letter = let
        self.color = col
        self.proper_use = 0
        self.mistakes = 0
        self.time = 0


class KeyboardLine:
    def __init__(self, x, y, keys_from_to, size):
        self.x = x
        self.y = y
        self.keys = keys_from_to
        self.size = size


class Keyboard:
    def __init__(self, screen):
        self.screen = screen
        self.text_size = 30
        self.key_size = (50, 50)
        self.key_space_size = (250, 50)
        self.space = 10
        self.key_font = pygame.font.SysFont('mannerliness', self.text_size)

        self.x_keys_from_1, self.y_keys_from_1 = 122, 550
        self.x_keys_from_Q, self.y_keys_from_Q = 122, 605
        self.x_keys_from_A, self.y_keys_from_A = 152, 660
        self.x_keys_from_Z, self.y_keys_from_Z = 182, 715
        self.x_key_space, self.y_key_space = 325, 770

        self.keys_from_1 = (
            Key('1'), Key('2'), Key('3'), Key('4'), Key('5'), Key('6'), Key('7'), Key('8'), Key('9'), Key('0'),
            Key('-'))
        self.keys_from_Q = (
            Key('Q'), Key('W'), Key('E'), Key('R'), Key('T'), Key('Y'), Key('Y'), Key('U'), Key('I'), Key('O'),
            Key('P'))
        self.keys_from_A = (
            Key('A'), Key('S'), Key('D'), Key('F'), Key('G'), Key('H'), Key('J'), Key('K'), Key('L'), Key(';'))
        self.keys_from_Z = (Key('Z'), Key('X'), Key('C'), Key('V'), Key('B'), Key('N'), Key('M'), Key(','), Key('.'))
        self.key_space = (Key('space'),)

        self.keys = {'1': self.keys_from_1[0], '2': self.keys_from_1[1], '3': self.keys_from_1[2],
                     '4': self.keys_from_1[3], '5': self.keys_from_1[4], '6': self.keys_from_1[5],
                     '7': self.keys_from_1[6], '8': self.keys_from_1[7], '9': self.keys_from_1[8],
                     '0': self.keys_from_1[9], '-': self.keys_from_1[10], 'q': self.keys_from_Q[0],
                     'w': self.keys_from_Q[1], 'e': self.keys_from_Q[2], 'i': self.keys_from_Q[7],
                     'o': self.keys_from_Q[8], 'p': self.keys_from_Q[9], 'a': self.keys_from_A[0],
                     's': self.keys_from_A[1], 'd': self.keys_from_A[2], 'f': self.keys_from_A[3],
                     'g': self.keys_from_A[4], 'h': self.keys_from_A[5], 'j': self.keys_from_A[6],
                     'k': self.keys_from_A[7], 'l': self.keys_from_A[8], ';': self.keys_from_A[9],
                     'z': self.keys_from_Z[0], 'x': self.keys_from_Z[1], 'c': self.keys_from_Z[2],
                     'v': self.keys_from_Z[3], 'b': self.keys_from_Z[4], 'n': self.keys_from_Z[5],
                     'm': self.keys_from_Z[6], ',': self.keys_from_Z[7], '.': self.keys_from_Z[8],
                     ' ': self.key_space[0]}

    def white(self):
        keys = (self.keys_from_1, self.keys_from_Q, self.keys_from_A, self.keys_from_Z, self.key_space)
        for line in keys:
            for key in line:
                if key.color != 'white' and time.time() - key.time > 0.12:
                    key.color = 'white'

    def blit(self):
        tuple_of_lines = (KeyboardLine(self.x_keys_from_1, self.y_keys_from_1, self.keys_from_1, self.key_size),
                          KeyboardLine(self.x_keys_from_Q, self.y_keys_from_Q, self.keys_from_Q, self.key_size),
                          KeyboardLine(self.x_keys_from_A, self.y_keys_from_A, self.keys_from_A, self.key_size),
                          KeyboardLine(self.x_keys_from_Z, self.y_keys_from_Z, self.keys_from_Z, self.key_size),
                          KeyboardLine(self.x_key_space, self.y_key_space, self.key_space, self.key_space_size))

        for line in tuple_of_lines:
            x = line.x
            y = line.y
            for key in line.keys:
                key_letter = self.key_font.render(key.letter, True, 'black')
                key_xy = key_letter.get_rect(center=(x + line.size[0] // 2, y + line.size[1] // 2))
                pg.draw.rect(self.screen, key.color, (x, y, line.size[0], line.size[1]))
                pg.draw.rect(self.screen, 'black', (x, y, line.size[0], line.size[1]), 3)
                self.screen.blit(key_letter, key_xy)
                x += (line.size[0] + self.space)

    def statistic(self):
        keys = (self.keys_from_1, self.keys_from_Q, self.keys_from_A, self.keys_from_Z, self.key_space)

        for line in keys:
            for key in line:
                if key.mistakes + key.proper_use <= 3:
                    key.color = 'white'
                else:
                    red_num = round(255 * key.mistakes / (key.mistakes + key.proper_use))
                    key.color = (red_num, 255 - red_num, 0)
