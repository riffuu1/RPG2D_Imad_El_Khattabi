import pygame
from Player import Player
from Items import *


def inventory_menu(screen, font, player: Player):
    running = True
    clock = pygame.time.Clock()
    selected_index = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_i, pygame.K_ESCAPE):
                    running = False

                if event.key == pygame.K_UP:
                    selected_index = max(0, selected_index - 1)
                if event.key == pygame.K_DOWN:
                    selected_index = min(len(player.inventory) - 1, selected_index + 1)

                if event.key == pygame.K_e and player.inventory:
                    item = player.inventory[selected_index]

                    # Use according to type
                    if isinstance(item, Potion):
                        item.use(player)        # recover HP
                        player.inventory.pop(selected_index)  # potion consumed
                        selected_index = max(0, selected_index - 1)
                    elif isinstance(item, Key):
                        print(f"{item.name} is just in the inventory")  # no removal

        # Semi-transparent background
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # Inventory display
        y = 150
        if not player.inventory:
            text = font.render("Inventory empty", True, (255, 255, 255))
            screen.blit(text, (50, y))
        else:
            for i, item in enumerate(player.inventory):
                color = (255, 255, 0) if i == selected_index else (255, 255, 255)

                if item.image:
                    screen.blit(item.image, (50, y))
                text = font.render(item.name, True, color)
                screen.blit(text, (100, y + 10))
                y += 50

        pygame.display.flip()
        clock.tick(60)