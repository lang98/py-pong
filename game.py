import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

# screen
size = 1000, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pong!')

# paddle
paddle_size = 100, 20
paddle_rect_x = size[0] / 2
paddle_rect_y = size[1] - 100

# ball
ball_rect_x = size[0] / 2
ball_rect_y = size[1] / 2
ball_size = 20
ball_speed_x = 5
ball_speed_y = 5

# score
score = 0


def update_paddle(x, y):
    if x < 0:
        x = 0
    if x > size[0] - paddle_size[0]:
        x = size[0] - paddle_size[0]
    pygame.draw.rect(screen, WHITE, [x, y, paddle_size[0], paddle_size[1]])


def update_ball(x, y):
    global ball_speed_x, ball_speed_y
    global paddle_rect_x, paddle_rect_y
    global score

    if x < 0 or x > size[0]:
        ball_speed_x = -ball_speed_x
    if y < 0 or y > size[1]:
        ball_speed_y = -ball_speed_y
    if y > paddle_rect_y - ball_size and paddle_rect_x < x < paddle_rect_x + paddle_size[0]:
        ball_speed_y = -ball_speed_y
        score += 1
    pygame.draw.rect(screen, WHITE, [x, y, ball_size, ball_size])


# Game loop


done = False
clock = pygame.time.Clock()

while not done:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            paddle_rect_x = event.pos[0]

    ball_rect_x += ball_speed_x
    ball_rect_y += ball_speed_y

    update_paddle(paddle_rect_x, paddle_rect_y)
    update_ball(ball_rect_x, ball_rect_y)

    # score
    font = pygame.font.SysFont('Calibri', 20)
    text = font.render('Score: ' + str(score), True, WHITE)
    screen.blit(text, [size[0] - 100, size[1] - 50])

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
