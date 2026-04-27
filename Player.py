# Author : El Khattabi Imad
# Date: 27.04.2026
# Version : 1.0



import pygame

class Player:
    def __init__(self, screen, player_folder,hp=100):
        self.screen = screen
        self.start_x = 200
        self.start_y = 150
        self.hp = hp

        self.x = self.start_x
        self.y = self.start_y
        self.speed = 2
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

        self.frame_index = 0
        self.frame_speed = 0.05
        self.last_direction = "right"

        #Animations
        self.animations = {
            "idle_left":self.load_animation(player_folder, ["player_left_0.png", "player_left_1.png"]),
            "idle_right": self.load_animation(player_folder, ["player_right_0.png", "player_right_1.png"]),
            "walk_left": self.load_animation(player_folder, ["player_left_0.png", "player_left_1.png"]),
            "walk_right": self.load_animation(player_folder, ["player_right_0.png", "player_right_1.png"]),
            "attack_left": self.load_animation(player_folder, ["player_attacks_left.png"]),
            "attacks_right": self.load_animation(player_folder, ["player_attacks_right.png"]),
        }
        self.current_animation = self.animations["idle_right"]

        #========================
        # Animation
        #========================
        def load_animation(self, folder, image_names, size=(128,128)):
            frames =[]
            for name in image_names:
                path = f"{folder}/{name}"
                image = pygame.image.load(path).convert_alpha()
                image = pygame.transform.scale(image, size)
                frames.append(image)
            return frames

        def get_frame(self):
            self.frame_index += self.frame_speed
            if self.frame_index >= len(self.current_animation):
                self.frame_index = 0
            return self.current_animation[int(self.frame_index)]
