# Author : El Khattabi Imad
# Date: 04.05.2026
# Version : 2.0


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

    def reset(self):
        self.active = True

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

class Tresor(GameObject):

    def __init__(self, x, y, image):
        super().__init__(image, x, y)
        self.finished = False

    def win(self, player):
        if self.rect.colliderect(player.hitbox):
            self.finished = True
            return "win"

class Pearls(GameObject):
    def __init__(self, x, y, image,score):
        super().__init__(image, x, y)
        self.score = score
        self.active = True

    def points(self,player):
        if self.active == False:
            return
        else:
            if self.rect.colliderect(player.hitbox):
                self.active = False
                player.score += self.score

class Traps(GameObject):
    def __init__(self, x, y, image,damage):
        super().__init__(image, x, y)
        self.damage = damage
        self.attack_cooldown = 1000
        self.last_attack_time = 0

    def hurt(self,player):
        if not self.rect.colliderect(player):
            return
        else:
            current_time = pygame.time.get_ticks()

            if current_time - self.last_attack_time >= self.attack_cooldown:
                player.hp -= self.damage
                player.hp = max(0, player.hp)
                if player.hp <= 0:
                    player.alive = False

                self.last_attack_time = current_time


