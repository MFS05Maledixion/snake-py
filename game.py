print("Lets start building the snake game in python!")

import pygame
import time
import random

# giving an initial value for each game
print("initializing the game values...")
delay = 0.1
score = 0
high_score = 0

# giving the snake its speed
print("setting the speed of the snake...")
snake_speed = 15

# defiing the width and height of the screen
print("setting the width and height of the screen...")
width_x = 960
height_y = 720

# defining the colors of the text shown on the board
print("setting the colors of the text...")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 64, 64)
green = pygame.Color(118, 238, 0)
blue = pygame.Color(0, 205, 205)

# initializing the pygame
print("initializing the pygame...")
pygame.init()

# initializing the window
print("initializing the window...")
pygame.display.set_caption("Snake Game in Python")
window = pygame.display.set_mode((width_x, height_y))

# to control the fps of the game
print("setting the fps of the game...")
frame_per_sec = pygame.time.Clock()

# define snake position at default
print("setting the default position of the snake...")
position_snake = [120, 60]

# creating the snake body by assigning five blocks to it
print("creating the snake body...")
snake_body = [
    [120, 60],
    [110, 60],
    [100, 60],
    [90, 60],
    [80, 60],
]

# allocated food in a random manner within game window
print("allocating food in a random manner within the game window...")
position_food = [
    random.randrange(1, (width_x // 10)) * 10,
    random.randrange(1, (height_y // 10)) * 10,
]
spawn_food = True

# defining the default direction of the snake on onset of the game
print("setting the default direction of the snake on onset of the game...")
snake_direction = "RIGHT"
flexible_to_change = snake_direction


# creating the score function
print("creating the score function...")


def score_metrics(selection, color, font, size):
    # build font
    font_score = pygame.font.SysFont(font, size)

    # create surface
    surface_score = font_score.render("The Score earned: " + str(score), True, color)

    # create rectangle
    rect_score = surface_score.get_rect()

    # build display
    window.blit(surface_score, rect_score)


# creating the GAME OVER function
print("creating the GAME OVER function...")


def game_over():
    # game over font
    game_over_font = pygame.font.SysFont("times new roman", 50)

    # game over surface
    game_over_surface = game_over_font.render("GAME OVER!" + str(score), True, red)

    # game over rectangle
    game_over_rect = game_over_surface.get_rect()

    # game over display in middle of screen
    game_over_rect.midtop = (width_x / 2, height_y / 4)

    # game over display
    window.blit(game_over_surface, game_over_rect)

    # update score with flip
    pygame.display.flip()

    # five second delay
    time.sleep(5)

    # quit game
    pygame.quit()

    # exit console
    quit()


# creating the main function for the game
print("creating the main function for the game...")


def main():
    global flexible_to_change
    global snake_direction
    global score
    global spawn_food
    global position_food
    global snake_body
    global position_snake

    # waiting for user to press space to start game
    print("waiting for user to press space to start game...")
    hasPressedSpace = False
    while not hasPressedSpace:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hasPressedSpace = True


    while True:
        # validate keystrokes for movement
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    flexible_to_change = "UP"
                if event.key == pygame.K_DOWN:
                    flexible_to_change = "DOWN"
                if event.key == pygame.K_LEFT:
                    flexible_to_change = "LEFT"
                if event.key == pygame.K_RIGHT:
                    flexible_to_change = "RIGHT"

        # since we dont want opposite directions in our case we are using this if condition
        if flexible_to_change == "UP" and snake_direction != "DOWN":
            snake_direction = "UP"
        if flexible_to_change == "DOWN" and snake_direction != "UP":
            snake_direction = "DOWN"
        if flexible_to_change == "LEFT" and snake_direction != "RIGHT":
            snake_direction = "LEFT"
        if flexible_to_change == "RIGHT" and snake_direction != "LEFT":
            snake_direction = "RIGHT"

        # making the snake move
        if snake_direction == "UP":
            position_snake[1] -= 10
        if snake_direction == "DOWN":
            position_snake[1] += 10
        if snake_direction == "LEFT":
            position_snake[0] -= 10
        if snake_direction == "RIGHT":
            position_snake[0] += 10

        # snake body growing mechanism
        # when snake and food collide, snake grows and score increases by 15 and new food is spawned
        snake_body.insert(0, list(position_snake))
        if (
            position_snake[0] == position_food[0]
            and position_snake[1] == position_food[1]
        ):
            score = score + 15
            spawn_food = False
        else:
            snake_body.pop()

        # food spawning mechanism
        print("spawning the food...")
        if not spawn_food:
            position_food = [
                random.randrange(1, (width_x // 10)) * 10,
                random.randrange(1, (height_y // 10)) * 10,
            ]
        spawn_food = True
        window.fill(white)

        # drawing the snake
        print("drawing the snake...")
        for position in snake_body:
            pygame.draw.rect(
                window, green, pygame.Rect(position[0], position[1], 10, 10)
            )
        pygame.draw.rect(
            window,
            red,
            pygame.Rect(position_food[0], position_food[1], 10, 10),
        )

        # game over conditions when snake hits the wall
        if position_snake[0] < 0 or position_snake[0] > width_x - 10:
            game_over()
        if position_snake[1] < 0 or position_snake[1] > height_y - 10:
            game_over()

        # game over conditions when snake hits itself
        for block in snake_body[1:]:
            if position_snake[0] == block[0] and position_snake[1] == block[1]:
                game_over()

        # displaying the score
        print("displaying the score...")
        score_metrics(1, black, "times new roman", 20)

        # updating the display
        print("updating the display...")
        pygame.display.update()


        # refresh rate of the game
        print("setting the refresh rate of the game...")
        frame_per_sec.tick(snake_speed)

# calling the main function
print("calling the main function...")
main()