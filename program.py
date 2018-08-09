from random import randint 
import pygame
import sys, os
from time import sleep
from tkinter import Tk, Text, Label, Button, END
import start

blue = (100, 100, 255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
brun = (170, 85, 0)
orange = (255, 72.8, 36.4)
purple = (51, 0, 255)
size = 800
player_i = ''

def player(def_player): 
    screen_text = font.render(str(def_player), True, black)
    game_display.blit(screen_text, [350, 10])
    pygame.display.update()

def snake(speed, snake_list):
    for X_Y in snake_list:
        pygame.draw.rect(game_display, green, [X_Y[0], X_Y[1], 10, 10])
        
def snake_cub(speed, snake_cub_list):
    for X_Y in snake_cub_list:
        pygame.draw.rect(game_display, green, [X_Y[0], X_Y[1], 10, 10])

def message(msg, color, x_coor, y_coor):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [x_coor, y_coor])
    pygame.display.update()
    
def cub_score_message(cub_score):
    screen_text = font.render('AI`s score: ' + str(cub_score), True, black)
    game_display.blit(screen_text, [680, 10])
    pygame.display.update()
    
def player_score(def_player, score):
    screen_text = font.render(def_player + '`s score: ' + str(score), True, black)
    game_display.blit(screen_text, [10, 10])
    pygame.display.update()
    
def game_init():
    global clock, font, game_display
    pygame.init()
    pygame.display.set_caption('Kyky')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 25)
    game_display = pygame.display.set_mode((size, size))
    
def close_name_window():
    window.destroy()
    quit()
    
def button_click():
    global player_i, snake_length, mode, snake_speed, min_cub_move_speed, max_cub_move_speed
    mode = ''
    player_i = textBox.get(1.0, END + "-1c")
    
    print(player_i)
    
    if str_mode == 'Normal':
        max_cub_move_speed = 10
        min_cub_move_speed = -10
        snake_speed = 10
        mode = 'Normal'
        print(mode)
        if len(player_i.strip()) != 0:
            window.destroy()
            game_init()
            start.loop(size, player_i, min_cub_move_speed,
                max_cub_move_speed, game_display, mode, 
                clock, snake_speed)
    elif str_mode == 'Easy':
        max_cub_move_speed = 4
        min_cub_move_speed = -4
        snake_speed = 4
        mode = 'Easy'
        print(mode)
        if len(player_i.strip()) != 0:
            window.destroy()
            game_init()
            start.loop(size, player_i, min_cub_move_speed,
                max_cub_move_speed, game_display, mode, 
                clock, snake_speed)

    
def btn_mode_click():
    global str_mode
    if str_mode == 'Normal':
        str_mode = 'Easy'
    else:
        str_mode = 'Normal'
        
    btn_mode.configure(text = str_mode)
    
    
def name_window():
    global label, textBox, btn, window
    global close_btn, w_label, str_mode, btn_mode
    
    window = Tk()
    window.title('Ky')
    str_mode = 'Normal'
    
    w_label = Label(window, text = 'You need a name.')
    label = Label(window, text='               What is you name?              ')
    textBox = Text(window, width = 10, height = 1)
    
    mode_label = Label(window, text = 'Select game mode:')
    help_label1 = Label(window, text = 'Normal, ')
    help_label2 = Label(window, text = 'Easy.')
    btn_mode = Button(window, text = str_mode, command = btn_mode_click)
    
    btn = Button(window, text = 'Enter', command = button_click)
    close_btn = Button(window, text = 'Exit', command = close_name_window)
    
    w_label.pack()
    label.pack()
    textBox.pack()
    mode_label.pack()
    help_label1.pack()
    help_label2.pack()
    btn_mode.pack()
    btn.pack()
    close_btn.pack()

name_window()

def save_exit(player_i, save_score, save_cub_score):
    path = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\Score.txt'
    print(path)
    f = open(path, "w")
    f.write('Last ' + player_i + '`s' + ' score: '+ str(save_score) + ', AI`s score: ' + str(save_cub_score) + '\n')
    f.close()
    pygame.quit()
    quit()
    
    
    
    
    