import pygame
import sys
from saves import saving

pygame.init()


def draw_button(surface, rect, text, font):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    color = (60, 60, 60) if rect.collidepoint(mouse_x, mouse_y) else (40, 40, 40)
    pygame.draw.rect(surface, color, rect, border_radius=8)
    pygame.draw.rect(surface, (200, 200, 200), rect, 2, border_radius=8)
    txt = font.render(text, True, (255, 255, 255))
    surface.blit(txt, txt.get_rect(center=rect.center))


def pause_menu(surface, FONT, BIG_FONT, player, current_map, maps):
    clock = pygame.time.Clock()
    btn_w, btn_h = 300, 50
    center_x = surface.get_width() // 2
    start_y = surface.get_height() // 2 - 60
    resume_rect = pygame.Rect(center_x - btn_w // 2, start_y, btn_w, btn_h)
    save_rect = pygame.Rect(center_x - btn_w // 2, start_y + 70, btn_w, btn_h)
    controls_rect = pygame.Rect(center_x - btn_w // 2, start_y + 140, btn_w, btn_h)
    quit_rect = pygame.Rect(center_x - btn_w // 2, start_y + 210, btn_w, btn_h)

    screenshot = surface.copy()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return 'resume'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                if resume_rect.collidepoint(mx, my):
                    return 'resume'
                if save_rect.collidepoint(mx, my):
                    saving(player, maps, current_map)
                if controls_rect.collidepoint(mx, my):
                    show_controls(surface, FONT)
                if quit_rect.collidepoint(mx, my):
                    pygame.quit()
                    sys.exit()

        surface.blit(screenshot, (0, 0))
        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        surface.blit(overlay, (0, 0))

        title_surf = BIG_FONT.render("PAUSE", True, (255, 255, 255))
        surface.blit(title_surf, title_surf.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 - 130)))

        draw_button(surface, resume_rect, "Resume", FONT)
        draw_button(surface, save_rect, "Save Game", FONT)
        draw_button(surface, controls_rect, "Controls", FONT)
        draw_button(surface, quit_rect, "Quit", FONT)

        pygame.display.flip()
        clock.tick(60)

def show_controls(surface, FONT):
    clock = pygame.time.Clock()
    running = True
    controls_text = [
        "Déplacer à gauche : flèche gauche",
        "Déplacer à droite : flèche droite",
        "Déplacer en haut : flèche haut",
        "Déplacer en bas : flèche bas",
        "L'inventaire : I",
        "Prendre un objet : E",
        "Utiliser un objet Item : E",
        "Attaquer : X",
        "Mettre en Pause/Retour : Esc",
    ]
    screenshot = surface.copy()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                running = False

        surface.blit(screenshot, (0, 0))
        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        surface.blit(overlay, (0, 0))

        y_offset = 100
        for line in controls_text:
            text_surf = FONT.render(line, True, (255, 255, 255))
            surface.blit(text_surf, text_surf.get_rect(center=(surface.get_width() // 2, y_offset)))
            y_offset += 50

        pygame.display.flip()
        clock.tick(60)