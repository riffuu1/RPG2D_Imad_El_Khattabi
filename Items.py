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
    def __init__(self, name, key_id, image_path=None):
        super().__init__(name, image_path)
        self.key_id = key_id



