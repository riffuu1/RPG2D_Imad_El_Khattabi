# Author : El Khattabi Imad
# Date: 28.04.2026
# Version : 1.5


import pygame
from pygame.display import get_surface

from Objects import PickableObject
from Player import Player
from Camera import Camera
from Enemy import Enemy
from Map import Map
from inventory_menu import inventory_menu
from Items import *

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
# Pickable Object
#=========================
potion_image = pygame.image.load('assets/Items/heal potion.png')
potion_image = pygame.transform.scale(potion_image, (50, 50))
potion_item = Potion("Potion", potion_image)
pickable_potion =PickableObject(200,350,potion_image,potion_item)



#=========================
# Maps
#========================
map_1 = Map(1900, 1200, background_1,"map_1",[],[pickable_potion])
map_2 = Map(1900, 1200, background_2,"map_2",[enemy],[])
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                e_pressed = True
            if event.key == pygame.K_i:
                inventory_menu(screen,pygame.font.Font(None, 36), player)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                e_pressed = False

    current_map.draw(screen, camera)
    player.update(keys,current_map.width, current_map.height, current_map.get_surface(),enemies)

    current_map = Map.switch_map(current_map, player, map_1, map_2)
    camera.update(player, Width, Height, current_map.width, current_map.height)

    for enemy in current_map.enemies:
        enemy.move(player, current_map.get_surface())
        enemy.draw(screen, camera)


    for obj in current_map.pickable_objects:
        obj.interact(player, e_pressed)

    player.draw(screen, camera)
    player.show_hp()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()