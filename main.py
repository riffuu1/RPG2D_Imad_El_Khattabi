# Author : El Khattabi Imad
# Date: 28.04.2026
# Version : 2.0


import pygame
from pygame.display import get_surface

from Objects import *
from Player import Player
from Camera import Camera
from Enemy import Enemy
from Map import Map
from inventory_menu import inventory_menu
from Items import *
from sign_in import register_screen
from log_in import login_screen
from backend.config.db import save_score
from saves import *
from Main_menu import main_menu
from ranking import ranking
from pause_menu import pause_menu


pygame.init()

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Chroniques du Kraken oublié")


def game(screen, username, mode="new"):

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
    player = Player(screen, folder_player,username)
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
    pickable_potion =PickableObject(200,350,potion_image,potion_item,"potion_1")

    skull_key_image = pygame.image.load('assets/Items/Skull_key.png.')
    skull_key_image = pygame.transform.scale(skull_key_image, (50, 50))
    skull_item = Key("skull_key","skull_key",skull_key_image)
    pickable_key = PickableObject(1736, 462,skull_key_image,skull_item,"skull_key")

    gem_key_image = pygame.image.load('assets/Items/gem_key.png.')
    gem_key_image = pygame.transform.scale(gem_key_image, (50, 50))
    gem_item = Key("gem_key", "gem_key", gem_key_image)
    pickable_key_2 = PickableObject(70, 250, gem_key_image, gem_item, "gem_key")

    patrick_key_image = pygame.image.load('assets/Items/patrick_key.png.')
    patrick_key_image = pygame.transform.scale(patrick_key_image, (50, 50))
    patrick_item = Key("patrick_key", "patrick_key", patrick_key_image)
    pickable_key_3 = PickableObject(1680, 1042, patrick_key_image, patrick_item, "patrick_key")

    kraken_key_image = pygame.image.load('assets/Items/final_key.png.')
    kraken_key_image = pygame.transform.scale(kraken_key_image, (50, 50))
    kraken_item = Key("kraken_key", "kraken_key", kraken_key_image)
    pickable_key_4 = PickableObject(1654, 60, kraken_key_image, kraken_item, "kraken_key")


    #==========================
    # Doors
    #=========================
    door_1_image = pygame.image.load('assets/Door/door_map_2.png')
    door_1_image = pygame.transform.scale(door_1_image, (1402, 36))
    door_1_id = "skull_key"
    door_1 = Door(210,996,door_1_image,door_1_id,"door_1")

    door_2_image = pygame.image.load('assets/Door/patrick_door.png')
    door_2_image = pygame.transform.scale(door_2_image, (114, 37))
    door_2_id = "patrick_key"
    door_2 = Door(1586,232,door_2_image,door_2_id,"door_2")

    door_3_image = pygame.image.load('assets/Door/gem_door.png')
    door_3_image = pygame.transform.scale(door_3_image, (128, 34))
    door_3_id = "gem_key"
    door_3 = Door(1360, 884,door_3_image,door_3_id,"door_3")

    door_4_image = pygame.image.load('assets/Door/kraken_door.png')
    door_4_image = pygame.transform.scale(door_4_image, (244, 41))
    door_4_id = "kraken_key"
    door_4 = Door(828,306,door_4_image,door_4_id,"door_4")
    doors = [door_1,door_2,door_3,door_4]

    #=================
    # Tresor
    #=================
    tresor_image = pygame.image.load('assets/Tresor/Last tresor.png')
    tresor_image = pygame.transform.scale(tresor_image, (250, 250))
    final_tresor = Tresor(800,28, tresor_image,"tresor_1")
    tresors=[final_tresor]

    #=========================
    # Pearls
    #=========================
    pearl_1_image = pygame.image.load('assets/Pearles/pearles_1.png')
    pearl_1_image = pygame.transform.scale(pearl_1_image, (50, 50))
    pearl_2_image = pygame.image.load('assets/Pearles/pearles_2.png')
    pearl_2_image = pygame.transform.scale(pearl_2_image, (50, 50))
    pearl_3_image = pygame.image.load('assets/Pearles/pearles_3.png')
    pearl_3_image = pygame.transform.scale(pearl_3_image, (50, 50))
    pearl_1 = Pearls (36,556,pearl_1_image,25,"pearles_1")
    pearl_2 = Pearls(592,888, pearl_1_image,25,"pearles_2")
    pearl_3 = Pearls(1442,272, pearl_1_image,25,"pearles_3")
    pearl_4 = Pearls(956,338, pearl_1_image,25,"pearles_4")
    pearl_5 = Pearls(790,1044, pearl_1_image,25,"pearles_5")
    pearl_6 = Pearls(610,780, pearl_1_image,25,"pearles_6")
    pearl_7 = Pearls(1424,346, pearl_1_image,25,"pearles_7")
    pearl_8 = Pearls (1496,380,pearl_1_image,25,"pearles_8")
    pearl_9 = Pearls(1048,658, pearl_2_image,50,"pearles_9")
    pearl_10 = Pearls(446,814, pearl_2_image,50,"pearles_10")
    pearl_11 = Pearls(1590,682, pearl_2_image,50,"pearles_11")
    pearl_12 = Pearls(552, 416, pearl_2_image,50,"pearles_12")
    pearl_13 = Pearls(818,932, pearl_2_image,50,"pearles_13")
    pearl_14 = Pearls(1286,394, pearl_2_image,50,"pearles_14")
    pearl_15 = Pearls(94,24, pearl_3_image,75,"pearles_15")
    pearl_16 = Pearls(128,788, pearl_3_image,75,"pearles_16")
    pearl_17 = Pearls(1414,490, pearl_3_image,75,"pearles_17")
    pearl_18 = Pearls(76, 614, pearl_2_image, 50, "pearles_18")
    pearl_19 = Pearls(320, 156, pearl_3_image, 75, "pearles_19")
    pearl_20 = Pearls(1000, 896, pearl_1_image, 25, "pearles_20")
    pearl_21 = Pearls(1016, 1062, pearl_3_image, 75, "pearles_21")
    pearl_22 = Pearls(1692, 740, pearl_3_image, 75, "pearles_22")
    pearl_23 = Pearls(1398,294, pearl_3_image,75,"pearles_23")

    pearls= [pearl_1,pearl_2,pearl_3,pearl_4,pearl_5,pearl_6,pearl_7,pearl_8,pearl_9,pearl_10,pearl_11,pearl_12,pearl_13,pearl_14,pearl_15,pearl_16,pearl_17,pearl_18,pearl_19,pearl_20,pearl_21,pearl_22,pearl_23]

    #===========================
    # Traps
    #==========================
    jellyfish_image = pygame.image.load('assets/Enemys/jellyfish.png')
    jellyfish_1 = Traps(1318,256,jellyfish_image,25,"jellyfish_1")
    jellyfish_2 = Traps(1378, 256, jellyfish_image, 25,"jellyfish_2")
    jellyfish_3 = Traps(1426, 256, jellyfish_image, 25,"jellyfish_3")
    jellyfish_4 = Traps(1488, 256, jellyfish_image, 25,"jellyfish_4")
    jellyfish_5 = Traps(1536, 256, jellyfish_image, 25,"jellyfish_5")
    jellyfish_6 = Traps(1598, 256, jellyfish_image, 25,"jellyfish_6")
    jellyfish_7 = Traps(1670, 256, jellyfish_image, 25,"jellyfish_7")
    jellyfishs = [jellyfish_1,jellyfish_2,jellyfish_3,jellyfish_4,jellyfish_5,jellyfish_6,jellyfish_7]

    #=========================
    # Maps
    #========================
    map_1 = Map(1900, 1200, background_1,"map_1",[],[pickable_potion,pickable_key],[],[],[pearl_1,pearl_2,pearl_3,pearl_9],[])
    map_2 = Map(1900, 1200, background_2,"map_2",[octopus_1,octopus_2,octopus_3,octopus_4],[],[door_1],[],[pearl_4,pearl_5,pearl_10,pearl_11,pearl_15],[])
    map_3 = Map(1900, 1200, background_3,"map_3",[scary_fish_1,scary_fish_2,scary_fish_3],[],[pickable_key],[],[pearl_6,pearl_7,pearl_8,pearl_12,pearl_13,pearl_14,pearl_16,pearl_17],[jellyfish_1,jellyfish_2,jellyfish_3,jellyfish_4,jellyfish_5,jellyfish_6,jellyfish_7])
    map_4 = Map(1900, 1200, background_4,"map_4",[],[pickable_key_2,pickable_key_3,pickable_key_4],[door_2,door_3,door_4],[final_tresor],[pearl_18,pearl_19,pearl_20,pearl_21,pearl_22,pearl_23],[])
    maps = [map_1, map_2,map_3,map_4]
    current_map = map_1

    #=================
    # Camera
    #=================
    camera = Camera()

    #=====================
    # End function
    #====================
    def end_screen(screen, player):
        clock = pygame.time.Clock()
        waiting = True
        score_saved = False


        while waiting:
            screen.fill((0, 0, 0))

            font = pygame.font.Font(None, 80)

            if player.win:

                text = font.render("VICTORY !!!", True, (0, 255, 0))
                if not score_saved:
                    player.score += player.count
                    save_score(player.username, player.score)
                    score_saved = True
            else:
                text = font.render("GAME OVER", True, (255, 0, 0))

            score = pygame.font.Font(None, 50).render(
                f"Score final : {player.score}", True, (255, 255, 255)
            )

            info = pygame.font.Font(None, 36).render(
                "Appuie n'importe quelle touche pour quitter",
                True,
                (200, 200, 200)
            )

            screen.blit(text, (250, 200))
            screen.blit(score, (250, 300))
            screen.blit(info, (120, 400))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return "restart"
                    if event.key == pygame.K_ESCAPE:
                        return "quit"

            clock.tick(60)


    #==================
    # Main Loop
    #==================
    clock = pygame.time.Clock()
    running = True
    e_pressed = False

    if mode == "load":
        current_map = charging(player, maps)
    else:
        current_map = map_1

    while running:
        keys = pygame.key.get_pressed()
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                saving(player,maps,current_map)
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    e_pressed = True
                if event.key == pygame.K_i:
                    inventory_menu(screen,pygame.font.Font(None, 36), player)
                if event.key == pygame.K_ESCAPE:
                    pause_menu(screen, pygame.font.Font(None, 40), pygame.font.Font(None, 80), player, current_map, maps)
                if event.key == pygame.K_F5:
                    saving(player, maps, current_map)

                if event.key == pygame.K_F9:
                    current_map = charging(player, maps)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_e:
                    e_pressed = False


        current_map.draw(screen, camera)
        if player.alive:
            player.update(keys,current_map.width, current_map.height, current_map.get_surface(),current_map.enemies,current_map.door_objects)
            old_map = current_map
            current_map = Map.switch_map(current_map, player, map_1, map_2,map_3,map_4)
            if old_map != current_map:
                saving(player, maps, current_map)
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

            for tresor in current_map.treasure_objects:
                result = tresor.win(player)

                if result == "win":
                    player.win = True
                    player.alive = False
                    return end_screen(screen, player)

            for pearls in current_map.pearls_objects:
                points = pearls.points(player)

            for traps in current_map.traps_objects:
                damage = traps.hurt(player)


        result = player.draw(screen, camera,events)
        if result == "restart":
            player.reset()
            current_map = map_1

            # --- Reset enemies ---
            for enemy in enemies:
                enemy.reset()

            # --- Reset objects ---
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
username = None

while True:

    if state == "register":
        result = register_screen(screen)
        if result:
            state, username = result if isinstance(result, tuple) else (result, None)

    elif state == "login":
        result = login_screen(screen)
        if result:
            state, username = result


    elif state == "game":

        state = game(screen, username, mode="new")


    elif state == "continue":

        state = game(screen, username, mode="load")


    elif state == "menu":
        result = main_menu(screen, username)
        if result:
            state, username = result

    elif state == "ranking":
        result = ranking(screen, username)
        if result:
            state, username = result

    elif state == "quit":
        break

pygame.quit()