import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Red ball")

# Set up the ball
ball_size = 50
ball_radius = 25
ball_color = (255, 0, 0)
ball_x = screen_width // 2
ball_y = screen_height // 2

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y -= 20
            elif event.key == pygame.K_DOWN:
                ball_y += 20
            elif event.key == pygame.K_LEFT:
                ball_x -= 20
            elif event.key == pygame.K_RIGHT:
                ball_x += 20
    
    # Keep the ball inside the screen
    if ball_x < ball_radius:
        ball_x = ball_radius
    elif ball_x > screen_width - ball_radius:
        ball_x = screen_width - ball_radius
    if ball_y < ball_radius:
        ball_y = ball_radius
    elif ball_y > screen_height - ball_radius:
        ball_y = screen_height - ball_radius
    
    # Draw the screen
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.update()
    
    # Set the frame rate
    clock.tick(60)