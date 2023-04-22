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

# initializing the pygame
pygame.init()

# initializing the window
pygame.display.set_caption("Snake Game in Python")
window = pygame.display.set_mode((width_x, height_y))

# to control the fps of the game
frame_per_sec = pygame.time.Clock()

# define snake position at default
position_snake = [120, 60]

# creating the snake body by assigning five blocks to it
snake_body = [
    [120, 60],
    [110, 60],
    [100, 60],
    [90, 60],
    [80, 60],
]

# allocated food in a random manner within game window
position_food = [
    random.randrange(1, (width_x // 10)) * 10,
    random.randrange(1, (height_y // 10)) * 10,
]

spawn_food = True

# defining the default direction of the snake on onset of the game
snake_direction = "LEFT"
flexible_to_change = snake_direction