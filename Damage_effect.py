# Author : El Khattabi Imad
# Date: 29.04.2026
# Version : 1.0


import pygame

class DamageEffect:
    def __init__(self, x, y, image, duration=200):
        self.image = image
        self.x = x
        self.y = y
        self.start_time = pygame.time.get_ticks()
        self.duration = duration

    def is_finished(self):
    #--- Check if the effect duration has elapsed. ---
        return pygame.time.get_ticks() - self.start_time > self.duration

    def draw(self, screen, camera):
        screen.blit(self.image, (self.x - camera.x, self.y - camera.y))