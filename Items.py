# Author : El Khattabi Imad
# Date: 04.05.2026
# Version : 2.0


import pygame

class Item:
    def __init__(self, name, image):
        self.name = name
        self.image = image

    def use(self, player):
        print(f"Item {self.name} used")

class Potion(Item):
    def use(self, player):
        player.hp = min(player.max_hp, player.hp + 20)
        print("You recover 20 HP")


class Key(Item):
    def __init__(self, name, key_id, image):
        super().__init__(name, image)
        self.key_id = key_id

    def use_on(self, door, player, e_pressed):
        if not e_pressed:
            return

        if not door.active:
            return

        if not door.rect.colliderect(player.rect):
            return

        if self.key_id == door.door:
            door.active = False
            player.remove_item(self)
            print("Door unlocked with key:", self.name)



