import pygame
import random

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Bird
bird_x = 100
bird_y = 300
bird_radius = 15
gravity = 0.5
velocity = 0
jump = -8

# Pipes
pipe_width = 60
gap = 150
pipe_vel = 3
pipes = []

# Score
score = 0
font = pygame.font.SysFont(None, 40)

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

def create_pipe():
    height = random.randint(100, 400)
    return [WIDTH, height]

def move_pipes(pipes):
    for pipe in pipes:
        pipe[0] -= pipe_vel
    return [pipe for pipe in pipes if pipe[0] > -pipe_width]

def draw_pipes(pipes):
    for pipe in pipes:
        # Top pipe
        pygame.draw.rect(screen, GREEN, (pipe[0], 0, pipe_width, pipe[1]))
        # Bottom pipe
        pygame.draw.rect(screen, GREEN, (pipe[0], pipe[1] + gap, pipe_width, HEIGHT))

def check_collision(pipes):
    global bird_y
    for pipe in pipes:
        if bird_x + bird_radius > pipe[0] and bird_x - bird_radius < pipe[0] + pipe_width:
            if bird_y - bird_radius < pipe[1] or bird_y + bird_radius > pipe[1] + gap:
                return True
    if bird_y > HEIGHT or bird_y < 0:
        return True
    return False

def game_loop():
    global bird_y, velocity, score
    run = True
    frame = 0
    pipes.clear()
    bird_y = 300
    velocity = 0
    score = 0

    while run:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    velocity = jump

        # Bird movement
        velocity += gravity
        bird_y += velocity

        # Pipes
        if frame % 90 == 0:
            pipes.append(create_pipe())
        frame += 1

        pipes[:] = move_pipes(pipes)

        # Score
        for pipe in pipes:
            if pipe[0] == bird_x:
                score += 1

        # Draw
        draw_pipes(pipes)
        pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)
        draw_text("Score: " + str(score), 10, 10)

        # Collision
        if check_collision(pipes):
            draw_text("Game Over!", 120, 250)
            pygame.display.update()
            pygame.time.delay(2000)
            run = False

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_loop()
