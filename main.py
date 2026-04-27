import pygame

from Player import Player

pygame.init()

#================
# Window
#================
Width, Height = 800, 700
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Chroniques du Kraken oublié")


#==================
# Background
#==================
background_1 = pygame.image.load('Design/Backgrounds/background_1.png')
background_1 = pygame.transform.scale(background_1, (1900, 1200))

current_map = background_1
#==================
# Player
#==================
folder_player = "./Design/Player/Moves"
player = Player(screen, folder_player)


#==================
# Main Loop
#==================
clock = pygame.time.Clock()
running = True
e_pressed = False

while running:
    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.blit(current_map, (0, 0))
    player.update(keys)

    player.draw()
    player.show_hp()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()