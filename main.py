# Author : El Khattabi Imad
# Date: 28.04.2026
# Version : 2.0


import pygame
from pygame.display import get_surface

from Objects import PickableObject, Door
from Player import Player
from Camera import Camera
from Enemy import Enemy
from Map import Map
from inventory_menu import inventory_menu
from Items import *
from sign_in import register_screen
from log_in import login_screen

pygame.init()

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Chroniques du Kraken oublié")


def game(screen):

    #================
    # Window
    #================
    Width, Height = 800, 700
    pygame.display.set_caption("Chroniques du Kraken oublié")


    #==================
    # Background
    #==================
    background_1 = pygame.image.load('assets/Backgrounds/background_1.png')
    background_1 = pygame.transform.scale(background_1, (1900, 1200))

    background_2 = pygame.image.load('assets/Backgrounds/background_2.png')
    background_2 = pygame.transform.scale(background_2, (1900, 1200))

    background_3 = pygame.image.load('assets/Backgrounds/map_3.png')
    background_3 = pygame.transform.scale(background_3, (1900, 1200))

    background_4 = pygame.image.load('assets/Backgrounds/map_4.png')
    background_4 = pygame.transform.scale(background_4, (1900, 1200))




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
    folder_octopus = "./assets/Enemys/octopus.png"
    folder_scary_fish = "./assets/Enemys/scary_fish.png"
    octopus_1 = Enemy(screen, "octopus 1", folder_octopus,1200,700, 120)
    octopus_2 = Enemy(screen, "octopus 2", folder_octopus,126,150, 120)
    octopus_3 = Enemy(screen, "octopus 3", folder_octopus,696,472, 120)
    octopus_4 = Enemy(screen, "octopus 4", folder_octopus,798,1018, 120)
    scary_fish_1 = Enemy(screen, "scary fish 1", folder_scary_fish,560,522, 200)
    scary_fish_2 = Enemy(screen, "scary fish 2", folder_scary_fish,908,750, 200)
    scary_fish_3 = Enemy(screen, "scary fish 3", folder_scary_fish,908,912, 200)
    scary_fish_4 = Enemy(screen, "scary fish 4", folder_scary_fish,1200,700, 200)
    enemies = [octopus_1,octopus_2,octopus_3,octopus_4,scary_fish_1,scary_fish_2,scary_fish_3]

    #=========================
    # Pickable Object
    #=========================
    potion_image = pygame.image.load('assets/Items/heal potion.png')
    potion_image = pygame.transform.scale(potion_image, (50, 50))
    potion_item = Potion("Potion", potion_image)
    pickable_potion =PickableObject(200,350,potion_image,potion_item)

    skull_key_image = pygame.image.load('assets/Items/Skull_key.png.')
    skull_key_image = pygame.transform.scale(skull_key_image, (50, 50))
    skull_item = Key("skull_key","skull_key",skull_key_image)
    pickable_key = PickableObject(1736, 462,skull_key_image,skull_item)


    #==========================
    # Doors
    #=========================
    door_image = pygame.image.load('assets/Door/door_map_2.png')
    door_image = pygame.transform.scale(door_image, (1402, 36))
    door_id = "skull_key"
    door_1 = Door(210,996,door_image,door_id)
    doors = [door_1]



    #=========================
    # Maps
    #========================
    map_1 = Map(1900, 1200, background_1,"map_1",[],[pickable_potion,pickable_key],[])
    map_2 = Map(1900, 1200, background_2,"map_2",[octopus_1,octopus_2,octopus_3,octopus_4],[],[door_1])
    map_3 = Map(1900, 1200, background_3,"map_3",[scary_fish_1,scary_fish_2,scary_fish_3],[],[pickable_key])
    map_4 = Map(1900, 1200, background_4,"map_4",[],[],[])
    maps = [map_1, map_2,map_3,map_4]
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
        if player.alive:
            player.update(keys,current_map.width, current_map.height, current_map.get_surface(),current_map.enemies,current_map.door_objects)

            current_map = Map.switch_map(current_map, player, map_1, map_2,map_3,map_4)
            camera.update(player, Width, Height, current_map.width, current_map.height)
            player.countdown()
            player.show_time(screen)

            for enemy in current_map.enemies:
                enemy.move(player, current_map.get_surface())
                enemy.draw(screen, camera)


            for obj in current_map.pickable_objects:
                obj.interact(player, e_pressed)

            for door in current_map.door_objects:
                for item in player.inventory:
                    if isinstance(item, Key):
                        item.use_on(door, player, e_pressed)

        result = player.draw(screen, camera,events)
        if result == "restart":
            player.reset()
            current_map = map_1

            # --- Reset ennemis ---
            for enemy in enemies:
                enemy.reset()

            # --- Reset objets ---
            for m in maps:
                for obj in m.pickable_objects:
                    obj.reset()

                for door in m.door_objects:
                    door.reset() # ou leur valeur initiale
        player.show_hp()
        player.show_score()


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    return  "quit"

state = "register"

while True:

    if state == "register":
        state = register_screen(screen)

    elif state == "login":
        state = login_screen(screen)

    elif state == "game":
        state = game(screen)
        break

    elif state == "quit" or state is False:
        break

pygame.quit()