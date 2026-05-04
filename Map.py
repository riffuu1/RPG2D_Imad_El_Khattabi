import pygame

class Map:
    def __init__(self, width, height, bg_image, bg_name, enemies=None, pickable_objects=None,door_objects=None):
        self.width = width
        self.height = height
        self.bg_image = bg_image
        self.bg_name = bg_name
        self.enemies = enemies if enemies else []
        self.pickable_objects = pickable_objects if pickable_objects else []
        self.door_objects = door_objects if door_objects else []

    @staticmethod
    def switch_map(current_map, player, map1, map2):
        # border top
        if player.rect.y == 0:
            if current_map == map2:
                player.rect.y = 1048
                return map1

        # border bottom
        elif player.rect.y >= 1048:
            if current_map == map1:
                player.rect.y = 0
                return map2


        return current_map

    def get_surface(self):
        return self.bg_image

    def draw(self, screen, camera):
        screen.blit(self.bg_image, (-camera.x, -camera.y))

        #Pickable objects
        for obj in self.pickable_objects:
            if hasattr(obj, "active") and not obj.active:
                continue
            obj.draw(screen,camera)

        # door objects
        for obj in self.door_objects:
            if hasattr(obj, "active") and not obj.active:
                continue
            obj.draw(screen, camera)
