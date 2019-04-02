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
        #for create structur of labyrinth whit the file 2
        with open(self.file, "r") as file:
            map_labyrinthe = []
            for line in file:
                line_laby = []
                for letter in line:
                    if letter != "\n":
                        line_laby.append(letter) #add letter in the list 
                map_labyrinthe.append(line_laby) #add line in the list map_labyrinthe
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
                if letter == "m":
                    window.blit(wall, (x,y))
                if letter == "O":
                    window.blit(self.tiles, (x, y))
                if letter == "A":
                    window.blit(self.tiles, (x, y))
                    window.blit(guardian, (x, y))
                if letter == "D":
                    window.blit(self.tiles, (x, y))
                num_letter +=1
            num_line +=1
    # this method return one objet random in the map
    def random_obj(self, window):
        for obj in rdm_obj:
            keep = True
            while keep:
                random_x = randint(0,14) 
                random_y = randint(0,14) 
                if self.map_labyrinthe[random_x][random_y] == "O":
                    
                    x = random_x * len_sprite
                    y = random_y * len_sprite
                    obj_lab_rdm = pygame.image.load(obj).convert()
                    window.blit(obj_lab_rdm, (y, x))
                    obj = obj[10:]
                    obj = obj [:-4]
                    pos_obj[obj] = (random_x, random_y)
                    self.map_labyrinthe[random_x][random_y] = "i"
                    keep = False

class Characters:
    def __init__(self, character, labyrinth):
        self.character = pygame.image.load(character).convert_alpha()
        #position of the box, 15 max
        self.case_x = 0
        self.case_y = 0
        # real position whit pixel 
        self.x = 0
        self.y = 0
        self.labyrinth = labyrinth
        self.inventory = []


    def moove(self, direction, window):
        
        if direction == "right":
            if self.case_x < (nb_sprite - 1):
                if self.labyrinth.map_labyrinthe[self.case_y][self.case_x+1] == "A":
                    if len(self.inventory) == len(rdm_obj):
                        win = pygame.image.load("ressource/win.png").convert_alpha()
                        window.blit(win, (80, 110))
                        pygame.display.flip()
                        print('Congratulation, you win')
                        for event in pygame.event.get():
                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    menu = 1
                                    menu = pygame.image.load("ressource/menu.png").convert()
                                    window.blit(menu, (0, 0))
                                    pygame.display.flip() 
                                    game = 0
  
                    else:
                        lose = pygame.image.load("ressource/lose.png").convert_alpha()
                        window.blit(lose, (80, 100))
                        pygame.display.flip()
                        print('Lose, u forgot : {} object'.format(len(rdm_obj)-len(self.inventory)))
                        for event in pygame.event.get():
                            if event.type == KEYDOWN and event.key == K_ESCAPE:
                                menu = 1
                                menu = pygame.image.load("ressource/menu.png").convert()
                                window.blit(menu, (0, 0))
                                pygame.display.flip() 
                                game = 0
                           
                      
                    window.blit(self.labyrinth.tiles, (self.x, self.y))
                    pygame.display.flip()
                    self.case_x += 1
                    pygame.display.flip()
                    self.x = self.case_x * len_sprite
                    self.labyrinth.map_labyrinthe[self.case_y][self.case_x-1] = "m"
                        
                elif self.labyrinth.map_labyrinthe[self.case_y][self.case_x+1] != "m":
                    window.blit(self.labyrinth.tiles, (self.x+1, self.y)) #display tiles after moove
                    pygame.display.flip()
                    self.case_x += 1
                    if self.labyrinth.map_labyrinthe[self.case_y][self.case_x] == "i":
                        for obj in pos_obj:
                            if pos_obj[obj] == (self.case_y, self.case_x):
                                print("you picked up : {}".format(obj))
                                self.inventory.append(obj)
                                self.labyrinth.map_labyrinthe[self.case_y][self.case_x] = "O"
                    window.blit(self.labyrinth.tiles, (self.x, self.y))
                    self.x = self.case_x * len_sprite
                    pygame.display.flip()
                    window.blit(self.labyrinth.tiles, (self.x, self.y)) #display tiles after moove
                    self.x = self.case_x * len_sprite

        if direction == "left":
            if self.case_x > 0:
                if self.labyrinth.map_labyrinthe[self.case_y][self.case_x-1] != "m":
                    window.blit(self.labyrinth.tiles, (self.x-1, self.y)) #display tiles after moove
                    pygame.display.flip()
                    window.blit(self.labyrinth.tiles, (self.x, self.y))
                    self.case_x -= 1
                    if self.labyrinth.map_labyrinthe[self.case_y][self.case_x] == "i":
                        for obj in pos_obj:
                            if pos_obj[obj] == (self.case_y, self.case_x):
                                print("you picked up : {}".format(obj))
                                self.inventory.append(obj)
                                self.labyrinth.map_labyrinthe[self.case_y][self.case_x] = "O"

                    window.blit(self.labyrinth.tiles, (self.x, self.y))
                    self.x = self.case_x * len_sprite
                    pygame.display.flip()
                    window.blit(self.labyrinth.tiles, (self.x, self.y)) #display tiles after moove

        if direction == "up":
            if self.case_y > 0:
                if self.labyrinth.map_labyrinthe[self.case_y-1][self.case_x] != "m":
                    window.blit(self.labyrinth.tiles, (self.x, self.y))
                    self.case_y -= 1
                    if self.labyrinth.map_labyrinthe[self.case_y][self.case_x] == "i":
                        for obj in pos_obj:
                            if pos_obj[obj] == (self.case_y, self.case_x):
                                print("you picked up : {}".format(obj))
                                self.inventory.append(obj)
                                self.labyrinth.map_labyrinthe[self.case_y][self.case_x] = "O"

                    window.blit(self.labyrinth.tiles, (self.x, self.y))
                    self.y = self.case_y * len_sprite
                    pygame.display.flip()
                    window.blit(self.labyrinth.tiles, (self.x, self.y)) #display tiles after moove
                    self.y = self.case_y * len_sprite
        if direction == "down":
            if self.case_y < (nb_sprite - 1):
                if self.labyrinth.map_labyrinthe[self.case_y+1][self.case_x] != "m":
                    window.blit(self.labyrinth.tiles, (self.x, self.y))
                    self.case_y += 1
                    if self.labyrinth.map_labyrinthe[self.case_y][self.case_x] == "i":
                        for obj in pos_obj:
                            if pos_obj[obj] == (self.case_y, self.case_x):
                                print("you picked up : {}".format(obj))
                                self.inventory.append(obj)
                                self.labyrinth.map_labyrinthe[self.case_y][self.case_x] = "O"
                    window.blit(self.labyrinth.tiles, (self.x, self.y))
                    self.y = self.case_y * len_sprite
                    pygame.display.flip()
                    window.blit(self.labyrinth.tiles, (self.x, self.y)) #display tiles after moove
                    
                    

