import pygame


class Key:
    def __init__(self, let, col='white'):
        self.letter = let
        self.color = col


class Keyboard:
    def __init__(self):
        self.text_size = 20
        self.width = 40
        self.length = 40
        self.space = 10

        self.x_keys_from_1, self.y_keys_from_1 = 177, 600
        self.x_keys_from_Q, self.y_keys_from_Q = 177, 650
        self.x_keys_from_A, self.y_keys_from_A = 202, 700
        self.x_keys_from_Z, self.y_keys_from_Z = 227, 750
        self.x_key_space, self.y_key_space = 325, 800

        self.keys_from_1 = (
            Key('1'), Key('2'), Key('3'), Key('4'), Key('5'), Key('6'), Key('7'), Key('8'), Key('9'), Key('0'),
            Key('-'))
        self.keys_from_Q = (
            Key('Q'), Key('W'), Key('E'), Key('R'), Key('T'), Key('Y'), Key('Y'), Key('U'), Key('I'), Key('O'),
            Key('P'))
        self.keys_from_A = (
            Key('A'), Key('S'), Key('D'), Key('F'), Key('G'), Key('H'), Key('J'), Key('K'), Key('L'), Key(';'))
        self.keys_from_Z = (Key('Z'), Key('X'), Key('C'), Key('V'), Key('B'), Key('N'), Key('M'), Key(','), Key('.'))
        self.key_space = Key('space')

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
                     pygame.K_SPACE: self.key_space}

    def white(self):
        for i in self.keys_from_1:
            i.color = 'white'
        for i in self.keys_from_Q:
            i.color = 'white'
        for i in self.keys_from_A:
            i.color = 'white'
        for i in self.keys_from_Z:
            i.color = 'white'
        self.key_space.color = 'white'
