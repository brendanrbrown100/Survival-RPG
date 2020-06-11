
import os

import random

import pygame

import sys

# Variables

test = pygame.Rect(300,100,50,50)

x = 50

y = 400

window_height = 500

window_width = 500

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

stamina = 100

health = 100

red = (255,0,0)

green = (0, 255, 0)

blue = (0, 0, 255)

black = (255, 255, 255)

clock = pygame.time.Clock()




#Initialize a Window

pygame.display.set_caption("Survivle RPG")

walkUp = [pygame.image.load('u1.png'), pygame.image.load('u2.png'), pygame.image.load('u3.png'), pygame.image.load('u4.png'), pygame.image.load('u5.png'), pygame.image.load('u6.png')]
walkDown = [pygame.image.load('d1.png'), pygame.image.load('d2.png'), pygame.image.load('d3.png'), pygame.image.load('d4.png'), pygame.image.load('d5.png'), pygame.image.load('d6.png')]
walkLeft = [pygame.image.load('l1.png'), pygame.image.load('l2.png'), pygame.image.load('l3.png'), pygame.image.load('l4.png'), pygame.image.load('l5.png'), pygame.image.load('l6.png')]
walkRight = [pygame.image.load('r1.png'), pygame.image.load('r2.png'), pygame.image.load('r3.png'), pygame.image.load('r4.png'), pygame.image.load('r5.png'), pygame.image.load('r6.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('d1.png')
sbar = [pygame.image.load('stamina1.png'), pygame.image.load('stamina2.png'), pygame.image.load('stamina3.png'), pygame.image.load('stamina4.png'), pygame.image.load('stamina5.png'), pygame.image.load('stamina6.png'), pygame.image.load('stamina7.png'), pygame.image.load('stamina8.png'), pygame.image.load('stamina9.png'), pygame.image.load('stamina10.png')]
hbar = [pygame.image.load('health1.png'), pygame.image.load('health2.png'), pygame.image.load('health3.png'), pygame.image.load('health4.png'), pygame.image.load('health5.png'), pygame.image.load('health6.png'), pygame.image.load('health7.png')]



# Class for the orange dude

class Player(pygame.sprite.Sprite):

    

    def __init__(self):

        #self.rect = pygame.Rect(50, 50, 16, 16)

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("d1.png")

        #img = [os.path.join('sprites', 'D1.png')].convert()

        #self.images.append(img)

        #self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.right = [pygame.image.load('r1.png'), pygame.image.load('r2.png'), pygame.image.load('r3.png'), pygame.image.load('r4.png'), pygame.image.load('r5.png'), pygame.image.load('r6.png')]
        self.left = [pygame.image.load('l1.png'), pygame.image.load('l2.png'), pygame.image.load('l3.png'), pygame.image.load('l4.png'), pygame.image.load('l5.png'), pygame.image.load('l6.png')]
        self.up =  [pygame.image.load('u1.png'), pygame.image.load('u2.png'), pygame.image.load('u3.png'), pygame.image.load('u4.png'), pygame.image.load('u5.png'), pygame.image.load('u6.png')]
        self.down = [pygame.image.load('d1.png'), pygame.image.load('d2.png'), pygame.image.load('d3.png'), pygame.image.load('d4.png'), pygame.image.load('d5.png'), pygame.image.load('d6.png')]


        



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

pygame.display.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()



win = pygame.display.set_mode((window_height,window_width))

backdrop = pygame.image.load(os.path.join('bg.jpg')).convert()

backdropbox = win.get_rect()



walls = [] # List to hold the walls

player = Player() # Create the player

player.rect.x = 0

player.rect.y = 0

player_list = pygame.sprite.Group()

player_list.add(player)


level = [

"              WWWWWWWWWWWWWWWW",

"                             W",

"W         WWWWWW             W",

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



#Animate Right, Left, Up, Down

def chooseDir():

    if key[pygame.K_a]:

        up = False

        down = False

        left = True

        right = False

        print("Moving left: " + str(left))

    elif key[pygame.K_d]:

        up = False

        down = False

        left = False

        right = True

        print("Moving right: " + str(right))

    elif key[pygame.K_w]:

        up = True

        down = False

        left = False

        right = False

        print("Moving up: " + str(up))

    elif key[pygame.K_s]:

        up = False

        down = True

        left = False

        right = False

        print("Moving down: " + str(down))

    else:

        up = False

        down = False

        left = False

        right = False

        print("Please Stand By")





#Animations

def redrawGameWindow():

    

    global walkcount



    if walkcount + 1 >= 16:

        walkcount = 0

    #Walking Animation



    if left:

        player_list.win.blit(walkLeft[walkcount//4], (x,y))

        walkcount += 1

    elif right:

        player_list.win.blit(walkRight[walkcount//4], (x,y))

        walkcount += 1

    elif up:

        player_list.win.blit(walkUp[walkcount//4], (x,y))

        walkcount += 1

    elif down:

        player_list.win.blit(walkDown[walkcount//4], (x,y))

        walkcount += 1

    else:

        win.blit(char, (x,y))

        walkcount = 0



    # Stamina UI Animation   

    

    if stamina >= 90:

        win.blit(sbar[9], (25,10))

        

    elif stamina < 90 and stamina >= 80:

        win.blit(sbar[8], (25,10))

        

    elif stamina < 80 and stamina >= 70:

        win.blit(sbar[7], (25,10))



    elif stamina < 70 and stamina >= 60:

        win.blit(sbar[6], (25,10))



    elif stamina < 60 and stamina >= 50:

        win.blit(sbar[5], (25,10))



    elif stamina < 50 and stamina >= 40:

        win.blit(sbar[4], (25,10))



    elif stamina < 40 and stamina > 30:

        win.blit(sbar[3], (25,10))

    elif stamina < 30 and stamina > 20:
        
        win.blit(sbar[2], (25,10))

    elif stamina < 20 and stamina > 10:
        
        win.blit(sbar[1], (25,10))

    else:

        win.blit(sbar[0], (25,10))



    pygame.display.update()

    



run = True

while run:



    #print(stamina)

    #print(cant_run)

    clock.tick(60)

    if stamina >= 100:

        cant_run = False

    

    for e in pygame.event.get():

        if e.type == pygame.QUIT:

            run = False

        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:

            run = False

    

    # Move the player if an arrow key is pressed

    key = pygame.key.get_pressed()

    if key[pygame.K_a] and key[pygame.K_LSHIFT] and stamina >= 1 and cant_run == False:#run left

        player.move(-3.5, 0)

        stamina -= .5

        running = True

        chooseDir()

    elif key[pygame.K_d] and key[pygame.K_LSHIFT] and stamina >= 1 and cant_run == False:#run right

        player.move(3.5, 0)

        stamina -= .5

        running = True

        chooseDir()

    elif key[pygame.K_w] and key[pygame.K_LSHIFT] and stamina >= 1 and cant_run == False:#run up

        player.move(0, -3.5)

        stamina -= .5

        running = True

        chooseDir()

    elif key[pygame.K_s] and key[pygame.K_LSHIFT] and stamina >= 1 and cant_run == False:#run down

        player.move(0, 3.5)

        stamina -= .5

        running = True

        chooseDir()

    elif key[pygame.K_a]:#walk left 

        player.move(-2, 0)

        running = False

        chooseDir()

        if stamina < 100 and running == False:

            stamina += .2

            if stamina <= 50:

                cant_run = True

            else:

                cant_run = False

    elif key[pygame.K_d]:#walk right

        player.move(2, 0)

        running = False

        chooseDir()

        if stamina < 80 and running == False:

            stamina += .2

            if stamina <= 40:

                cant_run = True

            else:

                cant_run = False

    elif key[pygame.K_w]:#walk up

        player.move(0, -2)

        running = False

        chooseDir()

        if stamina < 80 and running == False:

            stamina += .2

            if stamina <= 40:

                cant_run = True

            else:

                cant_run = False

    elif key[pygame.K_s]:#walk down

        player.move(0, 2)

        running = False

        chooseDir()

        if stamina < 80 and running == False:

            stamina += .2

            if stamina <= 40:

                cant_run = True

            else:

                cant_run = False

    else:

        if stamina < 80:

            stamina += 1

        chooseDir()

    

    # Draw the scene

    player_list.draw(win) #draw the player

    for wall in walls:

        pygame.draw.rect(win, black , wall.rect)

    redrawGameWindow()

    pygame.display.flip()

    win.blit(backdrop, backdropbox)
