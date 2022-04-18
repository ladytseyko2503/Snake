import pygame
import random

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

dis = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
snake = 10
def snake_1(snake, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], 10, 10])

def game():
    game_over = False

    x1 = 300
    y1 = 400

    x1_change = 0
    y1_change = 0

    snake_eat = []
    snake_len = 1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

        if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)


        pygame.draw.rect(dis, red, [70, 70, 10, 10])
        snake_food = []
        snake_food.append(x1)
        snake_food.append(y1)
        snake_eat.append(snake_food)
        if len(snake_eat) > snake_len:
            del snake_eat[0]

        for x in snake_eat[:-1]:
            if x == snake_food:
                game_over = True
        snake_1(snake, snake_eat)

        pygame.display.update()

        if x1 == 70 and y1 == 70:
            snake_len += 1

        clock.tick(10)

    pygame.quit()
    quit()


game()