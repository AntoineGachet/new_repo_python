import pygame
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

# x_direction = -1  # if x_pos == 2 else 1
# y_direction = -0.8  # y_pos/1000


class Ball:
    def __init__(self):
        self.y_direction = random.randint(-800, 800) / 100
        self.x_direction = 1 if random.randint(2, 3) == 2 else 3
        self.ball_vel = 1
        self.ball = pygame.Rect(
            (WIDTH - BALL_WIDTH) / 2,
            (HEIGHT - BALL_HEIGHT) / 2,
            BALL_WIDTH,
            BALL_HEIGHT / 2,
        )

    def ball_movement(self, left, right, top_boarder, bottom_boarder):

        if self.ball.colliderect(left) or self.ball.colliderect(
            right
        ):  # handle bordures collision
            self.x_direction = -self.x_direction
        if self.ball.colliderect(top_boarder) or self.ball.colliderect(
            bottom_boarder
        ):  # handle paddle collision
            self.y_direction = -self.y_direction

        self.ball.x += self.x_direction * self.ball_vel
        self.ball.y += self.y_direction * self.ball_vel
        self.ball_vel += 0.1


def draw_win(left, right):

    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, left)
    pygame.draw.rect(WIN, WHITE, right)
    pygame.draw.circle(WIN, WHITE, (Ball.ball.x / 2, Ball.ball.y / 2), BALL_WIDTH)
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


def main():
    left = pygame.Rect(50, (HEIGHT - REC_HEIGHT) / 2, REC_WIDTH, REC_HEIGHT)
    right = pygame.Rect(WIDTH - 50, (HEIGHT - REC_HEIGHT) / 2, REC_WIDTH, REC_HEIGHT)

    top_boarder = pygame.Rect(0, 0, WIDTH, 10)
    pygame.draw.rect(WIN, WHITE, (top_boarder))

    bottom_boarder = pygame.Rect(0, HEIGHT, WIDTH, 1)
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
        ball = Ball()
        ball.ball_movement(left, right, top_boarder, bottom_boarder)
        draw_win(left, right)


if __name__ == "__main__":
    main()
