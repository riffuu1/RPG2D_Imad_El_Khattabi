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
        self.max_hp = self.hp

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
        }
        self.current_animation = self.animations["idle_right"]

    #========================
    # Animations
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

    #=====================
    # Moves
    #====================
    def update(self, keys,map_width, map_height):
        old_x, od_y = self.rect.x, self.rect.y
        in_movement = False

        # --- Vertical moves ---
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            if self.last_direction == "left":
                self.current_animation = self.animations["walk_left"]
            else:
                self.current_animation = self.animations["walk_right"]
            in_movement = True

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            if self.last_direction == "left":
                self.current_animation = self.animations["walk_left"]
            else:
                self.current_animation = self.animations["walk_right"]
            in_movement = True

        # --- Horizontal moves ---
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.current_animation = self.animations["walk_left"]
            self.last_direction = "left"
            in_movement = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.current_animation = self.animations["walk_right"]
            self.last_direction = "right"
            in_movement = True

        # --- Not in movement ---
        if not in_movement:
            self.current_animation = self.animations[f"idle_{self.last_direction}"]

        # limites de la map
        self.rect.x = max(0, min(self.rect.x, map_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, map_height - self.rect.height))

    #================
    # HP
    #================
    def show_hp(self):
        font = pygame.font.Font(None, 36)
        hp_text = font.render(f"HP: {self.hp}", True, (255, 255, 255))
        bar_x, bar_y = 20, 20
        bar_width, bar_height = 200, 20
        pygame.draw.rect(self.screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        hp_width = int((self.hp / self.max_hp) * bar_width)
        pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, hp_width, bar_height))
        self.screen.blit(hp_text, (bar_x, bar_y))

    def draw(self, surface, camera):
        frame = self.get_frame()
        surface.blit(frame,(self.rect.x - camera.x,self.rect.y - camera.y))