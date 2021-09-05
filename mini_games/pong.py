import pygame
import random

pygame.init()
pygame.font.init()

WIDTH = 1080
HEIGHT = 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG game")

REC_WIDTH, REC_HEIGHT = 15, 200
BALL_WIDTH, BALL_HEIGHT = 30, 30

<<<<<<< HEAD
left_score = 0
right_score = 0

=======
>>>>>>> 094bf4bbec86c820af75a939ab611718526a11a3
SCORE_FONT = pygame.font.SysFont("Alt retro", 150)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FPS = 60

y_pos = random.randint(-150, 150)
x_pos = random.randint(2, 3)

x_direction = 1 if x_pos == 2 else -1
<<<<<<< HEAD
y_direction = y_pos / 100
opposite_y = y_direction
ball_vel = 3


def draw_win(left, right, ball):
    global left_score
    global right_score
    global y_direction
    global ball_vel
=======
y_direction = y_pos / 1000
opposite_y = 0 - y_direction
ball_vel = 2


def draw_win(left, right, ball, left_score=0, right_score=0):
>>>>>>> 094bf4bbec86c820af75a939ab611718526a11a3
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, left)
    pygame.draw.rect(WIN, WHITE, right)
    left_score_text = SCORE_FONT.render(str(left_score), 1, WHITE)
    right_score_text = SCORE_FONT.render(str(right_score), 1, WHITE)
<<<<<<< HEAD
    WIN.blit(left_score_text, (WIDTH / 2 - 125, 30))
    WIN.blit(right_score_text, (WIDTH / 2 + 50, 30))
    if ball.x >= WIDTH:
        left_score += 1
        if left_score == 5:
            print("Left wins !!!")
            exit()
        y_direction = random.randint(-150, 150) / 100
        ball_vel = 3
        main()
    if ball.x <= 0:
        right_score += 1
        if right_score == 5:
            print("Right wins !!!")
            exit()
        ball_vel = 3
        y_direction = random.randint(-150, 150) / 100
        main()
=======
    WIN.blit(left_score_text, (WIDTH / 2 - 50, 30))
    WIN.blit(right_score_text, (WIDTH / 2 + 50, 30))
    # pygame.draw.circle(WIN, WHITE, (ball.x / 2, ball.y / 2), BALL_WIDTH)
>>>>>>> 094bf4bbec86c820af75a939ab611718526a11a3
    pygame.draw.rect(WIN, WHITE, ball)
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
    ball,
    left,
    right,
    top_boarder,
    down_boarder,
<<<<<<< HEAD
=======
    ball_vel,
>>>>>>> 094bf4bbec86c820af75a939ab611718526a11a3
):
    global x_direction
    global y_direction
    global opposite_y
<<<<<<< HEAD
    global ball_vel

    if top_boarder.colliderect(ball):  # handle border collisions
        y_direction = -1 * y_direction
        ball_vel += 0.1

    if down_boarder.colliderect(ball):  # handle border collisions
        y_direction = -1 * y_direction
        ball_vel += 0.1
=======

    if top_boarder.colliderect(ball):  # handle border collisions
        y_direction = opposite_y

    if down_boarder.colliderect(ball):  # handle border collisions
        y_direction = opposite_y
>>>>>>> 094bf4bbec86c820af75a939ab611718526a11a3

    if left.colliderect(ball):  # handle rect collision
        x_direction = +1
        ball_vel += 0.1
        print(ball_vel)

    if right.colliderect(ball):
        x_direction = -1
        ball_vel += 0.1
        print(ball_vel)

    ball.x += x_direction * ball_vel
    ball.y += y_direction * ball_vel


def main():
    left = pygame.Rect(50, (HEIGHT - REC_HEIGHT) / 2, REC_WIDTH, REC_HEIGHT)
    right = pygame.Rect(WIDTH - 50, (HEIGHT - REC_HEIGHT) / 2, REC_WIDTH, REC_HEIGHT)
    ball = pygame.Rect(WIDTH / 2, HEIGHT / 2, BALL_WIDTH, BALL_HEIGHT)
    top_boarder = pygame.Rect(0, 0, WIDTH, 10)
    down_boarder = pygame.Rect(0, HEIGHT, WIDTH, 1)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        key_pressed = pygame.key.get_pressed()

        left_movement(key_pressed, left)
        right_movement(key_pressed, right)
        ball_movement(
            ball,
            left,
            right,
            top_boarder,
            down_boarder,
<<<<<<< HEAD
=======
            ball_vel,
>>>>>>> 094bf4bbec86c820af75a939ab611718526a11a3
        )
        draw_win(left, right, ball)


if __name__ == "__main__":
    main()
