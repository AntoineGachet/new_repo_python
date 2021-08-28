import pygame
import os
import random

pygame.init()

WIDTH = 1080
HEIGHT = 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG game")

REC_WIDTH, REC_HEIGHT = 15, 200
BALL_WIDTH, BALL_HEIGHT = 30, 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FPS = 60

y_pos = random.randint(-800, 800)
x_pos = random.randint(2, 3)

x_direction = 1  # if x_pos == 2 else 1
y_direction = 0  # y_pos/1000


def draw_win(left, right, ball, top_boarder, down_boarder):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, left)
    pygame.draw.rect(WIN, WHITE, right)
    pygame.draw.circle(WIN, WHITE, (ball.x / 2, ball.y / 2), BALL_WIDTH)
    pygame.draw.rect(WIN, WHITE, top_boarder)
    pygame.draw.rect(WIN, WHITE, down_boarder)
    # WIN.blit(BALL, (ball.x, ball.y))
    # WIN.blit(LEFT_RECTANGLE, (left.x, left.y))
    # WIN.blit(RIGHT_RECTANGLE, (right.x, right.y))
    pygame.display.update()


def right_movement(key_pressed, right):
    if key_pressed[pygame.K_UP]:  # right up
        right.y -= 5
    if right.y <= 0:
        right.y += 5
    if key_pressed[pygame.K_DOWN]:  # right down
        right.y += 5
    if right.y >= 720 - REC_HEIGHT:
        right.y -= 5
    else:
        pass


def left_movement(key_pressed, left):
    if key_pressed[pygame.K_z]:  # left up
        left.y -= 5
    if left.y <= 0:
        left.y += 5
    if key_pressed[pygame.K_s]:  # left down
        left.y += 5
    if left.y >= 720 - REC_HEIGHT:
        left.y -= 5


def ball_movement(
    ball, x_directionArg, y_directionArg, left, right, top_boarder, down_boarder
):
    global x_direction
    global y_direction

    ball_velocity = 3
    if top_boarder.colliderect(ball):  # handle border collisions
        y_direction = 0

    if down_boarder.colliderect(ball):  # handle border collisions
        y_direction = 0

    if left.colliderect(ball):  # handle rect collision
        x_direction = +1

    if right.colliderect(ball):
        x_direction = -1

    ball.x += x_direction * ball_velocity
    ball.y += y_direction * ball_velocity


def main():
    left = pygame.Rect(50, (HEIGHT - REC_HEIGHT) / 2, REC_WIDTH, REC_HEIGHT)
    right = pygame.Rect(WIDTH - 50, (HEIGHT - REC_HEIGHT) / 2, REC_WIDTH, REC_HEIGHT)
    ball = pygame.Rect(
        (WIDTH - BALL_WIDTH) / 2, (HEIGHT - BALL_HEIGHT) / 2, BALL_WIDTH, BALL_HEIGHT
    )
    top_boarder = pygame.Rect(0, 0, WIDTH, 10)
    pygame.draw.rect(WIN, WHITE, (top_boarder))

    down_boarder = pygame.Rect(0, HEIGHT, WIDTH, 1)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        print(left)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        key_pressed = pygame.key.get_pressed()

        left_movement(key_pressed, left)
        right_movement(key_pressed, right)
        ball_movement(
            ball, x_direction, y_direction, left, right, top_boarder, down_boarder
        )
        draw_win(left, right, ball, top_boarder, down_boarder)


if __name__ == "__main__":
    main()
