import pygame
import random

# initialize pygame
pygame.init()

# set window dimensions and block size
WINDOW_SIZE = 600
BLOCK_SIZE = 25

# create screen and set caption
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Snake')

# create clock and set FPS
clock = pygame.time.Clock()
FPS = 12

# create fonts for score and level display
SCORE_FONT = pygame.font.SysFont("Verdana", 30)
LEVEL_FONT = pygame.font.SysFont("Verdana", 30)

# initialize game variables
level = 0
score = 0
running = True

# create Apple class for food object
class Apple:
    def __init__(self):
        self.x = int(random.randint(0, WINDOW_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, WINDOW_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, 'red', self.rect)

# create Snake class for player object
class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir, self.ydir = 1, 0
        self.body = [pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.head = self.body[0]
        self.dead = False

    def update(self):
        global level
        global score

        # check collision with body
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                screen.fill('red')
                game_over = SCORE_FONT.render("Game over", True, (0, 0, 0))
                screen.blit(game_over, (WINDOW_SIZE/2 - 80, WINDOW_SIZE/2))
                pygame.display.update()
                pygame.time.delay(2000)
                self.dead = True

        # check collision with walls
        if self.head.x < 0 or self.head.x >= WINDOW_SIZE or self.head.y < 0 or self.head.y >= WINDOW_SIZE:
            screen.fill('red')
            game_over = SCORE_FONT.render("Game over", True, (0, 0, 0))
            screen.blit(game_over, (WINDOW_SIZE/2 - 80, WINDOW_SIZE/2))
            pygame.display.update()
            pygame.time.delay(2000)
            self.dead = True

        # reset game if dead
        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple = Apple()
            score = 0
            level = 0

        # move snake
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

# create function to draw grid
def draw_grid():
    for x in range(0, WINDOW_SIZE, BLOCK_SIZE):
        for y in range(0, WINDOW_SIZE, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

# create objects and initialize game loop
apple = Apple()
snake = Snake()
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.xdir, snake.ydir = 0, -1
            elif event.key == pygame.K_DOWN:
                snake.xdir, snake.ydir = 0, 1
            elif event.key == pygame.K_LEFT:
                snake.xdir, snake.ydir = -1, 0
            elif event.key == pygame.K_RIGHT:
                snake.xdir, snake.ydir = 1, 0
   
    snake.update()
    screen.fill('black')
   
    score_count = SCORE_FONT.render(f"score: {score}", True, (0, 0, 255))
    screen.blit(score_count, (0, 0))
    level_count = LEVEL_FONT.render(f"level: {level}", True, (0, 0, 255))
    screen.blit(level_count, (WINDOW_SIZE - 200, 0))
    apple.update()
    pygame.draw.rect(screen, 'green', snake.head)

    for body in snake.body:
      pygame.draw.rect(screen, 'green', body)

    if snake.head.x == apple.x and snake.head.y == apple.y:
      snake.body.append(pygame.Rect(body.x, body.y,BLOCK_SIZE, BLOCK_SIZE))
      apple = Apple()
      score += 1
      if score % 5 == 0:
         FPS += 1
         level += 1
    
    clock.tick(FPS)
    pygame.display.update()