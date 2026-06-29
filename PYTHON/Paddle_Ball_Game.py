import pygame
import random
pygame.init()

screen_width = 400
screen_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
fps = 60
font = pygame.font.SysFont(None, 30)

GameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

def screen_text(text, colour, x, y):
    text_screen = font.render(text, True, colour)
    GameWindow.blit(text_screen, [x, y])

def gameloop():
    ball_size = 5
    ball_x = screen_width/2
    ball_y = screen_height/2
    plate_width = 30
    plate_height = 5
    plate_x = (screen_width - plate_width)/2
    plate_y = (screen_height - 50)
    game_end = False
    game_exit = False
    ball_vel_x = random.choice([-4,4])
    ball_vel_y = random.choice([-3,3])
    plate_vel_x = 0
    score = 0

    while not game_exit:
        if game_end:
            GameWindow.fill(black)
            screen_text("Press SPACE to restart", white, 95, 270)
            screen_text("press Q to quit", white, 125, 310)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_exit = True
                        gameloop()
                    if event.key == pygame.K_q:
                        game_exit = True
            pygame.display.update()
            clock.tick(fps)
        else:
            GameWindow.fill(black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        plate_vel_x = 4
                    if event.key == pygame.K_LEFT:
                        plate_vel_x = -4
            ball_x += ball_vel_x
            ball_y += ball_vel_y
            plate_x += plate_vel_x
            if (ball_x - ball_size) <= 0 or (ball_x + ball_size) >= screen_width:
                ball_vel_x = -ball_vel_x
            if (ball_y - ball_size) <= 0:
                ball_vel_y = -ball_vel_y
            if (ball_vel_y > 0 and ball_y + ball_size >= plate_y and ball_y - ball_size <= plate_y + plate_height and plate_x <= ball_x <= plate_x + plate_width):
                ball_vel_y = -ball_vel_y
                score += 1
                if score % 5 == 0:
                    ball_vel_x *= 1.2
                    ball_vel_y *= 1.2
            if ball_y >= screen_height:
                game_end = True
            
            plate_x = max(0, min(plate_x, screen_width - plate_width))
            
            screen_text("Score: " + str(score), white, 160, 5)
            pygame.draw.rect(GameWindow, white, (plate_x, plate_y, plate_width, plate_height))
            pygame.draw.circle(GameWindow, white, (int(ball_x), int(ball_y)), ball_size)
            pygame.display.update()
            clock.tick(fps)
    pygame.quit()
    quit()
gameloop()
