# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 19:46:16 2022

@author: User
"""
# In[1]
from random import randint
import pgzrun
import pygame
import pgzero
from pgzero.builtins import Actor


# In[2]
#define size of screen
WIDTH = 800
HEIGHT = 600

#Define actors
balloon = Actor("balloon88")
balloon.pos = 400, 300

bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10,200)

house = Actor("house")
house.pos = randint(800,1600), 450

tree = Actor("tree")
tree.pos = randint(800, 1600), 450

# In[3]
#Initial game conditions
bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0
levelNum = 1
speed = 2
scores = []
lives = 3
# In[3]
#define function to keep track of high scores
def update_high_scores():
	global score, scores
	filename = r"C:\Users\Michael Low\Desktop\college\EE 104\Lab 7\balloon flight\scores.txt"
	scores = []
	with open(filename, "r") as file:
		line = file.readline()
		high_scores = line.split()
		for high_score in high_scores:
			if (score > int(high_score)):
				scores.append(str(score) + " ")
				score = int(high_score)
			else:
				scores.append(str(high_score) + " ")
		with open(filename, "w") as file:
			for high_score in scores:
				file.write(high_score)

#Hack and Tweak 1: displays 10 high scores now via changing text file.
def display_high_scores():
	screen.draw.text("HIGH SCORES", (350, 150), color = "black")
	y = 175
	position = 1
	for high_score in scores:
		screen.draw.text(str(position) + ". " + high_score, (350, y), color = "black")
		y+= 25
		position += 1
		

# In[4]
#define game screen
def draw():
	 screen.blit("background", (0,0))
	 if not game_over:
		 balloon.draw()
		 bird.draw()
		 house.draw()
		 tree.draw()
		 screen.draw.text("Score: " + str(score), (700,5), color = "black")
		 #add lives counter for hack and tweaks #4
		 screen.draw.text("Lives left: " + str(lives), color="black", topleft=(10,25), fontsize=25)
	 else:
		 display_high_scores()

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
		bird.image = "bird-down"
		bird_up = False
	else:
		bird.image = "bird-up"
		bird_up = True


def update():
	global game_over, score, number_of_updates, speed, levelNum, lives
	if not game_over:
		if not up:
			balloon.y += 1
			
		if bird.x > 0:
			bird.x -= speed*levelNum+4			#Hack and Tweak 2: make the bird move faster by having level speed added to base speed
			if number_of_updates == 9:
				flap()
				number_of_updates = 0
			else:
				number_of_updates +=1
			
		else:
			bird.x = randint(800,1600)
			bird.y = randint(10,200)
			score += 1
			number_of_updates = 0
			
		if house.right > 0:
			house.x -= speed*levelNum
		else:
			house.x = randint(800,1600)
			score += 1
			
		if tree.right > 0:
			tree.x -= speed*levelNum
		else:
			tree.x = randint(800,1600)
			score += 1
			
		if balloon.top < 0 or balloon.bottom > 560:
			#if hit subtract 1 life and reset the y position of the balloon
			lives = lives-1
			balloon.y = 300
		
		if balloon.collidepoint(bird.x, bird.y) or \
			balloon.collidepoint(house.x, house.y) or \
				balloon.collidepoint(tree.x, tree.y):
					#if hit subtract 1 life and reset the y position of the balloon
					lives = lives-1
					balloon.y = 300
					
		if(lives == 0):
			game_over = True
			update_high_scores()
		
		#Hack and Tweak 3: create levels
		if(score > (levelNum*10)):
			levelNum += 1
			
# In[6]
#run the game
pgzrun.go()