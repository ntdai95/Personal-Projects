import pygame as pg
import random
from os import path
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "horse.png")).convert_alpha()
        self.mini_image = pg.transform.scale(self.image, (70, 70))
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 500
        self.player_x_change = 0
        self.player_y_change = 0
        self.player_move_horizontal = None
        self.player_move_vertical = None
        self.player_life_point = 5
        self.player_score = 0

    def update(self, round_count):
        if self.player_move_horizontal == None:
            self.player_x_change = 0
        elif self.player_move_horizontal == "LEFT"and self.rect.y == 500:
            self.player_x_change = -15
        elif self.player_move_horizontal == "RIGHT"and self.rect.y == 500:
            self.player_x_change = 15

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 1300:
            self.rect.x = 1300
        self.rect.x += self.player_x_change

        if self.player_move_vertical == "UP" and self.rect.y == 500:
            self.player_y_change = -15
        elif self.rect.y <= 100:
            self.player_y_change = 15
        elif self.rect.y >= 500:
            self.player_y_change = 0
        self.rect.y += self.player_y_change


class Fence(pg.sprite.Sprite):
    def __init__(self, i):
        super().__init__()
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "fence.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = 570
        self.i = i
        self.fence_x_change = -10
        self.fence_appear = False

    def update(self, round_count):
        if round_count == 2 or round_count == 8 or round_count == 12:
            self.rect.x = -1000
            self.fence_appear = False
        elif self.i == 0 and self.fence_appear and round_count != 2 and round_count != 8 and round_count != 12:
            self.rect.x = random.randint(1500, 1800)
            self.rect.x += self.fence_x_change
        elif self.i == 0 and self.fence_appear == False and round_count != 2 and round_count != 8 and round_count != 12:
            self.rect.x += self.fence_x_change
        elif self.fence_appear and round_count != 2 and round_count != 8 and round_count != 12:
            if random.choice([True, False]):
                self.rect.x = random.randint(1500, 1800)
                self.rect.x += self.fence_x_change
        else:
            self.rect.x += self.fence_x_change
        

class Bat(pg.sprite.Sprite):
    def __init__(self, i):
        super().__init__()
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "bat.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = random.randint(100, 550)
        self.i = i
        self.bat_x_change = -10
        self.bat_appear = False

    def update(self, round_count):
        if round_count == 2 or round_count == 8 or round_count == 12:
            self.rect.x = -1000
            self.bat_appear = False
        elif self.i == 0 and self.bat_appear and round_count != 2 and round_count != 8 and round_count != 12:
            self.rect.x = random.randint(1500, 1800)
            self.rect.y = random.randint(100, 550)
            self.rect.x += self.bat_x_change
        elif self.i == 0 and self.bat_appear == False and round_count != 2 and round_count != 8 and round_count != 12:
            self.rect.x += self.bat_x_change
        elif self.bat_appear and round_count != 2 and round_count != 8 and round_count != 12:
            if random.choice([True, False]):
                self.rect.x = random.randint(1500, 1800)
                self.rect.y = random.randint(100, 550)
                self.rect.x += self.bat_x_change
        else:
            self.rect.x += self.bat_x_change


class Arrow(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "arrow.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000
        self.arrow_x_change = 25
        self.arrow_is_on = False

    def update(self, round_count):
        if self.arrow_is_on:
            self.rect.x += self.arrow_x_change
            if self.rect.x >= 1500:
                self.arrow_is_on = False
        else:
            self.rect.x = -1000
            self.rect.y = -1000            


class Dragon(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "dragon.png")).convert_alpha()
        self.mini_image = pg.transform.scale(self.image, (70, 70))
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = 500
        self.dragon_y_change = -10
        self.dragon_life_point = 5

    def update(self, round_count):
        if round_count == 2 or round_count == 8:
            if self.rect.x == -1000:
                self.rect.x = 1200
                self.rect.y = random.randint(100, 500)

            self.rect.y += self.dragon_y_change
            if self.rect.y <= 100:
                self.dragon_y_change = 10
            elif self.rect.y >= 500:
                self.dragon_y_change = -10
        else:
            self.rect.x = -1000
            self.rect.y = 500


class Fire(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "fire.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = 500
        self.fire_x_change = -15
    
    def update(self, round_count):
        if round_count == 2:
            if self.rect.x == -1000 or self.rect.x <= -100:
                self.rect.x = 1300
                self.rect.y = random.randint(100, 500)

            self.rect.x += self.fire_x_change
        elif round_count == 8:
            if self.rect.x == -1000 or self.rect.x >= 1300:
                self.rect.x = 1300
                self.rect.y = random.randint(100, 500)
                self.fire_x_change = -15
            elif self.rect.x <= 0:
                self.rect.x = 0
                self.rect.y = random.randint(100, 500)
                self.fire_x_change = 15

            self.rect.x += self.fire_x_change
        else:
            self.rect.x = -1000
            self.rect.y = 500
            self.fire_x_change = -15


class Octopus(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "octopus.png")).convert_alpha()
        self.mini_image = pg.transform.scale(self.image, (70, 70))
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = 500
        self.octopus_y_change = -10
        self.octopus_life_point = 5

    def update(self, round_count):
        if round_count == 12:
            if self.rect.x == -1000:
                self.rect.x = 1200
                self.rect.y = random.randint(100, 500)

            self.rect.y += self.octopus_y_change
            if self.rect.y <= 100:
                self.octopus_y_change = 10
            elif self.rect.y >= 500:
                self.octopus_y_change = -10
        else:
            self.rect.x = -1000
            self.rect.y = 500


class Waterdrop(pg.sprite.Sprite):
    def __init__(self, i):
        super().__init__()
        self.image = pg.image.load(path.join(path.join(path.dirname(__file__), "Images"), "waterdrop.png")).convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = 1000
        self.i = i
        self.waterdrop_y_change = 10
        self.waterdrop_appear = False

    def update(self, round_count):
        if round_count != 12:
            self.waterdrop_appear = False
            self.rect.x = -1000
            self.rect.y = 1000
        elif (self.i == 0 or self.i == 1) and self.waterdrop_appear and round_count == 12:
            self.rect.x = random.randint(0, 1300)
            self.rect.y = 0
            self.rect.y += self.waterdrop_y_change
        elif (self.i == 0 or self.i == 1) and self.waterdrop_appear == False and round_count == 12:
            self.rect.y += self.waterdrop_y_change
        elif self.waterdrop_appear and round_count == 12:
            if random.choice([True, False]):
                self.rect.x = random.randint(0, 1300)
                self.rect.y = 0
                self.rect.y += self.waterdrop_y_change
        else:
            self.rect.y += self.waterdrop_y_change