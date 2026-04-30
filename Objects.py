import pygame

class GameObject:
    def __init__(self, image, x, y):
        self.rect = image.get_rect(topleft=(x, y))
        self.image = image
        self.active = True

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.rect)

    def interact(self):
        pass

class PickableObject(GameObject):
    def __init__(self, x, y, image, item):
        # --- super() initializes parent class attributes (self.rect, self.image, self.active) ---
        super().__init__(image, x, y)
        self.item = item

    def interact(self, player, e_pressed):
        if self.active and self.rect.colliderect(player.feet) and e_pressed:
            player.add_item(self.item)
            self.active = False