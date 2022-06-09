
import pygame
from pygame.locals import *
import time
import pygame_menu
XO = 'X'
pygame.init()
width = 400
height = 500

pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("D://my games//Tic tac toe//tictac.png")
icon = pygame.transform.scale(icon, (64, 64))
pygame.display.set_icon(icon)

draw_game = False
winner = None

screen = pygame.display.set_mode([width, height])
background = pygame.image.load("D://my games//Tic tac toe//board.png")
background_x = 0
background_y = 0
background = pygame.transform.scale(background, (400, 400))

# setting up a 3 * 3 board in canvas
TTT = [[None]*3, [None]*3, [None]*3]
x_img = pygame.image.load("D://my games////Tic tac toe//x.png")
x_img = pygame.transform.scale(x_img, (80, 80))

o_img = pygame.image.load("D://my games////Tic tac toe//o.png")
o_img = pygame.transform.scale(o_img, (80, 80))

white = (255, 255, 255)


def welcome():
    screen.blit(background, (0, 0))
    # Drawing vertical lines
    pygame.draw.line(screen, (0, 0, 0), (133, 0), (133, 400), 7)
    pygame.draw.line(screen, (0, 0, 0), (266, 0), (266, 400), 7)
    # Drawing horizontal lines
    pygame.draw.line(screen, (0, 0, 0), (0, 133), (400, 133), 7)
    pygame.draw.line(screen, (0, 0, 0), (0, 266), (400, 266), 7)
    pygame.display.update()
    draw_status()


def draw_status():
    # global message
    if (winner is not None):
        message = winner + " won !"

    else:
        message = XO + "'s turn"

    if(draw_game == True):
        message = "Game draw"
        time.sleep(2)
    won = pygame.font.Font('freesansbold.ttf', 32)
    won_text = won.render(message, True, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = won_text.get_rect(center=(200, 450))
    screen.blit(won_text, text_rect)
    pygame.display.update()


def check_winner():
    global TTT, winner, draw_game
    # check for winning rows
    for row in range(0, 3):
        if (TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] is not None):
            winner = TTT[row][0]  # this row wins
            if(row == 0):
                y0 = 70
            if(row == 1):
                y0 = 200
            if(row == 2):
                y0 = 335
            pygame.draw.line(screen, (250, 0, 0), (0, y0), (400, y0), 4)
            break

    # check for winning columns
    for col in range(0, 3):
        if (TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None):
            winner = TTT[0][col]  # this column won
            if(col == 0):
                x0 = 70

            if(col == 1):
                x0 = 200

            if(col == 2):
                x0 = 335

            pygame.draw.line(screen, (250, 0, 0), (x0, 0), (x0, 400), 4)
            break

    if(TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):  # for diagonally left to right
        winner = TTT[0][0]
        pygame.draw.line(screen, (255, 0, 0), (0, 0), (400, 400), 4)

    if(TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):  # for diagonally left to right
        winner = TTT[0][2]
        pygame.draw.line(screen, (255, 0, 0), (400, 0), (0, 400), 4)

    if(all([all(row) for row in TTT]) and winner is None):
        draw_game = True
    draw_status()


def draw_XO(row, col):
    global TTT, XO
    if row == 1:
        drawx = 30
    if row == 2:
        drawx = 163
    if row == 3:
        drawx = 296

    if col == 1:
        drawy = 30
    if col == 2:
        drawy = 163
    if col == 3:
        drawy = 296

    TTT[row-1][col-1] = XO  # for alternate chance for 'o' and 'x'

    if(XO == 'X'):
        screen.blit(x_img, (drawy, drawx))
        XO = 'O'
    else:
        screen.blit(o_img, (drawy, drawx))
        XO = 'X'
    pygame.display.update()


def coordinates(x, y):

    if(x < 133):
        col = 1
    elif (x < 266):
        col = 2
    elif(x < 400):
        col = 3
    else:
        col = None

    if(y < 133):
        row = 1
    elif (y < 266):
        row = 2
    elif(y < 400):
        row = 3
    else:
        row = None
    if(row and col and TTT[row-1][col-1] is None):
        global XO
        draw_XO(row, col)
        check_winner()


def reset_game():
    global XO, TTT, winner, draw_game
    time.sleep(2)
    XO = 'X'
    draw_game = None
    winner = None
    TTT = [[None]*3, [None]*3, [None]*3]
    welcome()


def loop():
    global XO, TTT, winner, draw_game
    welcome()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                # playerinputs()
                if event.key == pygame.K_KP_1:
                    x = 0
                    y = 0
                if event.key == pygame.K_KP_2:
                    x = 140
                    y = 0
                if event.key == pygame.K_KP_3:
                    x = 280
                    y = 0
                if event.key == pygame.K_KP_4:
                    x = 0
                    y = 140
                if event.key == pygame.K_KP_5:
                    x = 140
                    y = 140
                if event.key == pygame.K_KP_6:
                    x = 280
                    y = 140
                if event.key == pygame.K_KP_7:
                    x = 0
                    y = 280
                if event.key == pygame.K_KP_8:
                    x = 140
                    y = 280
                if event.key == pygame.K_KP_9:
                    x = 280
                    y = 280

                coordinates(x, y)
                if(winner or draw_game):
                    time.sleep(2)
                    XO = 'X'
                    TTT = [[None]*3, [None]*3, [None]*3]
                    draw_game = None
                    winner = None
                    menu.mainloop(screen)
          

                    # reset_game()

        pygame.display.update()


menu = pygame_menu.Menu('TIC-TAC-TOE', 400, 500,
                        theme=pygame_menu.themes.THEME_DARK)

image_path = pygame_menu.baseimage.IMAGE_EXAMPLE_PYGAME_MENU
menu.add.image(image_path, angle=0, scale=(0.15, 0.15))

menu.add.text_input('Name :', default=' ')
menu.add.text_input('Name :', default1=' ')
menu.add.button('Play', loop)
menu.add.button('Quit', pygame_menu.events.EXIT)


menu.mainloop(screen)
