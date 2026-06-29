# initialising the game
import pygame
import random
pygame.init()

# defining colours
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 150, 0)

screen_width = 500
screen_height = 500

font = pygame.font.SysFont(None, 35)

# function to print score on screen
def screen_text(text, colour, x, y):
    text_screen = font.render(text, True, colour)
    GameWindow.blit(text_screen, [x, y])

# function to draw snake
def plot_snake(GameWindow, colour, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(GameWindow, colour, [x, y, snake_size, snake_size])

# initialising game clock
clock = pygame.time.Clock()

# creating game window
GameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snakes")

def gameloop():

    # game specific variables
    game_exit = False
    game_over = False

    snake_size = 20
    snake_speed = snake_size
    fps = 8

    snake_x = (screen_width // 2 // snake_size) * snake_size
    snake_y = (screen_height // 2 // snake_size) * snake_size

    velocity_x = 0
    velocity_y = 0

    score = 0
    snake_list = []
    snake_length = 1

    food_x = random.randint(0, (screen_width - snake_size)//snake_size) * snake_size
    food_y = random.randint(0, (screen_height - snake_size)//snake_size) * snake_size

    while not game_exit:

        if game_over:
            GameWindow.fill(green)
            screen_text("Game Over! Press Enter to Restart", red, 60, 250)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = snake_speed
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -snake_speed
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -snake_speed
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = snake_speed
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            # Boundary collision (corrected)
            if (snake_x < 0 or 
                snake_x > screen_width - snake_size or 
                snake_y < 0 or 
                snake_y > screen_height - snake_size):
                game_over = True

            # Food collision
            if snake_x == food_x and snake_y == food_y:
                score += 1
                snake_length += 1
                food_x = random.randint(0, (screen_width - snake_size)//snake_size) * snake_size
                food_y = random.randint(0, (screen_height - snake_size)//snake_size) * snake_size

            GameWindow.fill(green)

            # Draw visible boundary
            pygame.draw.rect(GameWindow, white, [0, 0, screen_width, screen_height], 3)

            screen_text("Score: " + str(score * 10), white, 200, 5)
            pygame.draw.rect(GameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snake_list.append(head)

            # Self collision
            if snake_length > 1 and head in snake_list[:-1]:
                game_over = True

            if len(snake_list) > snake_length:
                del snake_list[0]

            plot_snake(GameWindow, blue, snake_list, snake_size)

            pygame.display.update()
            clock.tick(fps)

    pygame.quit()
    quit()

gameloop()