# Date: Febuary 1st, 2021
# Written by: Oscar Law
# Description: Tic tac toe game made with pygame (just for fun lol)

import pygame
import sys
import time
import random
import threading
from Box import Box
from Screens import Screen

# Initiating pygame
pygame.init()

# Setting caption for program
pygame.display.set_caption("Tic Tac Toe")

# Setting up the screen
screen_width = 600
screen_height = 665
win = pygame.display.set_mode((screen_width, screen_height))

# Colours for the program
white = (255, 255, 255)
black = (0, 0, 0)
shadow = (224, 238, 238)
red = (200, 0, 0)

# Fonts for the program
comicSans = pygame.font.SysFont("Arial", 30)
comicSansBig = pygame.font.SysFont("Arial", 100)

# Boxes for each square
box1 = Box()
box2 = Box()
box3 = Box()
box4 = Box()
box5 = Box()
box6 = Box()
box7 = Box()
box8 = Box()
box9 = Box()
boxes = [None, box1, box2, box3, box4, box5, box6, box7, box8, box9]

# Grid for the program
grid = (None, 1, 2, 3, 4, 5, 6, 7, 8, 9)
win_combinations = ((7, 8, 9), (4, 5, 6), (1, 2, 3), (7, 4, 1),
                    (8, 5, 2), (9, 6, 3), (7, 5, 3), (9, 5, 1))

# X and O images
x = pygame.image.load("X.png")
x = pygame.transform.scale(x, (175, 175))
o = pygame.image.load("O.png")
o = pygame.transform.scale(o, (175, 175))

# Game variables
turn = x
on_main_page = True
game_over = False
move_made = False

# Positions for each piece
positions = (None, (13, 10), (213, 10), (413, 10), (13, 210),
             (213, 210), (413, 210), (13, 410), (213, 410), (413, 410))


def get_var_name(variable):
    for name in globals():
        if eval(name) == variable:
            return name


def change_grid(box, piece, grid):
    index = int(get_var_name(box)[-1])
    grid[index] = piece
    return grid


def change_turn(turn):
    if turn == x:
        turn = o
    else:
        turn = x
    return turn


def computer_move():
    if not game_end_check(grid):
        global temp
        temp = False
        next_move_win_combinations = ((7, 8, 9), (7, 9, 8), (8, 9, 7), (4, 5, 6), (4, 6, 5), (5, 6, 4), (1, 2, 3), (1, 3, 2), (2, 3, 1), (7, 4, 1), (7, 1, 4), (
            4, 1, 7), (8, 5, 2), (8, 2, 5), (5, 2, 8), (9, 6, 3), (9, 3, 6), (3, 6, 9), (1, 5, 9), (1, 9, 5), (9, 5, 1), (7, 5, 3), (7, 3, 5), (5, 3, 7))
        corner_moves = [1, 3, 7, 9]
        side_moves = [2, 4, 6, 8]
        while temp == False:
            for i in next_move_win_combinations:
                if grid[i[0]] == "O" and grid[i[1]] == "O" and grid[i[2]] != "X" and grid[i[2]] != "O" or grid[i[0]] == "X" and grid[i[1]] == "X" and grid[i[2]] != "X" and grid[i[2]] != "O":
                    grid[i[2]] = "O"
                    temp = True
                    break
            if grid[5] != "X" and grid[5] != "O":
                grid[5] = "O"
                temp = True
            elif grid[7] != "X" and grid[7] != "O" or grid[9] != "X" and grid[9] != "O" or grid[1] != "X" and grid[1] != "O" or grid[3] != "X" and grid[3] != "O":
                while temp == False:
                    o = random.choice(corner_moves)
                    if grid[o] != "X" and grid[o] != "O":
                        grid[o] = "O"
                        temp = True
            else:
                while temp == False:
                    o = random.choice(side_moves)
                    if grid[o] != "X" and grid[o] != "O":
                        grid[o] = "O"
                        temp = True


def game_end_check(grid):
    game_tie_check = 0
    win_combinations = ((7, 8, 9), (4, 5, 6), (1, 2, 3),
                        (7, 4, 1), (8, 5, 2), (9, 6, 3), (7, 5, 3), (9, 5, 1))
    for i in win_combinations:
        if grid[i[0]] == "X" and grid[i[1]] == "X" and grid[i[2]] == "X":
            return "X wins"
    for i in win_combinations:
        if grid[i[0]] == "O" and grid[i[1]] == "O" and grid[i[2]] == "O":
            return "O wins"
    for a in range(1, 10):
        if grid[a] == "X" or grid[a] == "O":
            game_tie_check += 1
    if game_tie_check == 9:
        return "Tie game"


def reset_game():
    box1.taken = False
    box1.piece = None
    box2.taken = False
    box2.piece = None
    box3.taken = False
    box3.piece = None
    box4.taken = False
    box4.piece = None
    box5.taken = False
    box5.piece = None
    box6.taken = False
    box6.piece = None
    box7.taken = False
    box7.piece = None
    box8.taken = False
    box8.piece = None
    box9.taken = False
    box9.piece = None


while True:
    for event in pygame.event.get():
        # Checks if user has exited the screen
        if event.type == pygame.QUIT:
            sys.exit()

        win.fill(white)

        if on_main_page:
            title = comicSansBig.render("Tic Tac Toe", False, (0, 0, 0))
            win.blit(title, (50, 115))

            play_button = Screen(win)
            play_button.initialize_button(
                200, 415, 180, 60, 50, shadow, "Play", (247, 410))

            if play_button.button_pressed(200, 415, 180, 60) and event.type == pygame.MOUSEBUTTONUP:
                on_main_page = False
                reset_game()
                grid = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                turn = x
                game_over = False

        else:
            # Creates boxes for the tic tac toe board
            pygame.draw.rect(win, box1.color, (0, 0, 200, 200))
            pygame.draw.rect(win, box2.color, (200, 0, 200, 200))
            pygame.draw.rect(win, box3.color, (400, 0, 200, 200))
            pygame.draw.rect(win, box4.color, (0, 200, 200, 200))
            pygame.draw.rect(win, box5.color, (200, 200, 200, 200))
            pygame.draw.rect(win, box6.color, (400, 200, 200, 200))
            pygame.draw.rect(win, box7.color, (0, 400, 200, 200))
            pygame.draw.rect(win, box8.color, (200, 400, 200, 200))
            pygame.draw.rect(win, box9.color, (400, 400, 200, 200))

            # Creates lines for the tic tac toe board
            pygame.draw.line(win, black, (0, 200), (600, 200), 2)
            pygame.draw.line(win, black, (0, 400), (600, 400), 2)
            pygame.draw.line(win, black, (200, 0), (200, 600), 2)
            pygame.draw.line(win, black, (400, 0), (400, 600), 2)

            # Creates restart button
            restart_button = Screen(win)
            restart_button.initialize_button(
                450, 615, 140, 40, 30, shadow, "Restart", (470, 613))

            # Resets game if restart button is pressed
            if restart_button.button_pressed(450, 615, 140, 40) and event.type == pygame.MOUSEBUTTONUP:
                reset_game()
                grid = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                turn = x
                game_over = False

################################################################
            # Detects if mouse is hovering over box
            mos_x, mos_y = pygame.mouse.get_pos()
            if mos_x > 0 and mos_x <= 200 and mos_y > 0 and mos_y <= 200:
                box1.color = shadow

                # Detects if box has been chosen
                if event.type == pygame.MOUSEBUTTONUP and box1.taken != True:
                    box1.taken = True
                    move_made = True
            else:
                box1.color = white
            if mos_x > 200 and mos_x <= 400 and mos_y > 0 and mos_y <= 200:
                box2.color = shadow
                if event.type == pygame.MOUSEBUTTONUP and box2.taken != True:
                    box2.taken = True
                    move_made = True
            else:
                box2.color = white
            if mos_x > 400 and mos_x <= 600 and mos_y > 0 and mos_y <= 200:
                box3.color = shadow
                if event.type == pygame.MOUSEBUTTONUP and box3.taken != True:
                    box3.taken = True
                    move_made = True
            else:
                box3.color = white
            if mos_x > 0 and mos_x <= 200 and mos_y > 200 and mos_y <= 400:
                box4.color = shadow
                if event.type == pygame.MOUSEBUTTONUP and box4.taken != True:
                    box4.taken = True
                    move_made = True
            else:
                box4.color = white
            if mos_x > 200 and mos_x <= 400 and mos_y > 200 and mos_y <= 400:
                box5.color = shadow
                if event.type == pygame.MOUSEBUTTONUP and box5.taken != True:
                    box5.taken = True
                    move_made = True
            else:
                box5.color = white
            if mos_x > 400 and mos_x <= 600 and mos_y > 200 and mos_y <= 400:
                box6.color = shadow
                if event.type == pygame.MOUSEBUTTONUP and box6.taken != True:
                    box6.taken = True
                    move_made = True
            else:
                box6.color = white
            if mos_x > 0 and mos_x <= 200 and mos_y > 400 and mos_y <= 600:
                box7.color = shadow
                if event.type == pygame.MOUSEBUTTONUP and box7.taken != True:
                    box7.taken = True
                    move_made = True
            else:
                box7.color = white
            if mos_x > 200 and mos_x <= 400 and mos_y > 400 and mos_y <= 600:
                box8.color = shadow
                if event.type == pygame.MOUSEBUTTONUP and box8.taken != True:
                    box8.taken = True
                    move_made = True
            else:
                box8.color = white
            if mos_x > 400 and mos_x <= 600 and mos_y > 400 and mos_y <= 600:
                box9.color = shadow
                if event.type == pygame.MOUSEBUTTONUP and box9.taken != True:
                    box9.taken = True
                    move_made = True
            else:
                box9.color = white
##############################################################

            for i in range(len(grid)):
                if grid[i] != None and grid[i] != i:
                    if grid[i] == "X":
                        boxes[i].piece = x
                    else:
                        boxes[i].piece = o
                    boxes[i].taken = True

            if not game_end_check(grid):
                for box in boxes:
                    if box != None and box.taken and box.piece == None:
                        box.piece = turn
                        grid = change_grid(
                            box, get_var_name(turn).upper(), grid)

            for i in range(len(boxes)):
                box = boxes[i]
                if box != None and box.piece:
                    win.blit(box.piece, positions[i])

            if mos_y <= 600 and event.type == pygame.MOUSEBUTTONUP and move_made:
                computer_move()
                move_made = False

            if turn == x:
                message = ""
            else:
                message = "Turn: O"
            if game_end_check(grid):
                game_over = True
                message = game_end_check(grid)
            message = comicSans.render(message, False, (0, 0, 0))
            win.blit(message, (250, 615))

            if game_over:
                # Draws red line over winning streak
                if grid[1] == grid[2] == grid[3]:
                    pygame.draw.line(win, red, (0, 100), (600, 100), 4)
                if grid[4] == grid[5] == grid[6]:
                    pygame.draw.line(win, red, (0, 300), (600, 300), 4)
                if grid[7] == grid[8] == grid[9]:
                    pygame.draw.line(win, red, (0, 500), (600, 500), 4)
                if grid[1] == grid[4] == grid[7]:
                    pygame.draw.line(win, red, (100, 0), (100, 600), 4)
                if grid[2] == grid[5] == grid[8]:
                    pygame.draw.line(win, red, (300, 0), (300, 600), 4)
                if grid[3] == grid[6] == grid[9]:
                    pygame.draw.line(win, red, (500, 0), (500, 600), 4)
                if grid[1] == grid[5] == grid[9]:
                    pygame.draw.line(win, red, (0, 0), (600, 600), 4)
                if grid[3] == grid[5] == grid[7]:
                    pygame.draw.line(win, red, (600, 0), (0, 600), 4)

        pygame.display.update()
