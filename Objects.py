import pygame
from Items import *

class GameObject:
    def __init__(self, image, x, y):
        self.rect = image.get_rect(topleft=(x, y))
        self.image = image
        self.active = True

    def draw(self, screen, camera):
        if self.active:
            screen.blit(self.image, (self.rect.x - camera.x, self.rect.y - camera.y))

    def interact(self):
        pass

class PickableObject(GameObject):
    def __init__(self, x, y, image, item):
        # --- super() initializes parent class attributes (self.rect, self.image, self.active) ---
        super().__init__(image, x, y)
        self.item = item

    def interact(self, player, e_pressed):
        if self.active and self.rect.colliderect(player.rect) and e_pressed:
            if len(player.inventory) < 8:
                player.add_item(self.item)
                self.active = False

class Door(GameObject):
    def __init__(self, x, y, image, door_id):
        super().__init__(image,x,y)
        self.door = door_id
        self.active = True

    def unlock(self,player, e_pressed):
        if not self.active:
            return

        if not e_pressed:
            return

        for item in player.inventory:
            if isinstance(item, Key) and item.key_id == self.door:
                self.active = False
                print("Door unlocked")
                return