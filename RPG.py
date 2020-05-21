import os
import random
import pygame
# Variables
test = pygame.Rect(300,100,50,50)
x = 50
y = 400
window_height = 500
window_width = 480
wall_size = 50
width = 92
height = 92
vel = 5
boost = 1.5
up = False
down = False
left = False
right = False
shift = False
running = False
cant_run = False
walkcount = 0
stamina = 80
health = 100
red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (255, 255, 255)
clock = pygame.time.Clock()


#Initialize a Window
win = pygame.display.set_mode((window_height,window_width))
pygame.display.set_caption("Survivle RPG")
walkRight = [pygame.image.load('sprites/R1.png'), pygame.image.load('sprites/R2.png'), pygame.image.load('sprites/R3.png'), pygame.image.load('sprites/R4.png')]
walkLeft = [pygame.image.load('sprites/L1.png'), pygame.image.load('sprites/L2.png'), pygame.image.load('sprites/L3.png'), pygame.image.load('sprites/L4.png')]
walkUp = [pygame.image.load('sprites/character1.png'), pygame.image.load('sprites/U2.png'), pygame.image.load('sprites/U3.png'), pygame.image.load('sprites/U4.png')]
walkDown = [pygame.image.load('sprites/D1.png'), pygame.image.load('sprites/D2.png'), pygame.image.load('sprites/D3.png'), pygame.image.load('sprites/D4.png')]
bg = pygame.image.load('sprites/bg.png')
char = pygame.image.load('sprites/D1.png')
sbar = [pygame.image.loa5d('sprites/stamina1.png'), pygame.image.load('sprites/stamina2.png'), pygame.image.load('sprites/stamina3.png'), pygame.image.load('sprites/stamina4.png'), pygame.image.load('sprites/stamina5.png'), pygame.image.load('sprites/stamina6.png'), pygame.image.load('sprites/stamina7.png'), pygame.image.load('sprites/stamina8.png')]
hbar = [pygame.image.load('sprites/health1.png'), pygame.image.load('sprites/health2.png'), pygame.image.load('sprites/health3.png'), pygame.image.load('sprites/health4.png'), pygame.image.load('sprites/health5.png'), pygame.image.load('sprites/health6.png'), pygame.image.load('sprites/health7.png'), pygame.image.load('sprites/health8.png')]

# Class for the orange dude
class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
                # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

# Nice class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

walls = [] # List to hold the walls
player = Player() # Create the player
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                            W",
"W         WWWWWW             W",
"W   WWWW       W             W",
"W   WWWW       W             W",
"W   WWWW       W             W",
"W   WWWW       W             W",
"W   WWWW       W             W",
"W   WWWW       W             W",
"W   WWWW       W             W",
"W   WWWW       W             W",
"W   WWWW       W             W",
"W   WWWW       W             W",
"W   WWWW       W             W",
"W   WWWW       W             W",
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        x += 16
    y += 16
    x = 0
#animation
#def redrawGameWindow():
    #win.blit(bg, (0,0))
    
    


run = True
while run:
    
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
    
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    #run left
    if key[pygame.K_a] and key[pygame.K_LSHIFT] and stamina > 1 and cant_run == False:
        player.move(-3.5,0)
        stamina -= .5
        running = True
    #run right
    elif key[pygame.K_d] and key[pygame.K_LSHIFT] and stamina > 1 and cant_run == False:
        player.move(3.5,0)
        stamina -= .5
        running = True
    #run up
    elif key[pygame.K_w] and key[pygame.K_LSHIFT] and stamina > 1 and cant_run == False:
        player.move(0, -3.5)
        stamina -= .5
        running = True
    #run down
    elif key[pygame.K_s] and key[pygame.K_LSHIFT] and stamina > 1 and cant_run == False:
        player.move(0,3.5)
        stamina -= .5
        running = True
    #walk left
    elif key[pygame.K_a]:
        player.move(-2, 0)
        running = False
        if stamina < 80 and running == False:
            stamina += .5
            if stamina <= 40:
                cant_run = True
            else:
                cant_run = False
    #walk right
    elif key[pygame.K_d]:
        player.move(2, 0)
        running = False
        if stamina < 80 and running == False:
            stamina += .5
            if stamina <= 40:
                cant_run = True
            else:
                cant_run = False
                
    #walk up
    elif key[pygame.K_w]:
        player.move(0, -2)
        running = False
        if stamina < 80 and running == False:
            stamina += .5
            if stamina <= 40:
                cant_run = True
            else:
                cant_run = False
    #walk down
    elif key[pygame.K_s]:
        player.move(0, 2)
        running = False
        if stamina < 80:
            stamina += .1
            if stamina <= 40:
                cant_run = True
            else:
                cant_run = False
  
    
    else:
        if stamina < 80:
            stamina += 1
            if stamina <= 40:
                running = False
        
    # Draw the scene
    win.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(win, black , wall.rect)
    pygame.draw.rect(win,green, player.rect)
    pygame.display.flip()
    #redrawGameWindow()

pygame.quit()
