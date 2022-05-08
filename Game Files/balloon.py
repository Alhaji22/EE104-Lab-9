# -*- coding: utf-8 -*-

import pgzrun
import pygame
import pgzrun
import random
from pgzero.builtins import Actor
from random import randint

balloon = Actor('balloon')
balloon.pos = 400, 300
bird = Actor('bird-up')
bird.pos = randint(800, 1600), randint(10, 200)
house = Actor('house')
house.pos = randint(900, 1000 ), 460 #change spacing of house
tree = Actor('tree')
tree.pos = randint(1000, 1600), 460 #Change spacing of tree

WIDTH = 800
HEIGHT = 600
GRAVITY_STRENGTH = 3 #Change gravity of the balloon
bird_up = True
up = False
lives = 5
levels = 1 
game_over = False
score = 0
new_level = 0
scores = []


def draw():
    screen.blit('background', (0,0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text('Score Achieved: ' + str(score), (500, 5), color='black')
        screen.draw.text('# of Lives: ' + str(lives), (300, 5), color='black') 
        screen.draw.text('Levels Passed: ' + str(levels), (100, 5), color='black') 
  

def on_mouse_down():
    global up
    up = True
    balloon.y -= 50

def on_mouse_up():
    global up
    up = False

def flap():
    global bird_up
    if bird_up:
        bird.image = 'bird-down'
        bird_up = False
    else:
        bird.image = 'bird-up'
        bird_up = True

def update():
    global game_over, score, new_level, levels, lives
    if not game_over:
        if score%10 == 0 and score != 0:
            score += 1
            levels += 1 
        if not up: balloon.y += GRAVITY_STRENGTH
        if bird.x > 0:
            bird.x -= 5*levels 
            if new_level == 9:
                flap()
                new_level = 0
            else:
                new_level += 1
        else:
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            score += 1
            new_level = 0   
        if house.right > 0: house.x -= 4*levels 
        else:
            house.x = randint(800, 1600)
            score += 1
        if tree.right > 0: tree.x -= 4*levels
        else:
            tree.x = randint(800, 1600)
            score += 1
        if balloon.top < 0 or balloon.bottom > 560:
            game_over = True
            
        if (balloon.collidepoint(bird.x, bird.y) or balloon.collidepoint(house.x, house.y) or balloon.collidepoint(tree.x, tree.y)):
            if (lives > 1): #2 Lives: added in logic for lives to keep the game going
                bird.x = randint(800, 1600)
                bird.y = randint(10, 200)
                house.x = randint(800, 1600)
                tree.x = randint(800, 1600)
				
                lives -= 1
            else:
                game_over = True
             

pgzrun.go()
