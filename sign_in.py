import pygame
from backend.config.db import register_user
from popup import Popup
from log_in import login_screen

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



# ======================
# MAIN SCREEN
# ======================
def register_screen(screen):


    pygame.display.set_caption("Register")

    font = pygame.font.Font(None, 40)

    username = ""
    password = ""
    confirm_password = ""

    active_input = "username"

    popup = Popup()

    running = True

    while running:

        screen.fill((20, 20, 30))

        # ======================
        # TITLE
        # ======================
        draw_text(screen, "Chroniques du Kraken oublié", font, (255, 255, 255), 200, 100)

        # ======================
        # INPUT BOXES
        # ======================
        pygame.draw.rect(screen, (255, 255, 255), (250, 220, 300, 50), 2)
        pygame.draw.rect(screen, (255, 255, 255), (250, 320, 300, 50), 2)
        pygame.draw.rect(screen, (255, 255, 255), (250, 420, 300, 50), 2)

        draw_text(screen, username, font, (255, 255, 255), 260, 230)
        draw_text(screen, "*" * len(password), font, (255, 255, 255), 260, 330)
        draw_text(screen, "*" * len(confirm_password), font, (255, 255, 255), 260, 430)

        draw_text(screen, "Username", font, (180, 180, 180), 250, 180)
        draw_text(screen, "Password", font, (180, 180, 180), 250, 280)
        draw_text(screen, "Confirm Password", font, (180, 180, 180), 250, 380)

        # ======================
        # BUTTON
        # ======================
        register_button = pygame.Rect(300, 520, 200, 60)
        pygame.draw.rect(screen, (70, 130, 180), register_button)
        draw_text(screen, "Register", font, (255, 255, 255), 340, 537)

        login_button = pygame.Rect(240, 620, 350, 60)
        pygame.draw.rect(screen, (70, 130, 180), login_button)
        draw_text(screen, "Already have an account", font, (255, 255, 255), 250, 637)

        # ======================
        # EVENTS
        # ======================
        ok_rect = popup.draw(screen, font)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            # --- Click ---
            if event.type == pygame.MOUSEBUTTONDOWN:

                # --- close popup first ---
                if popup.active:
                    if ok_rect and ok_rect.collidepoint(event.pos):
                        popup.hide()
                    continue

                # --- input select ---
                if 220 <= event.pos[1] <= 270:
                    active_input = "username"
                elif 320 <= event.pos[1] <= 370:
                    active_input = "password"
                elif 420 <= event.pos[1] <= 470:
                    active_input = "confirm_password"

                # --- register button ---
                if register_button.collidepoint(event.pos):

                    if username == "" or password == "" or confirm_password == "":
                        popup.show("Champs vides")
                        continue

                    if password != confirm_password:
                        popup.show("Les mots de passe \nne correspondent pas")
                        continue

                    success, message = register_user(username, password)

                    if success:
                        popup.show("Compte créé avec succès")
                        return "menu", username
                    else:
                        popup.show(message)

                if login_button.collidepoint(event.pos):
                    return "login"

            # --- Keyboard ---
            if event.type == pygame.KEYDOWN and not popup.active:

                if event.key == pygame.K_BACKSPACE:

                    if active_input == "username":
                        username = username[:-1]
                    elif active_input == "password":
                        password = password[:-1]
                    elif active_input == "confirm_password":
                        confirm_password = confirm_password[:-1]

                else:

                    if event.key not in [pygame.K_RETURN, pygame.K_TAB]:

                        if active_input == "username":
                            username += event.unicode
                        elif active_input == "password":
                            password += event.unicode
                        elif active_input == "confirm_password":
                            confirm_password += event.unicode

        #======================
        # DRAW POPUP LAST (on top)
        #======================
        ok_rect = popup.draw(screen, font)

        pygame.display.update()

