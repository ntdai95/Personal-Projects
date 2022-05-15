# The program uses third-party musics and icons, which are credited to:

# http://opengameart.org/users/copyc4t http://www.freesound.org/people/copyc4t/ https://soundcloud.com/copyc4t
# <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# <div>Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# <div>Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# <div>Icons made by <a href="https://www.flaticon.com/authors/ultimatearm" title="ultimatearm">ultimatearm</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

# The creator of the following program does not own any of the icons used below. All of the copyrights of the icons below belongs to the 
# creators mentioned above.


import sys
from os import path
import pygame as pg
import pickle
from settings import *
from sprites import *


class PickleHighScore:
    def __init__(self, list_of_highscores):
        self.list_of_highscores = list_of_highscores


    def saving_highscore_pickle(self):
        with open(".highscores.pickle", "wb") as p:
            pickle.dump(self.list_of_highscores, p)


class Main:
    def __init__(self):
        pg.init()
        pg.mixer.music.load(path.join(path.join(path.dirname(__file__), "Music"), "background_music.wav"))
        pg.mixer.music.set_volume(0.4)
        self.hit_sound = pg.mixer.Sound(path.join(path.join(path.dirname(__file__), "Music"), "hit.wav"))
        self.arrow_sound = pg.mixer.Sound(path.join(path.join(path.dirname(__file__), "Music"), "arrow.wav"))
        self.game_over_sound = pg.mixer.Sound(path.join(path.join(path.dirname(__file__), "Music"), "game_over.wav"))
        self.game_win_sound = pg.mixer.Sound(path.join(path.join(path.dirname(__file__), "Music"), "game_win.wav"))
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.first_last_background = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "first_last_background.png")).convert()
        self.main_game_background = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "background.png")).convert()
        pg.display.set_caption(TITLE)
        self.icon = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "horse_icon.png")).convert()
        self.icon.set_colorkey(BLACK)
        pg.display.set_icon(self.icon)
        self.clock = pg.time.Clock()
        self.reset()


    def reset(self):
        self.game_open = True
        self.instruction_page = False
        self.highscores_page = False
        self.game_running = False
        self.game_ending_lose = False
        self.game_ending_win = False
        self.list_of_button_texts = ["START GAME", "INSTRUCTIONS", "HIGHSCORES", "MUSIC ON/OFF", "SOUND ON/OFF", "EXIT GAME"]
        self.list_of_button_positions_x = None
        self.list_of_button_positions_y = None
        self.buttons_size_x = None
        self.buttons_size_y = None
        self.mouse_position = None
        self.round_count = -1
        self.list_of_highscores = []
        self.final_player_score_in_highscores = None
        self.player_name = ""
        self.is_music_playing = True
        self.is_sound_playing = True


### GAME START SCREEN ###


    def game_start_screen(self):
        pg.mixer.music.play(-1)
        while self.game_open:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_open = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(6):
                        if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                            self.game_running = True
                        elif i == 1 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.instruction_page = True
                        elif i == 2 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.highscores_page = True
                        elif i == 3 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            if self.is_music_playing:
                                pg.mixer.music.stop()
                                self.is_music_playing = False
                            else:
                                pg.mixer.music.play(-1)
                                self.is_music_playing = True
                        elif i == 4 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            if self.is_sound_playing:
                                self.is_sound_playing = False
                            else:
                                self.is_sound_playing = True
                        elif i == 5 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_open = False

            self.instructions_screen_page()
            self.highscores_screen()
            self.run_main_game()
            if self.game_open:
                self.screen.blit(self.first_last_background, (0, 0))
                self.initial_message_to_screen(self.screen)
                self.loading_buttons_on_first_page(self.screen, self.mouse_position, self.list_of_button_texts)

            pg.display.update()
            self.clock.tick(FPS)

        pg.quit()
        sys.exit()

    def initial_message_to_screen(self, screen):
        line_font = pg.font.Font('freesansbold.ttf', 60)
        line = line_font.render("Welcome to Horse Racer!", True, YELLOW)
        line_surface = pg.Surface(line.get_size())
        line_surface.fill(BLACK)
        line_surface.blit(line, (0, 0))
        self.screen.blit(line_surface, (400, 150))

    def loading_buttons_on_first_page(self, screen, mouse_position, list_of_button_texts):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_positions_x = [100, 575, 1050, 100, 575, 1050]
        self.list_of_button_positions_y = [350, 350, 350, 550, 550, 550]
        self.buttons_size_x = 350
        self.buttons_size_y = 100

        # Button Texts
        for i in range(6):
            if self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                pg.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)
            else: 
                pg.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)

            font = pg.font.Font('freesansbold.ttf', 40)
            text_font = font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()
            self.screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y - text_font_height) // 2))


### HIGHSCORES PAGE ###


    def highscores_screen(self):
        try:
            with open(".highscores.pickle", "rb") as p:
                pickle_objects = pickle.load(p)
            self.list_of_highscores = pickle_objects
            self.list_of_highscores.sort(reverse = True, key = lambda x: x[1])
        except EOFError:
            self.list_of_highscores = []

        while self.highscores_page:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.highscores_page = False
                    self.game_open = False
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(4):
                        if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.list_of_highscores = []
                            instance_of_PickleHighScore = PickleHighScore(self.list_of_highscores)
                            instance_of_PickleHighScore.saving_highscore_pickle()
                        elif i == 2 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.highscores_page = False

            self.screen.blit(self.first_last_background, (0, 0))
            self.highscores_message_to_screen(self.screen)
            self.loading_buttons_on_highscores_page(self.screen, self.mouse_position, self.list_of_button_texts, self.buttons_size_x, self.buttons_size_y)

            if self.highscores_page == False and self.game_open:
                self.reset()

            pg.display.update()
            self.clock.tick(FPS)

    def highscores_message_to_screen(self, screen):
        first_line_font = pg.font.Font('freesansbold.ttf', 60)
        line_font = pg.font.Font('freesansbold.ttf', 40)
        list_of_messages = ["TOP 10 HIGHSCORES!"]
        for index, name_score in enumerate(self.list_of_highscores):
            name_score_message = f"{index + 1}. {name_score[0]} --> {name_score[1]} points"
            list_of_messages.append(name_score_message)
        for index, message in enumerate(list_of_messages):
            if index == 0:
                line = first_line_font.render(message, True, BLACK)
            else:
                line = line_font.render(message, True, BLACK)
            line_surface = pg.Surface(line.get_size())
            line_surface.fill(PINK)
            line_surface.blit(line, (0, 0))
            if index == 0:
                self.screen.blit(line_surface, (470, 20))
            elif index < 6:
                self.screen.blit(line_surface, (60, 60 + 100 * index))  
            else:
                self.screen.blit(line_surface, (800, 60 + 100 * (index - 5)))

    def loading_buttons_on_highscores_page(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_texts = ["DELETE", "ALL SCORES", "MAIN", "PAGE"]
        self.list_of_button_positions_x = [450, 450, 750, 750]
        self.list_of_button_positions_y = [665, 705, 665, 705]
        self.buttons_size_x = 290
        self.buttons_size_y = 110

        # Button Texts
        for i in range(4):
            if i % 2 == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                pg.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)
            elif i % 2 == 0: 
                pg.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)

            font = pg.font.Font('freesansbold.ttf', 40)
            text_font = font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()
            self.screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y - text_font_height) // 4))


### INSTRUCTIONS PAGE ###


    def instructions_screen_page(self):
        while self.instruction_page:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.instruction_page = False
                    self.game_open = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(2):
                        if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.instruction_page = False

            self.screen.blit(self.first_last_background, (0, 0))
            self.instruction_message_to_screen(self.screen)
            self.loading_buttons_on_instruction_page(self.screen, self.mouse_position, self.list_of_button_texts, self.buttons_size_x, self.buttons_size_y)

            if self.instruction_page == False and self.game_open:
                self.reset()

            pg.display.update()
            self.clock.tick(FPS)
    
    def instruction_message_to_screen(self, screen):
        first_line_font = pg.font.Font('freesansbold.ttf', 50)
        line_font = pg.font.Font('freesansbold.ttf', 30)
        list_of_messages = ["Instructions!",
        "To move around, you can use the up, left, and right arrows. Note that you can only move around",
        "when you are on the ground. To shoot down enemies, press space. You can only shoot more arrows",
        "if the previous arrow has already hit an enemy or has disappeared from the screen.",
        "You can only shoot down bats, dragons, and the octopus (at the end). Each bat needs to be shoot",
        "down once. Each dragon and the octopus (at the end) need to be shoot down five times. The number",
        "of lives remaining for each dragon and the octopus (at the end) will be shown by the number of",
        "mini images on the right upper corner of the screen during the game when either of the dragons or",
        "the octopus appears.",
        "If you run out of lives (indicated by the number of mini images on the left upper corner of the",
        "screen during the game), you will lose the game. In order to win, you need to shoot down the octopus",
        "at the end. For scoring, you will get 1 point for every fired arrow that shoots down an enemy.",
        "You can only save your score if you win the game and your score is among the top 10 highscores."]
        for index, message in enumerate(list_of_messages):
            if index == 0:
                line = first_line_font.render(message, True, BLACK)
            else:
                line = line_font.render(message, True, BLACK)
            line_surface = pg.Surface(line.get_size())
            line_surface.fill(PINK)
            line_surface.blit(line, (0, 0))
            if index == 0:
                self.screen.blit(line_surface, (580, 20))
            elif index < 4:
                self.screen.blit(line_surface, (20, 100 + 30 * index))
            elif 4 <= index < 9:
                self.screen.blit(line_surface, (20, 140 + 30 * index))    
            else:
                self.screen.blit(line_surface, (20, 180 + 30 * index))

    def loading_buttons_on_instruction_page(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_texts = ["MAIN", "PAGE"]
        self.list_of_button_positions_x = [650, 650]
        self.list_of_button_positions_y = [665, 705]
        self.buttons_size_x = 170
        self.buttons_size_y = 110

        # Button Texts
        for i in range(2):
            if i % 2 == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                pg.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)
            elif i % 2 == 0: 
                pg.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)

            font = pg.font.Font('freesansbold.ttf', 40)
            text_font = font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()
            self.screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y - text_font_height) // 4))


### MAIN GAME SCREEN ###


    def loading_sprites_main_game(self, screen):
        self.all_sprites_group = pg.sprite.Group()
        self.player = Player()
        self.all_sprites_group.add(self.player)
        self.arrow = Arrow()
        self.all_sprites_group.add(self.arrow)
        self.fence = []
        for i in range(3):
            instance_of_Fence = Fence(i)
            self.fence.append(instance_of_Fence)
            self.all_sprites_group.add(instance_of_Fence)
        self.bat = []
        for i in range(2):
            instance_of_Bat = Bat(i)
            self.bat.append(instance_of_Bat)
            self.all_sprites_group.add(instance_of_Bat)
        self.dragon = Dragon()
        self.all_sprites_group.add(self.dragon)
        self.fire = Fire()
        self.all_sprites_group.add(self.fire)
        self.octopus = Octopus()
        self.all_sprites_group.add(self.octopus)
        self.waterdrop = []
        for i in range(4):
            instance_of_Waterdrop = Waterdrop(i)
            self.waterdrop.append(instance_of_Waterdrop)
            self.all_sprites_group.add(instance_of_Waterdrop)
        

    def run_main_game(self):
        self.loading_sprites_main_game(self.screen)
        while self.game_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_running = False
                    self.game_open = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.player.player_move_horizontal = "LEFT"
                    if event.key == pg.K_RIGHT:
                        self.player.player_move_horizontal = "RIGHT"
                    if event.key == pg.K_UP:
                        self.player.player_move_vertical = "UP"
                    if event.key == pg.K_SPACE:
                        if self.arrow.arrow_is_on == False:
                            self.arrow.arrow_is_on = True
                            self.arrow.rect.x = self.player.rect.x
                            self.arrow.rect.y = self.player.rect.y
        
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                        self.player.player_move_horizontal = None
                    if event.key == pg.K_UP:
                        self.player.player_move_vertical = None

            self.update_main_game(self.round_count)
            self.draw_main_game()

            if self.octopus.octopus_life_point < 1:
                self.game_ending_win = True
                self.game_win_sound.play()
                self.game_win_screen()

            if self.player.player_life_point < 1:
                self.game_ending_lose = True
                self.game_over_sound.play()
                self.game_lose_screen()

            pg.display.update()
            self.clock.tick(FPS)

    def update_main_game(self, round_count):
        if self.round_count != 2 and self.round_count != 8  and self.round_count != 12 and all(fence.rect.x <= -400 for fence in self.fence) and all(bat.rect.x <= -400 for bat in self.bat):
            self.round_count += 1
            for fence in self.fence:
                fence.fence_appear = True
            for bat in self.bat:
                bat.bat_appear = True
        elif self.round_count != 2 and self.round_count != 8 and self.round_count != 12:
            for fence in self.fence:
                fence.fence_appear = False
            for bat in self.bat:
                bat.bat_appear = False
        elif self.round_count == 12 and all(waterdrop.rect.y >= 800 for waterdrop in self.waterdrop):
            for waterdrop in self.waterdrop:
                waterdrop.waterdrop_appear = True
        elif self.round_count == 12:
            for waterdrop in self.waterdrop:
                waterdrop.waterdrop_appear = False
        
        self.collision_detection()
        if self.dragon.dragon_life_point == 0:
            self.round_count += 1
            self.dragon.dragon_life_point = 5

        self.all_sprites_group.update(self.round_count)

    def collision_detection(self):
        for bat in self.bat:
            if pg.sprite.collide_mask(self.player, bat):
                if self.is_sound_playing:
                    self.hit_sound.play()
                bat.rect.x = -1000
                bat.bat_appear = False
                self.player.player_life_point -= 1
        
        for fence in self.fence:
            if pg.sprite.collide_mask(self.player, fence):
                if self.is_sound_playing:
                    self.hit_sound.play()
                fence.rect.x = -1000
                fence.fence_appear = False
                self.player.player_life_point -= 1

        if pg.sprite.collide_mask(self.player, self.dragon):
            if self.is_sound_playing:
                self.hit_sound.play()
            self.player.rect.x = 100
            self.player.rect.y = 500
            self.player.player_life_point -= 1

        if pg.sprite.collide_mask(self.player, self.fire):
            if self.is_sound_playing:
                self.hit_sound.play()
            self.fire.rect.x = -1000
            self.player.player_life_point -= 1

        if pg.sprite.collide_mask(self.player, self.octopus):
            if self.is_sound_playing:
                self.hit_sound.play()
            self.player.rect.x = 100
            self.player.rect.y = 500
            self.player.player_life_point -= 1

        for waterdrop in self.waterdrop:
            if pg.sprite.collide_mask(self.player, waterdrop):
                if self.is_sound_playing:
                    self.hit_sound.play()
                waterdrop.rect.y = 1000
                waterdrop.waterdrop_appear = False
                self.player.player_life_point -= 1

        for bat in self.bat:
            if pg.sprite.collide_mask(self.arrow, bat):
                if self.is_sound_playing:
                    self.arrow_sound.play()
                self.arrow.arrow_is_on = False
                bat.rect.x = -1000
                bat.bat_appear = False
                self.player.player_score += 1

        if pg.sprite.collide_mask(self.arrow, self.dragon):
            if self.is_sound_playing:
                self.arrow_sound.play()
            self.arrow.arrow_is_on = False
            self.dragon.dragon_life_point -= 1
            self.player.player_score += 1

        if pg.sprite.collide_mask(self.arrow, self.octopus):
            if self.is_sound_playing:
                self.arrow_sound.play()
            self.arrow.arrow_is_on = False
            self.octopus.octopus_life_point -= 1
            self.player.player_score += 1

    def draw_main_game(self):
        self.screen.blit(self.main_game_background, (0, 0))
        self.message_to_main_game_screen(self.screen)
        self.player_lives_to_main_sreen (self.screen)
        if self.round_count == 2 or self.round_count == 8:
            self.dragon_lives_to_main_screen(self.screen)
        elif self.round_count == 12:
            self.octopus_lives_to_main_screen(self.screen)
        self.all_sprites_group.draw(self.screen)

    def message_to_main_game_screen(self, screen):
        line_font = pg.font.Font('freesansbold.ttf', 40)
        line = line_font.render(f"Score: {self.player.player_score}", True, YELLOW)
        line_surface = pg.Surface(line.get_size())
        line_surface.fill(BLACK)
        line_surface.blit(line, (0, 0))
        self.screen.blit(line_surface, (10, 80))

    def player_lives_to_main_sreen(self, screen):
        for i in range(self.player.player_life_point):
            player_mini_image_rect = self.player.mini_image.get_rect()
            player_mini_image_rect.x = 10 + 70 * i
            player_mini_image_rect.y = 10
            self.screen.blit(self.player.mini_image, player_mini_image_rect)

    def dragon_lives_to_main_screen(self, screen):
        for i in range(self.dragon.dragon_life_point):
            dragon_mini_image_rect = self.dragon.mini_image.get_rect()
            dragon_mini_image_rect.x = SCREEN_WIDTH - 80 - 70 * i
            dragon_mini_image_rect.y = 10
            self.screen.blit(self.dragon.mini_image, dragon_mini_image_rect)

    def octopus_lives_to_main_screen(self, screen):
        for i in range(self.octopus.octopus_life_point):
            octopus_mini_image_rect = self.octopus.mini_image.get_rect()
            octopus_mini_image_rect.x = SCREEN_WIDTH - 80 - 70 * i
            octopus_mini_image_rect.y = 10
            self.screen.blit(self.octopus.mini_image, octopus_mini_image_rect)


### GAME ENDING SCREENS ###


    def game_lose_screen(self):
        while self.game_ending_lose:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_running = False
                    self.game_open = False
                    self.game_ending_lose = False
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(4):
                        if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_ending_lose = False
                            self.game_running = False
                        elif i == 2 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_running = False
                            self.game_open = False
                            self.game_ending_lose = False

            self.draw_game_lose(self.screen)
            if self.game_open and self.game_ending_lose == False and self.game_running == False:
                self.reset()

            pg.display.update()
            self.clock.tick(FPS)


    def draw_game_lose(self, screen):
        self.screen.blit(self.first_last_background, (0, 0))
        self.message_to_screen_game_lose(self.screen)
        self.loading_buttons_on_game_lose_screen(self.screen, self.mouse_position, self.list_of_button_texts, self.buttons_size_x, self.buttons_size_y)


    def message_to_screen_game_lose(self, screen):
        line_font = pg.font.Font('freesansbold.ttf', 60)
        list_of_messages = ["GAME OVER!", f"Your score is {self.player.player_score} points.", "Try harder next time."]
        for index, message in enumerate(list_of_messages):
            line = line_font.render(message, True, YELLOW)
            line_surface = pg.Surface(line.get_size())
            line_surface.fill(BLACK)
            line_surface.blit(line, (0, 0))
            if index == 0:
                self.screen.blit(line_surface, (540, 20))
            elif index == 1:
                self.screen.blit(line_surface, (390, 250))
            else:
                self.screen.blit(line_surface, (440, 430))


    def loading_buttons_on_game_lose_screen(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_texts = ["MAIN", "PAGE", "EXIT", "GAME"]
        self.list_of_button_positions_x = [560, 560, 740, 740]
        self.list_of_button_positions_y = [665, 705, 665, 705]
        self.buttons_size_x = 170
        self.buttons_size_y = 110

        # Button Texts
        for i in range(4):
            if i % 2 == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                pg.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)
            elif i % 2 == 0: 
                pg.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)

            font = pg.font.Font('freesansbold.ttf', 40)
            text_font = font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()
            self.screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y - text_font_height) // 4))


    def game_win_screen(self):
        try:
            with open(".highscores.pickle", "rb") as p:
                pickle_objects = pickle.load(p)
            self.list_of_highscores = pickle_objects
            if len(self.list_of_highscores) < 10:
                self.final_player_score_in_highscores = True
            elif len(self.list_of_highscores) >= 10 and self.list_of_highscores[-1][1] < self.player.player_score:
                self.final_player_score_in_highscores = True
            else:
                self.final_player_score_in_highscores = False
        except EOFError:
            self.list_of_highscores = []
            self.final_player_score_in_highscores = True

        while self.game_ending_win:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_open = False
                    self.game_running = False
                    self.game_ending_win = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(6):
                        if i == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_running = False
                            self.game_ending_win = False
                        elif i == 2 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.game_open = False
                            self.game_running = False
                            self.game_ending_win = False
                        elif self.final_player_score_in_highscores != None and self.final_player_score_in_highscores and i == 4 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y:
                            self.list_of_highscores.append(tuple([self.player_name, self.player.player_score]))
                            self.list_of_highscores.sort(reverse = True, key = lambda x: x[1])
                            self.list_of_highscores = self.list_of_highscores[:10]
                            instance_of_PickleHighScore = PickleHighScore(self.list_of_highscores)
                            instance_of_PickleHighScore.saving_highscore_pickle()
                            self.final_player_score_in_highscores = None
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    elif len(self.player_name) < 10:
                        self.player_name += event.unicode

            self.draw_game_win(self.screen)
            if self.game_open and self.game_ending_win == False and self.game_running == False:
                self.reset()

            pg.display.update()
            self.clock.tick(FPS)


    def draw_game_win(self, screen):
        self.screen.blit(self.first_last_background, (0, 0))
        self.message_to_screen_game_win(self.screen)
        self.loading_buttons_on_game_win_screen(self.screen, self.mouse_position, self.list_of_button_texts, self.buttons_size_x, self.buttons_size_y)


    def message_to_screen_game_win(self, screen):
        first_line_font = pg.font.Font('freesansbold.ttf', 60)
        line_font = pg.font.Font('freesansbold.ttf', 50)
        list_of_messages = ["CONGRATULATIONS!", f"Your score is {self.player.player_score} points."]
        if self.final_player_score_in_highscores:
            list_of_messages.extend(["Your score is in the top 10 highscores.",
            "Type your name by pressing the alphabet letters", 
            "(max. 10 characters) to save your score.",
            f"{self.player_name}"])
        elif self.final_player_score_in_highscores == False:
            list_of_messages.extend(["Unfortunately, your score is not in the", 
            "top 10 highscores. Therefore, your score",
            "cannot be saved. Try harder next time."])
        elif self.final_player_score_in_highscores == None:
            list_of_messages.extend(["Your score has been saved!", "You can check it in the Highscores menu on the main page."])

        for index, message in enumerate(list_of_messages):
            if index == 0:
                line = first_line_font.render(message, True, YELLOW)
            elif self.final_player_score_in_highscores and index == 5:
                line = first_line_font.render(message, True, BLACK)
            else:
                line = line_font.render(message, True, YELLOW)
            line_surface = pg.Surface(line.get_size())
            if self.final_player_score_in_highscores and index == 5:
                line_surface.fill(PINK)
            else:
                line_surface.fill(BLACK)
            line_surface.blit(line, (0, 0))
            if index == 0:
                self.screen.blit(line_surface, (400, 20))
            elif index == 1:
                self.screen.blit(line_surface, (440, 160))
            elif self.final_player_score_in_highscores and index == 5:
                self.screen.blit(line_surface, (480, 540))
            else:
                self.screen.blit(line_surface, (20, 160 + index * 60))


    def loading_buttons_on_game_win_screen(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_texts = ["MAIN", "PAGE", "EXIT", "GAME"]
        self.list_of_button_positions_x = [560, 560, 740, 740]
        self.list_of_button_positions_y = [665, 705, 665, 705]
        self.buttons_size_x = 170
        self.buttons_size_y = 110

        if self.final_player_score_in_highscores:
            self.list_of_button_texts.extend(["SAVE", "SCORE"])
            self.list_of_button_positions_x.extend([1060, 1060])
            self.list_of_button_positions_y.extend([510, 550])
            # Button Texts
            for i in range(4, 6):
                if i % 2 == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                    pg.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                    pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)
                elif i % 2 == 0: 
                    pg.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                    pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)

                font = pg.font.Font('freesansbold.ttf', 40)
                text_font = font.render(self.list_of_button_texts[i], True, BLACK)
                text_font_width = text_font.get_width()
                text_font_height = text_font.get_height()
                self.screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y - text_font_height) // 4))

        # Button Texts
        for i in range(4):
            if i % 2 == 0 and self.list_of_button_positions_x[i] <= self.mouse_position[0] <= self.list_of_button_positions_x[i] + self.buttons_size_x and self.list_of_button_positions_y[i] <= self.mouse_position[1] <= self.list_of_button_positions_y[i] + self.buttons_size_y: 
                pg.draw.rect(self.screen, RED, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)
            elif i % 2 == 0: 
                pg.draw.rect(self.screen, GREEN, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y])
                pg.draw.rect(self.screen, BLACK, [self.list_of_button_positions_x[i], self.list_of_button_positions_y[i], self.buttons_size_x, self.buttons_size_y], 5)

            font = pg.font.Font('freesansbold.ttf', 40)
            text_font = font.render(self.list_of_button_texts[i], True, BLACK)
            text_font_width = text_font.get_width()
            text_font_height = text_font.get_height()
            self.screen.blit(text_font, (self.list_of_button_positions_x[i] + (self.buttons_size_x - text_font_width) // 2, self.list_of_button_positions_y[i] + (self.buttons_size_y - text_font_height) // 4))


if __name__ == '__main__':
    instance_of_Main = Main()
    instance_of_Main.game_start_screen()