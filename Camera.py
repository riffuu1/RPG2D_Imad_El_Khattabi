# Author : El Khattabi Imad
# Date: 27.04.2026
# Version : 1.0


# With Help of Chat GPT
#=======================
class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self, player, screen_width, screen_height, map_width, map_height):
        # player in the center
        self.x = player.rect.x + player.rect.width // 2 - screen_width // 2
        self.y = player.rect.y + player.rect.height // 2 - screen_height // 2

        # screen limit
        self.x = max(0, min(self.x, map_width - screen_width))
        self.y = max(0, min(self.y, map_height - screen_height))