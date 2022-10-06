import pygame, random
from sys import exit
from copy import deepcopy
pygame.init()

def newFood():
    global food, grid
    grid[food[0]][food[1]] = 0
    r = True
    while r:
        a = random.randint(0, 11)
        b = random.randint(0, 17)
        if grid[a][b] == 0:
            grid[a][b] = 3
            food = [a,b]
            r = False

def move(direction):
    global grid, snake_body, food, game
    eat = False
    head = [deepcopy(snake_body[-1][0]), deepcopy(snake_body[-1][1])]
    grid[head[0]][head[1]] = 1
    if head[0]+direction[0] < 0:
        head[0] = 11
    elif head[0]+direction[0] > 11:
        head[0] = 0
    else:
        head[0] += direction[0]
    if head[1]+direction[1] < 0:
        head[1] = 17
    elif head[1]+direction[1] > 17:
        head[1] = 0
    else:
        head[1] += direction[1]

    for i in snake_body:
        if head == i:
            game = 'failed'
    
    eat = False
    if head == food:
        eat = True
        newFood()
        
    w = len(grid[0])
    h = len(grid)

    grid[head[0]][head[1]] = 2
    grid[snake_body[0][0]][snake_body[0][1]] = 0
    snake_body.append([head[0], head[1]])
    if not eat: snake_body.pop(0)

def draw_grid(grid, screen):
    for i in range(0, len(grid)):
        for o in range(0, len(grid[0])):
            if grid[i][o] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (o*60+2, i*60+2, 56, 56))
            elif grid[i][o] == 2:
                pygame.draw.rect(screen, (255, 0, 0), (o*60+2, i*60+2, 56, 56))
            elif grid[i][o] == 3:
                pygame.draw.rect(screen, (0, 255, 0), (o*60+2, i*60+2, 56, 56))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (o*60+2, i*60+2, 56, 56))



directions = {
    'right': [0, 1], #right
    'left': [0, -1], #left
    'up': [-1, 0], #up
    'down': [1, 0], #down
    }

snake_direction = directions['up']
food = [2,2]
grid = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]

snake_body = [[8,10],[7,10],[6,10]]
game = 'inplay'
w = len(grid[0])*60
h = len(grid)*60
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
running = 1
while running:
    clicked = True
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and snake_direction != [1, 0] and clicked:
                snake_direction = directions['up']
                clicked = False
            elif e.key == pygame.K_DOWN and snake_direction != [-1, 0] and clicked:
                snake_direction = directions['down']
                clicked = False
            elif e.key == pygame.K_LEFT and snake_direction != [0, 1] and clicked:
                snake_direction = directions['left']
                clicked = False
            elif e.key == pygame.K_RIGHT and snake_direction != [0, -1] and clicked:
                snake_direction = directions['right']
                clicked = False
                
    screen.fill((0, 0, 0))
    move(snake_direction)
    draw_grid(grid, screen)

    if game == 'failed':
        running = False
    
    pygame.display.update()
    clock.tick(7)
while True:
    screen.fill((69, 69, 69))
    font = pygame.font.Font('freesansbold.ttf', 100) 
    text = font.render('haha you lost', True, (255, 0, 0)) 
    textRect = text.get_rect()
    textRect.center = (w/2, h/2)
    screen.blit(text, textRect)
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
