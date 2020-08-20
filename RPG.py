import os
import random
import pygame
import sys
import math
import Enemi
# Variables
x = 50
y = 400
speed = 4
speed_run = 6.5
fps = 25
window_height = 500
window_width = 500
cant_run = False

red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()

#stamina
running = False
stamina = 100
stamina_max= 100
stamina_mid = 50
stamina_consumption = 1
stamina_regen = 1
stamina_walk_regen = .5

#helth
hp = 100
maxhp = 100
regenhp = 25

#character variables
mini = 0 
hngr = 0
hngr_max = 100
hngr_reduce = mini
thrst = 0
thrst_max = 100
thrst_reduce = mini
trist_damage = 2
hngr_damage = 2
double_damage = 4
hngr_rise = .15
tirst_rise = .1
hp_increace = 100


#Initialize Sprites

pygame.display.set_caption("Survivle RPG")
walkUp = [pygame.image.load('u1.png'), pygame.image.load('u2.png'), pygame.image.load('u3.png'), pygame.image.load('u4.png'), pygame.image.load('u5.png'), pygame.image.load('u6.png')]
walkDown = [pygame.image.load('d1.png'), pygame.image.load('d2.png'), pygame.image.load('d3.png'), pygame.image.load('d4.png'), pygame.image.load('d5.png'), pygame.image.load('d6.png')]
walkLeft = [pygame.image.load('l1.png'), pygame.image.load('l2.png'), pygame.image.load('l3.png'), pygame.image.load('l4.png'), pygame.image.load('l5.png'), pygame.image.load('l6.png')]
walkRight = [pygame.image.load('r1.png'), pygame.image.load('r2.png'), pygame.image.load('r3.png'), pygame.image.load('r4.png'), pygame.image.load('r5.png'), pygame.image.load('r6.png')]
char = pygame.image.load('d1.png')
#stamina sprite
sbar = [pygame.image.load('stamina1.png'), pygame.image.load('stamina2.png'), pygame.image.load('stamina4.png'), pygame.image.load('stamina6.png'), pygame.image.load('stamina7.png'), pygame.image.load('stamina9.png'), pygame.image.load('stamina10.png')]
#health sprite
hbar = [pygame.image.load('health1.png'), pygame.image.load('health2.png'), pygame.image.load('health3.png'), pygame.image.load('health4.png'), pygame.image.load('health5.png'), pygame.image.load('health6.png'), pygame.image.load('health7.png')]
#hungry sprite
hngrbar = [pygame.image.load('health1.png'), pygame.image.load('health2.png'), pygame.image.load('health3.png'), pygame.image.load('health4.png'), pygame.image.load('health5.png'), pygame.image.load('health6.png'), pygame.image.load('health7.png')]
#thirst sprite
tbar = [pygame.image.load('health1.png'), pygame.image.load('health2.png'), pygame.image.load('health3.png'), pygame.image.load('health4.png'), pygame.image.load('health5.png'), pygame.image.load('health6.png'), pygame.image.load('health7.png')]

# Class for the orange dude 

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Player, self).__init__()
        self.images_down = []
        self.images_up = []
        self.images_right = []
        self.images_left = []
        self.images_char = []

        
        self.images_down.append(pygame.image.load('d1.png'))
        self.images_down.append(pygame.image.load('d2.png'))
        self.images_down.append(pygame.image.load('d3.png'))
        self.images_down.append(pygame.image.load('d4.png'))
        self.images_down.append(pygame.image.load('d5.png'))
        self.images_down.append(pygame.image.load('d6.png'))  
                
        
        self.images_up.append(pygame.image.load('u1.png'))
        self.images_up.append(pygame.image.load('u2.png'))
        self.images_up.append(pygame.image.load('u3.png'))
        self.images_up.append(pygame.image.load('u4.png'))
        self.images_up.append(pygame.image.load('u5.png'))
        self.images_up.append(pygame.image.load('u6.png'))

        self.images_right.append(pygame.image.load('r1.png'))
        self.images_right.append(pygame.image.load('r2.png'))
        self.images_right.append(pygame.image.load('r3.png'))
        self.images_right.append(pygame.image.load('r4.png'))
        self.images_right.append(pygame.image.load('r5.png'))
        self.images_right.append(pygame.image.load('r6.png'))

        self.images_left.append(pygame.image.load('l1.png'))
        self.images_left.append(pygame.image.load('l2.png'))
        self.images_left.append(pygame.image.load('l3.png'))
        self.images_left.append(pygame.image.load('l4.png'))
        self.images_left.append(pygame.image.load('l5.png'))
        self.images_left.append(pygame.image.load('l6.png'))        

        self.images_char.append(pygame.image.load('d1.png'))
        

        
        self.index = 0
        self.image = self.images_down[self.index]
        self.rect = self.image.get_rect()
        self.hngr = hngr
        self.thrst = thrst
        self.hngr_max = hngr_max
        self.thist_max = thrst_max
    def update(self):
        self.index += 1
        if key[pygame.K_s]:
            if self.index >= len(self.images_down):
                self.index = 0
            self.image = self.images_down[self.index]
        elif key[pygame.K_a]:
            if self.index >= len(self.images_left):
                self.index = 0
            self.image = self.images_left[self.index]
        elif key[pygame.K_w]:
            if self.index >= len(self.images_up):
                self.index = 0
            self.image = self.images_up[self.index]
        elif key[pygame.K_d]:
            if self.index >= len(self.images_right):
                self.index = 0
            self.image = self.images_right[self.index]

        else:
            if self.index >= len(self.images_char):
                self.index = 0
            self.image = self.images_char[self.index]



        
    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
            
    def move_single_axis(self, dx, dy):
        global hngr, thrst, hp
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
        if pygame.sprite.collide_rect (player,food):
            food.rect.x = random.randint(20, 300)
            food.rect.y = random.randint(20, 300)
            hngr = hngr_reduce
            if hngr < 0:
                hngr = 0
            print("You consumed food")
            print (hngr)

        if pygame.sprite.collide_rect (player,water):
            water.rect.x = random.randint(20, 300)
            water.rect.y = random.randint(20, 300)
            thrst = thrst_reduce
            if thrst < 0:
                thrst = 0
            print("You consumed water")
            print (thrst)

        if pygame.sprite.collide_rect (player,medkit):
            medkit.rect.x = random.randint(20, 300)
            medkit.rect.y = random.randint(20, 300)
            hp = hp_increace
            if hp > 100:
                hp = 100
            print("You consumed a health pack")
            print (hp)
# Nice class to hold a wall rect

class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Enemy(object):
    def __init__(self,x,y):
        self.rect = pygame.Rect(300, 100, 32, 32)
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.vel = 3
    
    def move_towards_player(self,player, dx, dy):
        dx, dy = player.rect.x - player.rect.y, player.rect.y - self.rect.y
        dist =  math.hypot(dx, dy)
        dx, dy = dx / dis, dy /dist # Normalize vector
        self.rect.x += dx + self.speed
        self.rect.y += dy + self.speed


class Food(object):
    def __init__(self,x,y):
        self.rect = pygame.Rect(0,0,16,16)

        self.rect.x = x
        self.rect.y = y

class Water(object):

    def __init__(self, x, y):
        self.rect = pygame.Rect(0,0, 16, 16)

        self.rect.x = x
        self.rect.y = y

class Medkit(object):
    
    def __init__(self, x, y):
        self.rect = pygame.Rect(0,0, 16, 16)

        self.rect.x = x
        self.rect.y = y

        
        
# Initialise pygame


pygame.display.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
#initilizing window and backround

win = pygame.display.set_mode((window_height,window_width))
backdrop = pygame.image.load(os.path.join('bg.jpg')).convert()
backdropbox = win.get_rect()
walls = [] # List to hold the walls
player = Player() # Create the player
enemy = Enemy(150,100) 
food = Food(250,100)
water = Water(100,100)
medkit = Medkit(100, 150)
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group(player)
level = [



    

"                              W",
"                              W",
"                              W",
"                              W",
"                              W",
"                              W",
"                              W",
"                              W",
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
    
#Animations

def redrawGameWindow():
    
    # Stamina UI Animation  

    def animateUI(var,spr, pos):

        if var >= 95:
            win.blit(spr[6], (pos,10))
        elif var < 95 and var >= 70:
            win.blit(spr[5], (pos,10))
        elif var < 70 and var >= 56:
            win.blit(spr[4], (pos,10))
        elif var < 56 and var > 42:
            win.blit(spr[3], (pos,10))
        elif var < 42 and var > 28:
            win.blit(spr[2], (pos,10))
        elif var < 28 and var > 10:
            win.blit(spr[1], (pos,10))
        else:
            win.blit(spr[0], (pos,10))
    #health UI Animation
    animateUI(stamina, sbar, 20)
    animateUI(hp, hbar, 140)
    animateUI(hngr, hngrbar, 260)
    animateUI(thrst, tbar, 380)
    pygame.display.update()


counter = 0
run = True
while run:

    clock.tick(fps)
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
        player.move(-speed_run, 0)
        stamina -= stamina_consumption
        running = True
        
    elif key[pygame.K_d] and key[pygame.K_LSHIFT] and stamina >= 1 and cant_run == False:#run right
        player.move(speed_run, 0)
        stamina -= stamina_consumption
        running = True
        
    elif key[pygame.K_w] and key[pygame.K_LSHIFT] and stamina >= 1 and cant_run == False:#run up
        player.move(0, -speed_run)
        stamina -= stamina_consumption
        running = True

    elif key[pygame.K_s] and key[pygame.K_LSHIFT] and stamina >= 1 and cant_run == False:#run down
        player.move(0, speed_run)
        stamina -= stamina_consumption
        running = True

    elif key[pygame.K_a]:#walk left 
        player.move(-speed, 0)
        running = False
        if stamina < stamina_max and running == False:
            stamina += stamina_walk_regen
            if stamina <= stamina_mid:
                cant_run = True
            else:
                cant_run = False

    elif key[pygame.K_d]:#walk right
        player.move(speed, 0)
        running = False
        if stamina < stamina_max and running == False:
            stamina += stamina_walk_regen
            if stamina <= stamina_mid:
                cant_run = True
            else:
                cant_run = False
    elif key[pygame.K_w]:#walk up
        player.move(0, -speed)
        running = False
        if stamina < stamina_max and running == False:
            stamina += stamina_walk_regen
            if stamina <= stamina_mid:
                cant_run = True
            else:
                cant_run = False
    elif key[pygame.K_s]:#walk down
        player.move(0, speed)
        running = False
        if stamina < stamina_max and running == False:
            stamina += stamina_walk_regen
            if stamina <= stamina_mid:
                cant_run = True
            else:
                cant_run = False
    else:
        if stamina < stamina_max:
            stamina += stamina_regen
    #hunger and thirst bar
    if hngr < hngr_max:
        hngr += hngr_rise
        if running == True:
            hngr += hngr_rise*1.5
    elif hngr > hngr_max:
        hngr = hngr_max
    elif running == True and hngr < hngr_max:
        hngr += double_damage

    if thrst < thrst_max:
        thrst += tirst_rise
        if running == True:
            thrst += tirst_rise*1.5
    elif thrst > thrst_max:
        thrst = thrst_max
    # health bar

    if thrst == thrst_max:
        hp -= trist_damage                                      
    elif hngr == hngr_max:
        hp -= hngr_damage
    elif hngr == hngr_max and thrst == thrst_max:
        hp -= double_damage
        
    
    # Draw the scene
    player_list.update()
    player_list.draw(win) #draw the player
    #pygame.draw.rect(win, black, enemy)
    for wall in walls:
        pygame.draw.rect(win, blue , wall.rect)
    pygame.draw.rect(win, green, food)
    pygame.draw.rect(win, red, water)
    pygame.draw.rect(win, red, medkit)
    redrawGameWindow()
    pygame.display.flip()
    win.blit(backdrop, backdropbox)
