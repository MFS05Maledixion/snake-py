print("Lets start building the snake game in python!")

import pygame
import time
import random

# giving an initial value for each game
delay = 0.1
score = 0
high_score = 0

# giving the snake its speed
snake_speed = 15

# defiing the width and height of the screen
width_x = 960
height_y = 720

# defining the colors of the text shown on the board
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 64, 64)
green = pygame.Color(118, 238, 0)
blue = pygame.Color(0, 205, 205)