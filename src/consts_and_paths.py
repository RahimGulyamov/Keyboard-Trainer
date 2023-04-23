import pygame
from src.class_Text import Text

pygame.init()

path_to_background_image = './images/background_keyboard.jpg'  # background image
path_to_icon_image = './images/icon.png'  # icon image
path_to_start_bottom = './images/start.png'  # start button image
path_to_statistic_bottom = './images/statistic.png'  # statistic bottom image
path_to_joke_bottom = './images/joke.png'  # joke bottom image
path_to_wiki_bottom = './images/wiki.png'  # wiki bottom image

background_image = pygame.image.load(path_to_background_image)  # loading bg image into "bg" parameter
icon_image = pygame.image.load(path_to_icon_image)  # loading icon image into "icon" param.
start_image = pygame.image.load(path_to_start_bottom)  # loading start button img into "start" param.
statistic_image = pygame.image.load(path_to_statistic_bottom)
joke_image = pygame.image.load(path_to_joke_bottom)
wiki_image = pygame.image.load(path_to_wiki_bottom)

size_of_bottom_start = (200, 64)
coord_of_bottom_start = (225, 400)

size_of_bottom_statistic = (200, 64)
coord_of_bottom_statistic = (475, 400)

size_of_joke_bottom = (100, 32)
coord_of_joke_bottom = (750, 230)

size_of_wiki_bottom = (100, 32)
coord_of_wiki_bottom = (750, 280)

size_of_screen = (900, 900)

text_size = 20  # the size of text, which inputting.

header_size = 60
header_font = pygame.font.Font('./fonts/BrunoAceSC-Regular.ttf', header_size)
header_text = 'KEYBOARD TRAINER'
header_coord = (size_of_screen[0] // 2, 50)
header_color = 'white'
header_bg_color = 'black'
header_indent = 4
header = Text(text=header_text, center_coord=header_coord, color=header_color, font=header_font,
              bg_color=header_bg_color, bg_indent=header_indent)

result_size = 30
result_font = pygame.font.Font('./fonts/Ysabeau-Medium.ttf', result_size)
result_text = 'Time:0   Accuracy:0 %    WpM:0'
result_coord = (size_of_screen[0] // 2, 310)
result_color = 'green'
result_bg_color = 'black'
result_indent = 1
result = Text(text=result_text, center_coord=result_coord, color=result_color, font=result_font,
              bg_color=result_bg_color, bg_indent=result_indent)

last_res_size = 20
last_res_font = pygame.font.Font('./fonts/Ysabeau-Medium.ttf', last_res_size)
last_res_text = 'Your Last Result: Time:0   Accuracy:0 %    WpM:0'
last_res_coord = (size_of_screen[0] // 2, 350)
last_res_color = 'Yellow'
last_result = Text(text=last_res_text, center_coord=last_res_coord, color=last_res_color,
                   font=last_res_font)

finish_size = 15
finish_font = pygame.font.Font('./fonts/Ysabeau-Medium.ttf', finish_size)
finish_text = 'Press ENTER for finish!'
finish_coord = (size_of_screen[0] // 2, 500)
finish_color = 'white'
finish = Text(text=finish_text, center_coord=finish_coord, color=finish_color, font=finish_font)

input_font = pygame.font.Font('./fonts/Ysabeau-Medium.ttf', text_size)
input_text = ''
input_coord = (size_of_screen[0] // 2, 185)
input_color = 'white'
users_input = Text(text=input_text, center_coord=input_coord, color=input_color, font=input_font)
