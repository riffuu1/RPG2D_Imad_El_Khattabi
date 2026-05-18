import pygame
import pygame_menu

from sign_in import WIDTH

pygame.init()

WIDTH, HEIGHT = 800, 700


# ======================
# TEXT DRAW
# ======================
def draw_text(screen, text, font, color, x, y, center=False):
    lines = text.split("\n")

    for i, line in enumerate(lines):
        img = font.render(line, True, color)

        if center:
            rect = img.get_rect(center=(x, y + i * 40))
            screen.blit(img, rect)
        else:
            screen.blit(img, (x, y + i * 40))


def main_menu(screen, username):

    pygame.display.set_caption("Main Menu")

    font = pygame.font.Font(None,40)

    running = True

    while running:

        screen.fill((20,20,30))

        #==========================
        # TITLE
        #==========================
        draw_text(screen, "Chroniques du Kraken oublié", font, (255,255,255), 200, 100)

        new_game_button = pygame.Rect(310, 320, 190, 60)
        pygame.draw.rect(screen, (70, 130, 180), new_game_button)
        draw_text(screen, "New Game", font, (255, 255, 255), 340, 337)

        quit_button = pygame.Rect(370, 420, 80, 60)
        pygame.draw.rect(screen, (70, 130, 180), quit_button)
        draw_text(screen, "Quit", font, (255, 255, 255), 380, 437)

        #===========================
        # EVENTS
        #===========================
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            # --- Click ---
            if event.type == pygame.MOUSEBUTTONDOWN:

                if new_game_button.collidepoint(event.pos):
                    return "game", username

                if quit_button.collidepoint(event.pos):
                    return "quit", username

        pygame.display.flip()