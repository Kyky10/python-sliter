from random import randint 
import pygame
from time import sleep
import program

blue = (100, 100, 255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
brun = (170, 85, 0)
orange = (255, 72.8, 36.4)
background = (200, 255, 255)
purple = (51, 0, 255)
score = 0
cub_score = 0

def loop(size, player_i,min_cub_move_speed, 
    max_cub_move_speed, game_display, mode,
    clock, snake_speed):
    
    global score, cub_score

    snake_length = 1
    snake_list = []
    snake_cub_length = 1
    snake_cub_list = []
    #sn_id = []

    x_apple = round(randint(0, size - 30)/10.0)*10.0
    y_apple = round(randint(0, size - 30)/10.0)*10.0

    x = size / 2
    y = size / 2
    x_cub = 500
    y_cub = 400
    x_change = 0
    y_change = 0
    x_change_cub = 0
    y_change_cub = 0
    
    speed = 5
    
    FPS = 60
    
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = - speed
                    #x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = speed
                    #x_change = 0
                elif event.key == pygame.K_LEFT:
                    x_change = - speed
                    #y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = speed
                    #y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0 
                    
            
        mustChange  = (randint(0, 30) == 1)
        mustStop = (randint(0, 280) == 1)
        y_cub_y_apple = (y_cub == y_apple or y_cub == y_apple + 5 or y_cub == y_apple - 5)
        x_cub_x_apple = (x_cub == x_apple or x_cub == x_apple + 5 or x_cub == x_apple - 5)
        
            
        if x > size:
            x_change = - speed
        elif x < 0:
            x_change = speed
        elif y > size:
            y_change = - speed
        elif y < 0:
            y_change = speed
    
        elif x_cub >= size:
            x_change_cub = - snake_speed
        elif x_cub <= 0:
            x_change_cub = snake_speed
        elif y_cub >= size:
            y_change_cub = - snake_speed
        elif y_cub <= 0:
            y_change_cub = snake_speed
        
        elif y_cub_y_apple:
            y_change_cub = 0
            if x_cub <= x_apple: 
                x_change_cub = int(max_cub_move_speed)
            elif x_cub >= x_apple:
                x_change_cub = - int(max_cub_move_speed)
            mustChange = (0 == 1)
            mustStop = (0 == 1)
        elif x_cub_x_apple:
            x_change_cub = 0
            if y_cub <= y_apple: 
                y_change_cub = int(max_cub_move_speed)
            elif y_cub >= y_apple:
                y_change_cub = - int(max_cub_move_speed)
            mustChange = (0 == 1)
            mustStop = (0 == 1)
        elif mustChange:
            y_change_cub = randint(min_cub_move_speed, max_cub_move_speed)
            x_change_cub = randint(min_cub_move_speed, max_cub_move_speed)
        elif mustStop:
            x_change_cub = y_change_cub = 0
        
        x_cub += x_change_cub
        y_cub += y_change_cub
        x += x_change
        y += y_change
    
        game_display.fill(background)
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        program.snake(speed, snake_list)

        snake_cub_head = []
        snake_cub_head.append(x_cub)
        snake_cub_head.append(y_cub)
        snake_cub_list.append(snake_cub_head)
        if len(snake_cub_list) > snake_cub_length:
            del snake_cub_list[0]
        program.snake_cub(speed, snake_cub_list)
        
        pygame.draw.rect(game_display, green, [x, y, 10, 10])
        pygame.draw.rect(game_display, red, [x_cub, y_cub, 10, 10])
        pygame.draw.rect(game_display, brun, [x_apple + 3, y_apple + -5 , 4, 10 ])
        pygame.draw.rect(game_display, green, [x_apple, y_apple - 8, 5, 5])
        pygame.draw.rect(game_display, purple, [x_apple, y_apple, 10, 10])
        pygame.display.update()
        if  (x >= x_apple - 5 
            and x <= x_apple + 5 
            and y >= y_apple - 5
            and y <= y_apple + 5):
            snake_length += 1
            score = snake_length - 1
            program.message('like a boss', green, x_apple + 16, y_apple)
            program.message('like a boss', green, x_apple + 16, y_apple)
            program.message('like a boss', green, x_apple + 16, y_apple)
            program.message('like a boss', green, x_apple + 16, y_apple)
            print(player_i + '`s score: ' + str(score))
            x_apple = round(randint(0, size - 10)/10.0)*10.0
            y_apple = round(randint(0, size - 10)/10.0)*10.0
        elif (x_cub >= x_apple - 5
            and x_cub <= x_apple + 5 
            and y_cub >= y_apple - 5
            and y_cub <= y_apple + 5):
            snake_cub_length += 1
            cub_score = snake_cub_length - 1
            print('AI`s score: ' + str(cub_score))
            program.message('like a noob', black, x_apple + 16, y_apple)
            program.message('like a noob', black, x_apple + 16, y_apple)
            program.message('like a noob', black, x_apple + 16, y_apple)
            program.message('like a noob', black, x_apple + 16, y_apple)
            x_apple = round(randint(0, size - 30)/10.0)*10.0
            y_apple = round(randint(0, size - 30)/10.0)*10.0
            
        program.player_score(player_i, score)
        program.cub_score_message(cub_score)
        program.player(player_i + ' on ' + mode)
        clock.tick(FPS)
    if score > cub_score:
        game_display.fill(white)
        pygame.display.update()
        mes = 'You WIN!!!'
        program.message(mes, green, 370, size/2)
        pygame.display.update()
        sleep(0.9)
    elif score < cub_score:
        game_display.fill(black)
        mes = 'You lose.'
        program.message(mes, red, 370, size/2)
        sleep(0.9)
        pygame.display.update()
    else:
        mes = 'Tie'
        program.message(mes, white, 370, size/2)
        sleep(0.9)
    game_display.fill(blue)
    sleep(0.9)
    program.message('Closing the game... Your score: ' + str(score) + ', AI`s score: ' + str(cub_score), white, 250, size/2)
    program.save_exit(player_i, score, cub_score)