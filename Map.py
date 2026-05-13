# Author : El Khattabi Imad
# Date: 04.05.2026
# Version : 2.1


import pygame

class Map:
    def __init__(self, width, height, bg_image, bg_name, enemies=None, pickable_objects=None,door_objects=None, treasure_objects=None, pearls_objects=None):
        self.width = width
        self.height = height
        self.bg_image = bg_image
        self.bg_name = bg_name
        self.enemies = enemies if enemies else []
        self.pickable_objects = pickable_objects if pickable_objects else []
        self.door_objects = door_objects if door_objects else []
        self.treasure_objects = treasure_objects if treasure_objects else []
        self.pearls_objects = pearls_objects if pearls_objects else []


    @staticmethod
    def switch_map(current_map, player, map1, map2,map3,map4):
        # --- Border top ---
        if player.rect.y == 0:
            if current_map == map2:
                player.rect.y = 1048
                return map1
            if current_map == map3:
                player.rect.y = 1048
                return map2

        # --- Border bottom ---
        elif player.rect.y >= 1048:
            if current_map == map1:
                player.rect.y = 0
                return map2
            if current_map == map2:
                player.rect.y = 0
                return map3
        # --- Border left ---
        elif player.rect.x == 0:
            if current_map == map4:
                player.rect.x = 1468
                return map3

        # --- Border right ---
        elif player.rect.x <= 1484 and player.rect.x >= 1470 and player.rect.y >= 800:
            if current_map == map3:
                player.rect.x = 0
                player.rect.y = 950
                return map4

        return current_map

    def get_surface(self):
        return self.bg_image

    def draw(self, screen, camera):
        screen.blit(self.bg_image, (-camera.x, -camera.y))

        # --- pickable objects ---
        for obj in self.pickable_objects:
            if hasattr(obj, "active") and not obj.active:
                continue
            obj.draw(screen,camera)

        # --- door objects ---
        for obj in self.door_objects:
            if hasattr(obj, "active") and not obj.active:
                continue
            obj.draw(screen, camera)

        # --- tresor objects ---
        for obj in self.treasure_objects:
            obj.draw(screen, camera)

        # --- pearl objects ---
        for obj in self.pearls_objects:
            obj.draw(screen, camera)