import pygame as pg
import time
from src.consts_and_paths import *
from src.Keyboard import Key, Keyboard
from src.Bottom import Bottom
from src.RequiredText import RequiredText, Joke, Wiki


class Game:
    def __init__(self):
        pg.init()
        pygame.display.set_caption('Keyboard Trainer')  # show in screen caption
        pygame.display.set_icon(icon_image)  # show in screen caption
        self.clock = pg.time.Clock()
        self.size_of_screen = size_of_screen
        self.screen = pygame.display.set_mode(self.size_of_screen)  # display screen (900x900)
        self.background = pygame.transform.scale(background_image,
                                                 self.size_of_screen)  # scale background image to fit screen

        self.bottom_start = Bottom(size_of_bottom_start, start_image, 'red', coord_of_bottom_start)
        self.bottom_statistic = Bottom(size_of_bottom_statistic, statistic_image, 'red', coord_of_bottom_statistic)
        self.bottom_joke = Bottom(size_of_joke_bottom, joke_image, 'green', coord_of_joke_bottom)
        self.bottom_wiki = Bottom(size_of_wiki_bottom, wiki_image, 'red', coord_of_wiki_bottom)

        self.header = header
        self.result = result
        self.last_result = last_result
        self.finish = finish
        self.users_text = users_input
        self.required_text = Joke()

        self.time_start = 0  # will fix the start of time after the start.
        self.total_time = 0  # total time during after typing.
        self.res = 'Time:0   Accuracy:0 %    WpM:0'  # result of typing.
        self.game_over = True  # will fix end of game.
        self.len_rect = 10  # the length of the rectangle where the text is inputted.
        self.rect_color = 'red'  # color of this rectangle.
        self.count = 0

        self.keyboard = Keyboard(self.screen)

    def count_result(self, cost):
        """
        This function counts and check total time, accuracy
         and wpm while typing
        """
        accuracy = 0
        wpm = 0
        percent = 100
        minute = 60
        count = 0
        average_word = 5
        if not self.game_over:
            # calculate time
            self.total_time = time.time() - self.time_start
            # calculate accuracy
            for i in range(len(self.required_text.output_text)):
                try:
                    if self.users_text.output_text[i] != self.required_text.output_text[i]:
                        cost += 1
                        self.users_text.update(self.users_text.output_text[:-1])
                    if self.users_text.output_text[i] == self.required_text.output_text[i]:
                        count += 1
                except:
                    pass
            try:
                accuracy = (count / ((len(self.users_text.output_text)) + cost)) * percent
                # calculate wpm (words per minutes)
                wpm = len(self.users_text.output_text) * minute / (average_word * self.total_time)
            except:
                pass
            # 'Time:1   Accuracy:100 %    Wpm:1'
            self.res = 'Time:' + str(round(self.total_time)) + \
                       " secs   Accuracy:" + str(round(accuracy)) + "%" + \
                       '   WpM: ' + str(round(wpm))
        self.result.update(self.res)
        f = open('./statics.txt')
        self.last_result.update('Your Last ' + str(f.readlines()[-1]))

    def testing(self):
        """
        This function is the main one (run the code).
        Responsible for typing, the "start" and "exit" buttons.
        """
        play = True
        active = False
        max_len_rect, change_len_rect, max_len_text = 440, 5, 90  # max len of rect and text during input
        time_tick = 60
        help_text = ''
        count = 0
        while play:
            f = open('./statics.txt', 'a')
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    play = False
                # mouse button for reStart
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()
                    if self.bottom_start.rect.collidepoint(mouse):
                        self.rect_color = 'green'
                        self.bottom_start.color = 'green'
                        self.bottom_statistic.color = 'red'

                        self.required_text.get_text()
                        self.users_text.update('')
                        active = True
                        self.game_over = False
                        self.time_start = time.time()

                        self.len_rect = 10
                        count = 0

                    elif self.bottom_statistic.rect.collidepoint(mouse):
                        self.enter_start(f)
                        self.required_text.update('')
                        self.bottom_statistic.color = 'green'
                        self.keyboard.statistic()
                    elif self.bottom_joke.rect.collidepoint(mouse):
                        self.bottom_joke.color = 'green'
                        self.bottom_wiki.color = 'red'
                        self.enter_start(f)
                        self.required_text = Joke()
                    elif self.bottom_wiki.rect.collidepoint(mouse):
                        self.bottom_wiki.color = 'green'
                        self.bottom_joke.color = 'red'
                        self.enter_start(f)
                        self.required_text = Wiki()

                # KEYDOWN for word processing
                elif event.type == pg.KEYDOWN and active:
                    if event.key == pg.K_RETURN:
                        self.enter_start(f)
                        self.required_text.update('Are you ready?')
                        if self.bottom_statistic.color == 'green':
                            self.keyboard.white()
                            self.bottom_statistic.color = 'red'
                    elif event.key == pg.K_BACKSPACE:
                        count += 1
                        self.users_text.update(self.users_text.output_text[:-1])

                        if len(self.users_text.output_text) < max_len_text - 10:
                            self.len_rect -= change_len_rect
                    elif self.bottom_start.color == 'green':
                        if event.unicode == self.required_text.output_text[len(self.users_text.output_text)]:
                            if self.len_rect < max_len_rect:
                                self.len_rect += change_len_rect
                            if str(event.unicode).lower() in self.keyboard.keys:
                                self.keyboard.keys[str(event.unicode).lower()].color = 'green'
                                self.keyboard.keys[str(event.unicode).lower()].time = time.time()
                                self.keyboard.keys[str(event.unicode).lower()].proper_use += 1

                            self.users_text.update(self.users_text.output_text + event.unicode)
                        else:
                            count += 1

                            if str(event.unicode).lower() in self.keyboard.keys:
                                self.keyboard.keys[str(event.unicode).lower()].color = 'red'
                                self.keyboard.keys[str(event.unicode).lower()].time = time.time()
                                self.keyboard.keys[str(event.unicode).lower()].mistakes += 1

                    if len(self.users_text.output_text) == len(
                            self.required_text.output_text) and self.bottom_start.color == 'green':
                        f.write('\n' + '\n' + 'Main Text: ' + self.required_text.output_text + '\n')
                        f.write('Your Text: ' + self.users_text.output_text + '\n')
                        f.write('Result: ' + self.res)
                        self.required_text.get_text()
                        self.users_text.update('')
                        self.len_rect = 10
                        count = 0
                        print(' ' + self.users_text.output_text)
                        print(self.res + '\n')
                        self.time_start = time.time()

            self.count_result(count)
            self.display()
            pg.display.update()
            self.clock.tick(time_tick)

    def enter_start(self, f):
        self.bottom_start.color = 'red'
        self.rect_color = 'red'
        f.write('\n' + '\n' + 'Main Text: ' + self.required_text.output_text + '\n')
        f.write('Your Text: ' + self.users_text.output_text + '\n')
        f.write('Result: ' + self.res)
        active = False
        self.game_over = True
        count = 0
        # saved result on console
        print(' ' + self.users_text.output_text)
        print(self.res + '\n')
        self.users_text.update('')

    def display(self):
        """
            This function displays widgets in a screen.
        """
        rect = max(self.len_rect, 150)  # here 150 - initial length of rect
        rect_size = (self.size_of_screen[0] // 2 - rect, 160, 2 * rect, 50)  # size increases as you enter text
        # background
        self.screen.blit(self.background, (0, 0))

        # rect for input text
        pg.draw.rect(self.screen, 'black', rect_size)
        pg.draw.rect(self.screen, self.rect_color, rect_size, 3)

        # start button
        self.bottom_start.blit(self.screen)
        # statistic button
        self.bottom_statistic.blit(self.screen)
        # joke button
        self.bottom_joke.blit(self.screen)
        # wiki button
        self.bottom_wiki.blit(self.screen)

        # header text
        self.header.blit(self.screen)
        # output text (random text, joke)
        self.required_text.blit(self.screen)
        # input text
        self.users_text.blit(self.screen)
        # result text
        self.result.blit(self.screen)
        self.last_result.blit(self.screen)
        # finish rext
        self.finish.blit(self.screen)

        self.keyboard.blit()
        if self.bottom_statistic.color != 'green':
            self.keyboard.white()


game = Game()
