import pygame
import os
import random
from pygame.locals import *
# variables
test = pygame.Rect(300,100,50,50)
x = 50
y = 400
width = 64
height = 64
window_height = 500
window_width = 500
wall_size = 50
vel = 5
boost = 1.5
up = False
down = False
left = False
right = False
walkcount = 0
stamina = 100
health = 100
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#make windown
win = pygame.display.set_mode((window_height,window_width))
pygame.display.set_caption("Survivle RPG")
# animation

walkUp = [pygame.image.load('Sprites/characterup1.png'), pygame.image.load('Sprites/characterup2.png'), pygame.image.load('Sprites/characterup3.png'), pygame.image.load('Sprites/characterup4.png'), pygame.image.load('Sprites/characterup5.png'), pygame.image.load('Sprites/characterup6.png'), pygame.image.load('Sprites/characterup7.png'), pygame.image.load('Sprites/characterup8.png'), pygame.image.load('Sprites/characterup9.png')]
walkDown = [pygame.image.load('Sprites/character1.png'), pygame.image.load('Sprites/character2.png'), pygame.image.load('Sprites/character3.png'), pygame.image.load('Sprites/character4.png'), pygame.image.load('Sprites/character5.png'), pygame.image.load('Sprites/character6.png'), pygame.image.load('Sprites/character7.png'), pygame.image.load('Sprites/character8.png'), pygame.image.load('Sprites/character9.png')]
walkLeft = [pygame.image.load('Sprites/characterup1.png'), pygame.image.load('Sprites/characterup2.png'), pygame.image.load('Sprites/characterup3.png'), pygame.image.load('Sprites/characterup4.png'), pygame.image.load('Sprites/characterup5.png'), pygame.image.load('Sprites/characterup6.png'), pygame.image.load('Sprites/characterup7.png'), pygame.image.load('Sprites/characterup8.png'), pygame.image.load('Sprites/characterup9.png')]
walkRight = [pygame.image.load('Sprites/character1.png'), pygame.image.load('Sprites/character2.png'), pygame.image.load('Sprites/character3.png'), pygame.image.load('Sprites/character4.png'), pygame.image.load('Sprites/character5.png'), pygame.image.load('Sprites/character6.png'), pygame.image.load('Sprites/character7.png'), pygame.image.load('Sprites/character8.png'), pygame.image.load('Sprites/character9.png')]
char = pygame.image.load('Sprites/character.png')
#Bg = pygame.image.load('green.jpg')
sbar = [pygame.image.load('Sprites/stamina1.png'), pygame.image.load('Sprites/stamina2.png'), pygame.image.load('Sprites/stamina3.png'), pygame.image.load('Sprites/stamina4.png'), pygame.image.load('Sprites/stamina5.png'), pygame.image.load('Sprites/stamina6.png'), pygame.image.load('Sprites/stamina7.png'), pygame.image.load('Sprites/stamina8.png'), pygame.image.load('Sprites/stamina9.png'),pygame.image.load('Sprites/stamina10.png')]
hbar = [pygame.image.load('Sprites/health1.png'), pygame.image.load('Sprites/health2.png'), pygame.image.load('Sprites/health3.png'), pygame.image.load('Sprites/health4.png'), pygame.image.load('Sprites/health5.png'), pygame.image.load('Sprites/health6.png'), pygame.image.load('Sprites/health7.png')]
walls = []
player = Player()
for i in range(10):
    walls.append(pygame.Rect(random.randint(0, window_width - wall_size),
    random.randint(0,window_height - wall_size), wall_size, wall_size))
    
class Player(object):
    
    def move(self, dx, dy):
        



class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0],pos[1], 16, 16)


    
    
clock = pygame.time.Clock()
def redrawGameWindow():
    global walkcount
    

    if walkcount + 1 >= 27:
        walkcount = 0
    #drawing the animation for walking and running
    
        
    if left:
        win.blit(walkLeft[walkcount//3], (x,y))
        walkcount += 1
    elif right:
        win.blit(walkRight[walkcount//3], (x,y))
        walkcount += 1
    elif up:
        win.blit(walkUp[walkcount//3], (x,y))
        walkcount += 1
    elif down:
        win.blit(walkDown[walkcount//3], (x,y))
        walkcount += 1
    else:
        win.blit(char, (x,y))
        walkcount = 0
    #for when the stamina bar goes up or down 
    if stamina == 100:
        win.blit(sbar[9], (25,65))

    elif stamina < 100 and stamina >= 79:
        win.blit(sbar[8], (25,65))

    elif stamina < 79 and stamina >= 69:
        win.blit(sbar[7], (25,65))

    elif stamina < 69 and stamina >= 58:
        win.blit(sbar[6], (25,65))

    elif stamina < 58 and stamina >= 47:
        win.blit(sbar[5], (25,65))

    elif stamina < 47 and stamina >= 36:
        win.blit(sbar[4], (25,65))

    elif stamina < 36 and stamina >= 25:
        win.blit(sbar[3], (25,65))

    elif stamina < 25 and stamina >= 14:
        win.blit(sbar[2], (25,65))

    elif stamina < 14 and stamina >= 1:
        win.blit(sbar[1], (25,65))

    else:
        win.blit(sbar[0], (25,65))

    #health bar going down, or up

    if health == 100:
        win.blit(hbar[6], (25, 25))

    elif health < 100 and health >= 80:
        win.blit(hbar[5], (25,25))

    elif health < 80 and health >= 60:
        win.blit(hbar[4], (25,25))

    elif health < 60 and health >= 40:
        win.blit(hbar[3], (25,25))

    elif health < 40 and health >= 20:
        win.blit(hbar[2], (25,25))

    elif health < 20 and health >= 1:
        win.blit(hbar[1], (25,25))
        
    else:
        win.blit(hbar[0], (25,25))
        
    for i in range(len(walls)):
        pygame.draw.rect(win,blue,walls[i])
    pygame.draw.rect(win,red,test)

    pygame.display.update()
#making a while loop
run = True
while run:
    #speed of refreash
    clock.tick(16)
    #making code close if x is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    for wall in walls[:]:
        if test.colliderect(wall):
            walls.remove(wall)
    #useing keys to move in the code
    if keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
        if stamina > 10:
            y -= vel*boost 
            stamina -= 1
        left = False
        right = False
        up = True
        down = False
    elif keys[pygame.K_s] and keys[pygame.K_LSHIFT]:
        
        if stamina >= 1:
            y += vel*boost
            stamina -= 1
        left = False
        right = False
        up = False
        down = True
    elif keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
        
        if stamina >= 1:
            x -= vel*boost 
            stamina -= 1
        left = True
        right = False
        up = False
        down = False
    elif keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
        
        if stamina >= 1:
            x += vel*boost 
            stamina -= 1
        left = False
        right = True
        up = False
        down = False
    elif keys[pygame.K_a]:
        x -= vel
        left = True
        right = False
        up = False
        down = False
        if stamina < 100:
            stamina += 1
    elif keys[pygame.K_d]:
        x += vel
        left = False
        right = True
        up = False
        down = False
        if stamina < 100:
            stamina += 1
    elif keys[pygame.K_w]:
        y -= vel
        left = False
        right = False
        up = True
        down = False
        if stamina < 100:
            stamina += 1
    elif keys[pygame.K_s]:
        y += vel
        left = False 
        right = False
        up = False
        down = True
        if stamina < 100:
            stamina += 1
    else:
        left = False 
        right = False
        up = False
        down = False
        walkcount = 0
        if stamina < 100:
            stamina += 1
    win.fill(green)
    #calling redrawGameWindow function
    #giveing the leval color
        
    redrawGameWindow()
#end code
pygame.quit()
