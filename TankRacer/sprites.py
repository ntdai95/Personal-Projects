import pygame as pg
import random
from os import path
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "tank.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 630
        self.player_x_change = 0
        self.player_y_change = 0
        self.player_move = None
        self.player_life_point = 3
        self.player_score = 0

    def update(self, round_count):
        if self.player_move == None:
            self.player_x_change = 0
            self.player_y_change = 0
        elif self.player_move == "LEFT" and self.player_y_change == 0:
            self.player_x_change = -7
        elif self.player_move == "RIGHT" and self.player_y_change == 0:
            self.player_x_change = 7
        elif self.player_move == "UP" and self.player_x_change == 0:
            self.player_y_change = -7
        elif self.player_move == "DOWN" and self.player_x_change == 0:
            self.player_y_change = 7

        if self.rect.x <= 200:
            self.rect.x = 200
        elif self.rect.x >= 655:
            self.rect.x = 655
        self.rect.x += self.player_x_change

        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 630:
            self.rect.y = 630
        self.rect.y += self.player_y_change


class Bullet(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "bullet.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -500
        self.rect.y = -500
        self.bullet_is_on = False
        self.bullet_y_change = -15

    def update(self, round_count):
        if self.bullet_is_on:
            self.rect.y += self.bullet_y_change
            if self.rect.y <= 0:
                self.bullet_is_on = False
        else:
            self.rect.x = -500
            self.rect.y = -500


class Landmine(pg.sprite.Sprite):
    def __init__(self, i):
        super().__init__()
        self.i = i
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "landmine.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000
        self.landmine_y_change = 5

    def update(self, round_count):
        if round_count != 4 and round_count != 8 and round_count != 12:
            if self.rect.x == -1000 and self.rect.y == -1000:
                self.rect.x = random.choice([200, 350, 500, 650])
                if self.i <= 2:
                    self.rect.y = -(self.i + 1) * 150
                else:
                    self.rect.y = -(self.i + 2) * 150

            self.rect.y += self.landmine_y_change
            if self.rect.y >= 1050:
                self.rect.x = random.choice([200, 350, 500, 650])
                self.rect.y = -150
        else:
            self.rect.x = -1000
            self.rect.y = -1000


class Medal(pg.sprite.Sprite):
    def __init__(self, i):
        super().__init__()
        self.i = i
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "medal.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000
        self.medal_y_change = 5

    def update(self, round_count):
        if round_count != 4 and round_count != 8 and round_count != 12:
            if self.rect.x == -1000 and self.rect.y == -1000:
                self.rect.x = random.choice([200, 350, 500, 650])
                self.rect.y = -600 * (self.i + 1)

            self.rect.y += self.medal_y_change
            if self.rect.y >= 1050:
                self.rect.x = random.choice([200, 350, 500, 650])
                self.rect.y = -150
        else:
            self.rect.x = -1000
            self.rect.y = -1000


class Airplane(pg.sprite.Sprite):
    def __init__(self, i):
        super().__init__()
        self.i = i
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "airplane.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000
        self.airplane_x_change = 5 * (-1) ** (self.i + 1)
        self.airplane_life_point = 1
        
    def update(self, round_count):
        if (round_count == 4 or round_count == 8) and self.airplane_life_point > 0:
            if self.rect.x == -1000 and self.rect.y == -1000:
                if self.i == 0:
                    self.rect.x = random.randint(200, 425)
                else:
                    self.rect.x = random.randint(425, 655)
                self.rect.y = 0

            self.rect.x += self.airplane_x_change
            if self.rect.x <= 200 or 655 <= self.rect.x:
                self.airplane_x_change = -self.airplane_x_change
        else:
            self.rect.x = -1000
            self.rect.y = -1000


class Bomb(pg.sprite.Sprite):
    def __init__(self, i):
        super().__init__()
        self.i = i
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "bomb.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000
        self.bomb_y_change = 5

    def update(self, round_count):
        if round_count == 4 or round_count == 8 or round_count == 12:
            if self.rect.x == -1000 and self.rect.y == -1000:
                if self.i == 0:
                    self.rect.x = random.choice([200, 350])
                else:
                    self.rect.x = random.choice([500, 650])
                self.rect.y = 0

            self.rect.y += self.bomb_y_change
            if self.rect.y >= 900:
                if self.i == 0:
                    self.rect.x = random.choice([200, 350])
                else:
                    self.rect.x = random.choice([500, 650])
                self.rect.y = 0
        else:
            self.rect.x = -1000
            self.rect.y = -1000


class Headquarter(pg.sprite.Sprite):
    def __init__(self, i):
        super().__init__()
        self.i = i
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "headquarter.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000
        self.headquarter_life_point = 2

    def update(self, round_count):
        if round_count == 12 and self.headquarter_life_point > 0:
            if self.rect.x == -1000 and self.rect.y == -1000:
                self.rect.x = 200 + self.i * 150
                self.rect.y = 30
        else:
            self.rect.x = -1000
            self.rect.y = -1000


class Rocket(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "rocket.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000
        self.rocket_x_change = 5

    def update(self, round_count):
        if round_count == 12:
            if self.rect.x == -1000 and self.rect.y == -1000:
                self.rect.x = 0
                self.rect.y = random.randint(150, 630)

            self.rect.x += self.rocket_x_change
            if self.rect.x >= 1000:
                self.rect.x = 0
                self.rect.y = random.randint(150, 630)
        else:
            self.rect.x = -1000
            self.rect.y = -1000