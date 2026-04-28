# Author : El Khattabi Imad
# Date: 28.04.2026
# Version : 1.0

import pygame
import os

class Enemy:
    def __init__(self,screen, name, image_path, x, y, hp):
        self.screen = screen
        self.name = name
        self.hp = hp
        self.speed = 1.5
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(128,128))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x,y))
        self.hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 70, 48, 50)
        self.active = True

    def draw(self, screen):
        if self.active:
            self.screen.blit(self.image, self.rect)
