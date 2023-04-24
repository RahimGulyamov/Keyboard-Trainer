import pygame as pg
import os


class Text:
    def __init__(self, text, center_coord, color, font, bg_color=None, bg_indent=None):
        self.font = font
        self.color = color
        self.bg_color = bg_color
        self.bg_indent = bg_indent
        self.center_coord = center_coord
        self.output_text = text
        self.text = self.font.render(self.output_text, True, self.color)
        self.text_bg = self.font.render(self.output_text, True, self.bg_color) if self.bg_color is not None else None
        self.rect = self.text.get_rect(center=self.center_coord)
        self.rect_bg = self.text_bg.get_rect(center=(self.center_coord[0] + self.bg_indent, self.center_coord[
            1] + self.bg_indent)) if self.bg_indent is not None else None

    def blit(self, screen):
        if self.text_bg is not None:
            screen.blit(self.text_bg, self.rect_bg)

        screen.blit(self.text, self.rect)

    def update(self, new_text):
        self.output_text = new_text
        self.text = self.font.render(self.output_text, True, self.color)
        self.text_bg = self.font.render(self.output_text, True, self.bg_color) if self.bg_color is not None else None
        self.rect = self.text.get_rect(center=self.center_coord)
        self.rect_bg = self.text_bg.get_rect(center=(self.center_coord[0] + self.bg_indent, self.center_coord[
            1] + self.bg_indent)) if self.bg_indent is not None else None
