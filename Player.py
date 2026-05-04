# Author : El Khattabi Imad
# Date: 27.04.2026
# Version : 1.2



import pygame
from Collision_color import *
from Enemy import Enemy
from Damage_effect import DamageEffect
from Items import *

class Player:
    def __init__(self, screen, player_folder,hp=100,damage=20):
        self.screen = screen
        self.start_x = 200
        self.start_y = 350
        self.hp = hp
        self.max_hp = self.hp
        self.inventory = []
        self.damage = damage
        self.attack_cooldown = 300 # ms
        self.last_attack_time = 0
        self.effects = []
        self.damage_image = None


        self.x = self.start_x
        self.y = self.start_y
        self.speed = 2
        self.rect = pygame.Rect(self.x, self.y, 128, 128)
        self.hitbox = pygame.Rect(self.rect.x + 40, self.rect.y + 70, 48, 50)
        self.feet = pygame.Rect(self.x + 54, self.y + 118, 20, 10)

        self.frame_index = 0
        self.frame_speed = 0.05
        self.last_direction = "right"
        self.alive = True

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


    #====================
    # Collisions
    #====================
    def collision(self, surface):
        points = [
            self.hitbox.topleft,
            self.hitbox.topright,
            self.hitbox.bottomleft,
            self.hitbox.bottomright,
            self.hitbox.midleft,
            self.hitbox.midright,
            self.hitbox.midtop,
            self.hitbox.midbottom
        ]

        for px, py in points:
            if check_collision_with_color(surface, px, py):
                return True

        return False

    #=====================
    # Moves
    #====================
    def update(self, keys,map_width, map_height,surface,enemies):
        if not self.alive:
            return
        old_x, old_y = self.rect.x, self.rect.y
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

        # --- Update Hitbox ---
        self.hitbox.y = self.rect.y + 70

        # --- Vertical Collision ---
        if self.collision(surface):
            self.rect.y = old_y
            self.hitbox.y = old_y + 70

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

        self.hitbox.x = self.rect.x + 40

        # --- Horizontal Collision ---
        if self.collision(surface):
            self.rect.x = old_x
            self.hitbox.x = old_x + 40

        # --- Not in movement ---
        if not in_movement:
            self.current_animation = self.animations[f"idle_{self.last_direction}"]

        # --- Border of the map ---
        self.rect.x = max(0, min(self.rect.x, map_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, map_height - self.rect.height))

        for enemy in enemies:
            if enemy.active and self.hitbox.colliderect(enemy.hitbox):
                # --- prevents player to pass through ennemies ---
                self.rect.x = old_x
                self.hitbox.x = old_x + 40

                self.rect.y = old_y
                self.hitbox.y = old_y + 70

        # --- Attack ---
        if keys[pygame.K_x]:
            self.attack(enemies)

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

    #=================
    # Attack
    #=================
    def attack(self,enemies):
        if not self.damage_image:
            return

        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time < self.attack_cooldown:
            return
        self.last_attack_time = current_time

        attack_range = 50
        attack_rect = self.hitbox.copy()
        if self.last_direction == "left":
            attack_rect.x -= attack_range
            effect_x, effect_y, angle = attack_rect.right, attack_rect.centery, 180
        elif self.last_direction == "right":
            attack_rect.x += attack_range
            effect_x, effect_y, angle = attack_rect.left, attack_rect.centery, 0

        # --- Apply the damage ---
        for enemy in enemies:
            if enemy.active and attack_rect.colliderect(enemy.hitbox):
                enemy.hp -= self.damage
                print(f"{enemy.name} takes {self.damage} damage")
                if enemy.hp <= 0:
                    enemy.active = False

        # --- Visual Effect ---
        rotated_image = pygame.transform.rotate(self.damage_image, angle)
        effect = DamageEffect(effect_x - rotated_image.get_width() // 2,
                              effect_y - rotated_image.get_height() // 2,
                              rotated_image)
        self.effects.append(effect)

    #=================
    # Inventory
    #=================

    def add_item(self, item: Item):
        if self.inventory.count(item) <8:
            if item not in self.inventory:
                self.inventory.append(item)
                print(f"{item.name} added to inventory")

    def remove_item(self, item: Item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item.name} removed from inventory")

    def use_item(self, item: Item):
        item.use(self)
        if isinstance(item, Potion):
            self.remove_item(item)



    #================
    # Affichage
    #================
    def draw(self, surface, camera):
        if not self.alive:
            overlay = pygame.Surface(surface.get_size())
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            surface.blit(overlay, (0, 0))

            font = pygame.font.Font(None, 80)
            text = font.render("GAME OVER", True, (255, 0, 0))

            text_rect = text.get_rect(center=(surface.get_width() // 2,
                                              surface.get_height() // 2))
            surface.blit(text, text_rect)
            return

        # --- Player animation ---
        surface.blit(self.get_frame(),
                     (self.rect.x - camera.x, self.rect.y - camera.y))

        # --- Effects ---
        for effect in self.effects:
            effect.draw(surface, camera)

        self.effects = [e for e in self.effects if not e.is_finished()]