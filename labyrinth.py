#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
from constantes import *
from classes import *


""" this file is a script to play a game of labyrinth, 
it corresponds at my project 3 of openclassroom 

for win you need to take the objects and to lull the guard 
"""


def launch_game():

    # initialization of pygame and create windows whit 15 sprites
    pygame.init()
    window = pygame.display.set_mode((len_window, len_window))


    
    menu = 1
    game = 0

    while menu:
        # display and refresh the labyrinth whit wall and tiles in the windows
        menu = pygame.image.load("ressource/menu.png").convert()
        setting_game = pygame.image.load("ressource/setting.png").convert()
        window.blit(menu, (0, 0))
        
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                menu = 0
                game = 0
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    menu = 0
                    setting = 0
                    game = 1
                    labyrinth = Labyrinth("map")
                    labyrinth.map_building()
                    labyrinth.display_lab(window)
                    mg = Characters(picture_mcgyver, labyrinth)
                    window.blit(mg.character, (mg.x,mg.y))
                    labyrinth.random_obj(window)
                    pygame.display.flip()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE]:
            window.blit(setting_game, (0, 0))
        pygame.display.flip()


    # initialization of loop, to leave the game need to game = 0
        while game:
                # Loop for leave the game
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    menu = 1
                    game = 0
                    # touch to move in the labyrinth
                elif event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        mg.moove("down", window)
                    if event.key == K_LEFT:
                        mg.moove("left", window)
                    if event.key == K_UP:
                        mg.moove("up", window)
                    if event.key == K_RIGHT:
                        mg.moove("right", window)
                    
                window.blit(mg.character, (mg.x, mg.y))
                pygame.display.flip()
                    

                

launch_game()