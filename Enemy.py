# Author : El Khattabi Imad
# Date: 28.04.2026
# Version : 1.0

import pygame
import os
import math
from Collision_color import *

class Enemy:
    def __init__(self,screen, name, image_path, x, y, hp):
        self.screen = screen
        self.name = name
        self.hp = hp
        self.max_hp = self.hp
        self.speed = 1.5
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(128,128))
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.rect = self.image.get_rect(topleft=(x,y))
        self.hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 70, 48, 50)
        self.active = True
        self.attack_cooldown = 1000
        self.last_attack_time = 0

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.rect.topleft = (self.x, self.y)
        self.update_hitbox()
        self.hp = self.max_hp
        self.active = True

    def draw(self, screen,camera):
        if self.active:
            screen.blit(self.image,(self.rect.x - camera.x, self.rect.y - camera.y))

    def update_hitbox(self):
        self.hitbox.topleft = (self.rect.x + 40, self.rect.y + 70)



    #===============
    # Moves
    #===============
    def move(self, player,collision_surface):
        if not self.active:
            return  # Do nothing if the enemy is dead

        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery

        distance = math.hypot(dx, dy)
        if distance == 0:
            return

        if distance <= 200:  # --- Normalize vector ---
            dx /= distance
            dy /= distance

            future_hitbox = self.hitbox.copy()
            future_hitbox.x += dx * self.speed
            future_hitbox.y += dy * self.speed

            future_x = self.rect.x + dx * self.speed
            future_y = self.rect.y + dy * self.speed

            check_x = int(future_x + 64)
            check_y = int(future_y + 100)


            # --- Check the colors of map for possible collision ---
            if not check_collision_with_color(collision_surface, check_x, check_y) and not future_hitbox.colliderect(player.hitbox):
                self.rect.x += dx * self.speed
                self.rect.y += dy * self.speed
                self.update_hitbox()


                self.hitbox.x = self.rect.x + 40
                self.hitbox.y = self.rect.y + 70

            # --- Check if enemy touches the player to hurt him ---
            if future_hitbox.colliderect(player.hitbox):
                current_time = pygame.time.get_ticks()

                if current_time - self.last_attack_time >= self.attack_cooldown:
                    player.hp -= 10
                    player.hp = max(0, player.hp)
                    if player.hp <= 0:
                        player.alive = False

                    self.last_attack_time = current_time