# The program uses third-party icons, which are credited to:

# Icons made by <a href="https://www.flaticon.com/authors/creaticca-creative-agency" title="Creaticca Creative Agency">Creaticca Creative Agency</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/free-icon/airplane_2646745?related_item_id=2646727&term=airplane%20military" title="ultimatearm">ultimatearm</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/free-icon/missile_2809728?related_item_id=2762183&term=missile" title="smalllikeart">smalllikeart</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/nhor-phai" title="Nhor Phai">Nhor Phai</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/smalllikeart" title="smalllikeart">smalllikeart</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

# The creator of the following program does not own any of the icons used below. All of the copyrights of the icons below belongs to the 
# creators mentioned above.


import sys
from os import path
import pygame as pg
import random
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
        pg.mixer.music.set_volume(0.2)
        self.hit_sound = pg.mixer.Sound(path.join(path.join(path.dirname(__file__), "Music"), "hit.wav"))
        self.explosion_sound = pg.mixer.Sound(path.join(path.join(path.dirname(__file__), "Music"), "bullet.wav"))
        self.game_over_sound = pg.mixer.Sound(path.join(path.join(path.dirname(__file__), "Music"), "game_over.wav"))
        self.game_win_sound = pg.mixer.Sound(path.join(path.join(path.dirname(__file__), "Music"), "game_win.wav"))
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.first_last_background = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "first_last_background.png")).convert()
        self.main_game_background = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "background.png")).convert()
        pg.display.set_caption(TITLE)
        self.icon = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "tank_icon.png")).convert()
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
        self.round_count = 0
        self.list_of_highscores = []
        self.final_player_score_in_highscores = None
        self.player_name = ""
        self.is_music_playing = True
        self.is_sound_playing = True


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
        line = line_font.render("Welcome to Tank Racer!", True, BLUE)
        line_surface = pg.Surface(line.get_size())
        line_surface.fill(WHITE)
        line_surface.blit(line, (0, 0))
        self.screen.blit(line_surface, (150, 100))


    def loading_buttons_on_first_page(self, screen, mouse_position, list_of_button_texts):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_positions_x = [100, 550, 100, 100, 550, 550]
        self.list_of_button_positions_y = [300, 300, 600, 450, 450, 600]
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
        first_line_font = pg.font.Font('freesansbold.ttf', 50)
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
            if index % 2 == 0:
                line_surface.fill(PINK)
            else:
                line_surface.fill(YELLOW)
            line_surface.blit(line, (0, 0))
            if index == 0:
                self.screen.blit(line_surface, (240, 20))
            else:
                self.screen.blit(line_surface, (180, 60 + 50 * index))


    def loading_buttons_on_highscores_page(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_texts = ["DELETE", "ALL SCORES", "MAIN", "PAGE"]
        self.list_of_button_positions_x = [210, 210, 510, 510]
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
        "To move around, you can use the up, down, left, and right arrows.",
        "To shoot down enemies, press space. You can only shoot more",
        "bullets if the previous bullet has already hit an enemy or has",
        "disappeared from the screen. You can only shoot down airplanes",
        "or headquarters (at the end). Each airplane needs to be shoot",
        "down once. Each headquarter needs to be shoot down twice.",
        "The number of lives remaining for each headquarter will be",
        "shown by the length of health bars above each of them.",
        "If you run out of lives (indicated by the length of health bar on",
        "the left upper corner of the screen during the game), you will lose",
        "the game. In order to win, you need to shoot down all headquarters",
        "at the end. You can only save your score if you win the game and",
        "your score is among the top 10 highscores."]
        for index, message in enumerate(list_of_messages):
            if index == 0:
                line = first_line_font.render(message, True, BLACK)
            else:
                line = line_font.render(message, True, BLACK)
            line_surface = pg.Surface(line.get_size())
            line_surface.fill(PINK)
            line_surface.blit(line, (0, 0))
            if index == 0:
                self.screen.blit(line_surface, (350, 20))
            elif index < 4:
                self.screen.blit(line_surface, (20, 100 + 30 * index))
            elif 4 <= index < 9:
                self.screen.blit(line_surface, (20, 140 + 30 * index))    
            else:
                self.screen.blit(line_surface, (20, 180 + 30 * index))


    def loading_buttons_on_instruction_page(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_texts = ["MAIN", "PAGE"]
        self.list_of_button_positions_x = [420, 420]
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
        self.bullet = Bullet()
        self.all_sprites_group.add(self.bullet)
        self.landmine = []
        for i in range(6):
            instance_of_Landmine = Landmine(i)
            self.landmine.append(instance_of_Landmine)
            self.all_sprites_group.add(instance_of_Landmine)
        self.medal = []
        for i in range(2):
            instance_of_Medal = Medal(i)
            self.medal.append(instance_of_Medal)
            self.all_sprites_group.add(instance_of_Medal)
        self.airplane = []
        for i in range(2):
            instance_of_Airplane = Airplane(i)
            self.airplane.append(instance_of_Airplane)
            self.all_sprites_group.add(instance_of_Airplane)
        self.bomb = []
        for i in range(2):
            instance_of_Bomb = Bomb(i)
            self.bomb.append(instance_of_Bomb)
            self.all_sprites_group.add(instance_of_Bomb)
        self.headquarter = []
        for i in range(4):
            instance_of_Headquarter = Headquarter(i)
            self.headquarter.append(instance_of_Headquarter)
            self.all_sprites_group.add(instance_of_Headquarter)
        self.rocket = Rocket()
        self.all_sprites_group.add(self.rocket)


    def run_main_game(self):
        self.loading_sprites_main_game(self.screen)
        while self.game_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_running = False
                    self.game_open = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.player.player_move = "LEFT"
                    if event.key == pg.K_RIGHT:
                        self.player.player_move = "RIGHT"
                    if event.key == pg.K_UP:
                        self.player.player_move = "UP"
                    if event.key == pg.K_DOWN:
                        self.player.player_move = "DOWN"
                    if event.key == pg.K_SPACE:
                        if self.bullet.bullet_is_on == False:
                            self.bullet.bullet_is_on = True
                            self.bullet.rect.x = self.player.rect.x
                            self.bullet.rect.y = self.player.rect.y
        
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN:
                        self.player.player_move = None

            self.update_main_game(self.round_count)
            self.draw_main_game()

            if all(headquarter.headquarter_life_point == 0 for headquarter in self.headquarter):
                self.player.player_score += self.player.player_life_point * 15
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
        if self.round_count != 4 and self.round_count != 8  and self.round_count != 12:
            for medal in self.medal:
                if medal.rect.y == 800:
                    self.round_count += 1
        elif self.round_count == 4 and all(airplane.rect.x == -1000 and airplane.rect.y == -1000 for airplane in self.airplane):
            for airplane in self.airplane:
                airplane.airplane_life_point = 1
            self.round_count += 1
        elif self.round_count == 8 and all(airplane.rect.x == -1000 and airplane.rect.y == -1000 for airplane in self.airplane):
            for airplane in self.airplane:
                airplane.airplane_life_point = 1
            self.round_count += 1
        
        self.collision_detection()
        self.all_sprites_group.update(self.round_count)


    def collision_detection(self):
        for landmine in self.landmine:
            if pg.sprite.collide_mask(self.player, landmine):
                if self.is_sound_playing:
                    self.hit_sound.play()
                landmine.rect.x -= 1000
                self.player.player_life_point -= 1
                self.player.rect.x = random.choice([200, 350, 500, 650])
                self.player.rect.y = 630
        
        for medal in self.medal:
            if pg.sprite.collide_mask(self.player, medal):
                self.player.player_score += 1

        for airplane in self.airplane:
            if pg.sprite.collide_mask(self.player, airplane):
                if self.is_sound_playing:
                    self.hit_sound.play()
                self.player.player_life_point -= 1
                self.player.rect.x = random.choice([200, 350, 500, 650])
                self.player.rect.y = 630

        for bomb in self.bomb:
            if pg.sprite.collide_mask(self.player, bomb):
                if self.is_sound_playing:
                    self.hit_sound.play()
                bomb.rect.x -= 1000
                self.player.player_life_point -= 1
                self.player.rect.x = random.choice([200, 350, 500, 650])
                self.player.rect.y = 630

        for headquarter in self.headquarter:
            if pg.sprite.collide_mask(self.player, headquarter):
                if self.is_sound_playing:
                    self.hit_sound.play()
                self.player.player_life_point -= 1
                self.player.rect.x = random.choice([200, 350, 500, 650])
                self.player.rect.y = 630

        if pg.sprite.collide_mask(self.player, self.rocket):
            if self.is_sound_playing:
                self.hit_sound.play()
            self.rocket.rect.x = -1000
            self.rocket.rect.y = -1000
            self.player.player_life_point -= 1
            self.player.rect.x = random.choice([200, 350, 500, 650])
            self.player.rect.y = 630

        for airplane in self.airplane:
            if pg.sprite.collide_mask(self.bullet, airplane):
                if self.is_sound_playing:
                    self.explosion_sound.play()
                self.bullet.bullet_is_on = False
                self.player.player_score += 10
                airplane.airplane_life_point -= 1

        for headquarter in self.headquarter:
            if pg.sprite.collide_mask(self.bullet, headquarter):
                if self.is_sound_playing:
                    self.explosion_sound.play()
                self.bullet.bullet_is_on = False
                self.player.player_score += 5
                headquarter.headquarter_life_point -= 1


    def draw_main_game(self):
        self.screen.blit(self.main_game_background, (0, 0))
        self.message_to_main_game_screen(self.screen)
        self.all_sprites_group.draw(self.screen)


    def message_to_main_game_screen(self, screen):
        line_font = pg.font.Font('freesansbold.ttf', 40)
        list_of_messages = ["Health:", "Score:", f"{self.player.player_score}"]
        for i, message in enumerate(list_of_messages):
            line = line_font.render(message, True, YELLOW)
            line_surface = pg.Surface(line.get_size())
            line_surface.fill(BLACK)
            line_surface.blit(line, (0, 0))
            if i == 0:
                self.screen.blit(line_surface, (10, 10))
            else:
                self.screen.blit(line_surface, (820 + i * 30, -40 + i * 50))

        self.draw_health_bar_player(self.screen)
        if self.round_count == 12:
            self.draw_health_bar_headquarter(self.screen)


    def draw_health_bar_player(self, screen):
        BAR_LENGTH = 140
        BAR_HEIGHT = 30
        fill = (self.player.player_life_point / 3) * BAR_LENGTH
        outline_rect = pg.Rect(10, 60, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(10, 60, fill, BAR_HEIGHT)
        pg.draw.rect(self.screen, GREEN, fill_rect)
        pg.draw.rect(self.screen, BLACK, outline_rect, 5)


    def draw_health_bar_headquarter(self, screen):
        for headquarter in self.headquarter:
            if headquarter.headquarter_life_point > 0:
                BAR_LENGTH = 120
                BAR_HEIGHT = 20
                fill = (headquarter.headquarter_life_point / 2) * BAR_LENGTH
                outline_rect = pg.Rect(215 + headquarter.i * 150, 10, BAR_LENGTH, BAR_HEIGHT)
                fill_rect = pg.Rect(215 + headquarter.i * 150, 10, fill, BAR_HEIGHT)
                pg.draw.rect(self.screen, PINK, fill_rect)
                pg.draw.rect(self.screen, BLACK, outline_rect, 5)


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
        line_font = pg.font.Font('freesansbold.ttf', 50)
        list_of_messages = ["GAME OVER!", f"Your score is {self.player.player_score} points.", "Try harder next time."]
        for index, message in enumerate(list_of_messages):
            line = line_font.render(message, True, YELLOW)
            line_surface = pg.Surface(line.get_size())
            line_surface.fill(BLACK)
            line_surface.blit(line, (0, 0))
            if index == 0:
                self.screen.blit(line_surface, (350, 20))
            elif index == 1:
                self.screen.blit(line_surface, (220, 250))
            else:
                self.screen.blit(line_surface, (250, 430))


    def loading_buttons_on_game_lose_screen(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_texts = ["MAIN", "PAGE", "EXIT", "GAME"]
        self.list_of_button_positions_x = [340, 340, 520, 520]
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
        first_line_font = pg.font.Font('freesansbold.ttf', 50)
        line_font = pg.font.Font('freesansbold.ttf', 40)
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
            list_of_messages.extend(["Your score has been saved!", "You can check it in the Highscores", "menu on the main page."])

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
                self.screen.blit(line_surface, (250, 20))
            elif index == 1:
                self.screen.blit(line_surface, (290, 160))
            elif self.final_player_score_in_highscores and index == 5:
                self.screen.blit(line_surface, (290, 540))
            else:
                self.screen.blit(line_surface, (20, 160 + index * 60))


    def loading_buttons_on_game_win_screen(self, screen, mouse_position, list_of_button_texts, buttons_size_x, buttons_size_y):
        self.mouse_position = pg.mouse.get_pos()
        self.list_of_button_texts = ["MAIN", "PAGE", "EXIT", "GAME"]
        self.list_of_button_positions_x = [340, 340, 520, 520]
        self.list_of_button_positions_y = [665, 705, 665, 705]
        self.buttons_size_x = 170
        self.buttons_size_y = 110

        if self.final_player_score_in_highscores:
            self.list_of_button_texts.extend(["SAVE", "SCORE"])
            self.list_of_button_positions_x.extend([780, 780])
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