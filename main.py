import pygame
import random
from helpers import drawHitBox
from entities import enemy, player, bullet

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("my Game!")
icon = pygame.image.load("ship.png")
pygame.display.set_icon(icon)

#player
player = player(pygame.image.load("player.png"), 370, 480, 0, 0.3)
right_bound = 800 - player.img.get_width()

#enemy
num_of_enemies = 4
enemies = []
for i in range(num_of_enemies):
    i = enemy(pygame.image.load("ufo.png"), random.randint(0, 736), 50, 0.2, False, 0.3, 25)
    enemies.append(i)
print(enemies)

#bullet
bullet = bullet(pygame.image.load("bullet.png"), 0, player.img.get_height()/2 + 480, 0.4, 0, "ready")

#score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

lost = False

def show_score(x,y):
    score = font.render(f"Score: {score_value}", True, (255,255,255))
    screen.blit(score, (x,y))

def game_over():
    gg = font.render(f"GAME OVER Final score: {score_value}", True, (255,255,255))
    screen.blit(gg, (200, 200))

def win():
    gg = font.render(f"You win!", True, (255,255,255))
    screen.blit(gg, (330, 200))

#draws the player
def drawPlayer(x,y):
    screen.blit(player.img, (x,y))

#draws enemy
def enemy(x,y):
    for enemy1 in enemies:
        screen.blit(enemy1.img, (x,y))

#draw bullet
def fire_bullet(x,y):
    bullet.state = "moving"
    screen.blit(bullet.img, (x, y))

running = True

#game loop
while running:

    #set screen color using rgb
    screen.fill((0, 0, 0))

    #for loop to be able to quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -1 * player.speed
            if event.key == pygame.K_RIGHT:
                player.x_change = 1 * player.speed
            if event.key == pygame.K_SPACE and bullet.state is "ready":
                bullet.x = player.x + player.img.get_width()/2
                fire_bullet(bullet.x, bullet.y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player.x_change = 0

    #create screen bounds
    if player.x <= 0:
        player.x = 0
    if player.x >= right_bound:
        player.x = right_bound

    #enemy movement
    for enemy1 in enemies:
        if enemy1.x <= 0:
            enemy1.x_change = enemy1.speed
            enemy1.y += enemy1.y_change
        if enemy1.x >= right_bound:
            enemy1.x_change = -enemy1.speed
            enemy1.y += enemy1.y_change
        
        #drawHitBox(enemy1.x,enemy1.y, enemy1.img, screen)

        #updates enemy hitbox
        enemy1.hitbox = pygame.Rect(enemy1.x, enemy1.y, enemy1.img.get_width(), enemy1.img.get_height())

        #checks if bullet collided with enemy
        if enemy1.hitbox.collidepoint(bullet.x, bullet.y) and not enemy1.is_dead:
            bullet.state = "ready"
            bullet.y = player.img.get_height()/2 + 480
            score_value += 1
            enemy1.is_dead = True
            enemies.remove(enemy1)
        
        #game over
        if enemy1.y >= 440:
            enemies.clear()
            lost = True


    #bullet movement
    if bullet.state is "moving":
        fire_bullet(bullet.x, bullet.y)
        bullet.y -= bullet.speed
        if bullet.y <= 0:
            bullet.state = "ready"
            bullet.y = player.img.get_height()/2 + 480


    #drawHitBox(player.x,player.y, player.img, screen)
    #drawHitBox(bullet.x, bullet.y, bullet.img, screen)

    #moves sprites
    player.x += player.x_change
    for enemy1 in enemies:
        if not enemy1.is_dead:
            enemy1.x += enemy1.x_change
    

    #draw the sprites onto the screen
    drawPlayer(player.x ,player.y)
    for enemy1 in enemies:
        if not enemy1.is_dead:
            enemy(enemy1.x, enemy1.y)

    #shows score
    show_score(textX, textY)

    #game over
    if lost:
        game_over()

    #win
    if len(enemies) == 0:
        win()
    
    #update the screen
    pygame.display.update()