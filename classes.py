#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from constantes import *
from random import randint


class Labyrinth:

    def __init__(self, file):
        self.file = str(file)
        self.map_labyrinthe = 0

    def map_building(self):
        # for create structur of labyrinth whit the file 2
        with open(self.file, "r") as file:
            map_labyrinthe = []
            for line in file:
                line_laby = []
                for letter in line:
                    if letter != "\n":
                        # add letter in the list
                        line_laby.append(letter)
                # add line in the list map_labyrinthe
                map_labyrinthe.append(line_laby)
            self.map_labyrinthe = map_labyrinthe

    def display_lab(self, window):
        # to display the PNG of the labyrinth
        wall = pygame.image.load(picture_rampart).convert()
        self.tiles = pygame.image.load(picture_tiles).convert()
        guardian = pygame.image.load(picture_guardian).convert_alpha()
        # take letter and line in list of map_labyrinthe, if the letter is a m we make one wall else one tiles.
        num_line = 0
        for line in self.map_labyrinthe:
            num_letter = 0
            for letter in line:
                x = num_letter * len_sprite
                y = num_line * len_sprite
                if letter == "x":
                    window.blit(wall, (x, y))
                if letter == " ":
                    window.blit(self.tiles, (x, y))
                if letter == "A":
                    window.blit(self.tiles, (x, y))
                    window.blit(guardian, (x, y))
                num_letter += 1
            num_line += 1

    # this method return one objet random in the map
    def random_obj(self, window):
        number_obj = 0
        for obj in rdm_obj:
            keep = True
            while keep:
                random_x = randint(0, 14)
                random_y = randint(0, 14)
                if self.map_labyrinthe[random_x][random_y] == " ":
                    # select letter for first objet in list rdm_obj
                    letter_object = 'ijk'
                    x = random_x * len_sprite
                    y = random_y * len_sprite
                    obj_lab_rdm = pygame.image.load(obj).convert_alpha()
                    window.blit(obj_lab_rdm, (y, x))
                    self.map_labyrinthe[random_x][random_y] = letter_object[number_obj]
                    number_obj += 1
                    keep = False


class Characters:

    def __init__(self, character, labyrinth, window):
        self.character = pygame.image.load(character).convert_alpha()
        # position of the box, 15 max
        self.case_x = 0
        self.case_y = 0
        # real position whit pixel
        self.x = 0
        self.y = 0
        self.window = window
        self.labyrinth = labyrinth
        self.inventory = []

    def take_obj(self):
        obj_nb = 0
        if self.labyrinth.map_labyrinthe[self.case_y][self.case_x] != ' ' and self.labyrinth.map_labyrinthe[self.case_y][self.case_x] != 'A':
            if self.labyrinth.map_labyrinthe[self.case_y][self.case_x] == "i":
                obj_nb = 0
            elif self.labyrinth.map_labyrinthe[self.case_y][self.case_x] == "j":
                obj_nb = 1
            elif self.labyrinth.map_labyrinthe[self.case_y][self.case_x] == "k":
                obj_nb = 2
            # for only take name and not ressources/ and .png
            obj_picked = rdm_obj[obj_nb]
            obj_picked = obj_picked[10:]
            obj_picked = obj_picked[:-4]
            print("you picked up : {}".format(obj_picked))
            self.inventory.append(obj_picked)
            self.labyrinth.map_labyrinthe[self.case_y][self.case_x] = " "

    def end_game(self):
        if self.labyrinth.map_labyrinthe[self.case_y][self.case_x] == "A":
            if len(self.inventory) == len(rdm_obj):
                win = pygame.image.load("ressource/win.png").convert_alpha()
                self.window.blit(win, (80, 110))
                pygame.display.flip()
                print('Congratulation, you win')
            else:
                lose = pygame.image.load("ressource/lose.png").convert_alpha()
                self.window.blit(lose, (80, 100))
                pygame.display.flip()
                print('Lose, u forgot : {} object'.format(len(rdm_obj)-len(self.inventory)))
            self.labyrinth.map_labyrinthe[self.case_y][self.case_x-1] = "x"

    def moove(self, direction):
        if direction == "right":
            if self.case_x < (nb_sprite - 1):
                if self.labyrinth.map_labyrinthe[self.case_y][self.case_x+1] != "x":
                    self.case_x += 1
                    self.end_game()
                    self.take_obj()
        if direction == "left":
            if self.case_x > 0:
                if self.labyrinth.map_labyrinthe[self.case_y][self.case_x-1] != "x":
                    self.window.blit(self.labyrinth.tiles, (self.x, self.y))
                    self.case_x -= 1
                    self.end_game()
                    self.take_obj()
        if direction == "up":
            if self.case_y > 0:
                if self.labyrinth.map_labyrinthe[self.case_y-1][self.case_x] != "x":
                    self.window.blit(self.labyrinth.tiles, (self.x, self.y))
                    self.case_y -= 1
                    self.end_game()
                    self.take_obj()
        if direction == "down":
            if self.case_y < (nb_sprite - 1):
                if self.labyrinth.map_labyrinthe[self.case_y+1][self.case_x] != "x":
                    self.window.blit(self.labyrinth.tiles, (self.x, self.y))
                    self.case_y += 1
                    self.end_game()
                    self.take_obj()
        self.window.blit(self.labyrinth.tiles, (self.x, self.y))
        self.x = self.case_x * len_sprite
        self.y = self.case_y * len_sprite
        pygame.display.flip()
        self.window.blit(self.labyrinth.tiles, (self.x, self.y))
