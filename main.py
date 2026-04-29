# Author : El Khattabi Imad
# Date: 28.04.2026
# Version : 1.5


import pygame
from pygame.display import get_surface

from Player import Player
from Camera import Camera
from Enemy import Enemy
from Map import Map

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
background_1 = pygame.image.load('assets/Backgrounds/background_1.png')
background_1 = pygame.transform.scale(background_1, (1900, 1200))

background_2 = pygame.image.load('assets/Backgrounds/background_2.png')
background_2 = pygame.transform.scale(background_2, (1900, 1200))




#==================
# Damage effect
#==================
damage_image = pygame.image.load('assets/effect/slash.png')
damage_image = pygame.transform.scale(damage_image, (100, 100))


#==================
# Player
#==================
folder_player = "./assets/Player"
player = Player(screen, folder_player)
player.damage_image = damage_image

#==================
# Enemys
#==================
folder_enemy = "./assets/Enemys/octopus.png"
enemy = Enemy(screen, "octopus", folder_enemy,1200,700, 120)
enemies = [enemy]

#=========================
# Maps
#========================
map_1 = Map(1900, 1200, background_1,"map_1",[])
map_2 = Map(1900, 1200, background_2,"map_2",[enemy])
maps = [map_1, map_2]
current_map = map_1

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

    current_map.draw(screen, camera)
    player.update(keys,current_map.width, current_map.height, current_map.get_surface(),enemies)
    current_map = Map.switch_map(current_map, player, map_1, map_2)
    camera.update(player, Width, Height, current_map.width, current_map.height)

    for enemy in current_map.enemies:
        enemy.move(player, current_map.get_surface())
        enemy.draw(screen, camera)



    player.draw(screen, camera)
    player.show_hp()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()