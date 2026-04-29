# Author : El Khattabi Imad
# Date: 28.04.2026
# Version : 1.5


import pygame

from Player import Player
from Camera import Camera
from Enemy import Enemy

pygame.init()

#================
# Window
#================
Width, Height = 800, 700
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Chroniques du Kraken oublié")


#==================
# Background
#==================
background_1 = pygame.image.load('Design/Backgrounds/background_1.png')
background_1 = pygame.transform.scale(background_1, (1900, 1200))
map_width = background_1.get_width()
map_height = background_1.get_height()

current_map = background_1
#==================
# Player
#==================
folder_player = "./Design/Player/Moves"
player = Player(screen, folder_player)

#==================
# Enemys
#==================
folder_enemy = "./Design/Enemys/octopus.png"
enemy = Enemy(screen, "octopus", folder_enemy,800,400, 120)
enemies = [enemy]

#=================
# Camera
#=================
camera = Camera()


#==================
# Main Loop
#==================
clock = pygame.time.Clock()
running = True
e_pressed = False

while running:
    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.blit(current_map, (-camera.x, -camera.y))
    player.update(keys,map_width, map_height,current_map,enemies)
    enemy.move(player,current_map)
    camera.update(player, Width, Height, map_width, map_height)



    enemy.draw(screen,camera)
    player.draw(screen, camera)
    player.show_hp()

    pygame.display.flip()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()