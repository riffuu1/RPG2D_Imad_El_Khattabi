import pygame
from popup import Popup
from backend.config.db import login_user


pygame.init()

WIDTH, HEIGHT = 800, 700


# ======================
# TEXT DRAW
# ======================
def draw_text(screen, text, font, color, x, y, center=False):
    # --- handle return to line ---
    lines = text.split("\n")

    for i, line in enumerate(lines):
        img = font.render(line, True, color)

        if center:
            rect = img.get_rect(center=(x, y + i * 40))
            screen.blit(img, rect)
        else:
            screen.blit(img, (x, y + i * 40))

#===================
# LOGIN SCREEN
#===================
def login_screen(screen):


    pygame.display.set_caption("Login")

    font = pygame.font.Font(None, 40)

    username = ""
    password = ""

    active_input = "username"

    popup = Popup()

    running = True

    while running:

        screen.fill((20, 20, 30))

        draw_text(screen, "Login", font, (255, 255, 255), 350, 100)

        pygame.draw.rect(screen, (255, 255, 255), (250, 220, 300, 50), 2)
        pygame.draw.rect(screen, (255, 255, 255), (250, 320, 300, 50), 2)

        draw_text(screen, username, font, (255, 255, 255), 260, 230)
        draw_text(screen, "*" * len(password), font, (255, 255, 255), 260, 330)

        draw_text(screen, "Username", font, (180, 180, 180), 250, 180)
        draw_text(screen, "Password", font, (180, 180, 180), 250, 280)

        login_button = pygame.Rect(300, 450, 200, 60)
        pygame.draw.rect(screen, (70, 130, 180), login_button)
        draw_text(screen, "Login", font, (255, 255, 255), 350, 467)

        register_button = pygame.Rect(240, 550, 320, 60)
        pygame.draw.rect(screen, (70, 130, 180), register_button)
        draw_text(screen, "Don't have an account", font, (255, 255, 255), 250, 567)

        ok_rect = popup.draw(screen, font)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if popup.active:
                    if ok_rect and ok_rect.collidepoint(event.pos):
                        popup.hide()
                    continue

                if 220 <= event.pos[1] <= 270:
                    active_input = "username"
                elif 320 <= event.pos[1] <= 370:
                    active_input = "password"

                if login_button.collidepoint(event.pos):

                    if username == "" or password == "":
                        popup.show("Champs vides")
                        continue

                    success, message = login_user(username, password)
                    if success:
                        popup.show("Connexion réussie")
                        pygame.time.delay(300)
                        return "game"
                    else:
                        popup.show(message)

                if register_button.collidepoint(event.pos):
                    return "register"

            if event.type == pygame.KEYDOWN and not popup.active:

                if event.key == pygame.K_BACKSPACE:

                    if active_input == "username":
                        username = username[:-1]
                    elif active_input == "password":
                        password = password[:-1]

                else:

                    if event.key not in [pygame.K_RETURN, pygame.K_TAB]:

                        if active_input == "username":
                            username += event.unicode
                        elif active_input == "password":
                            password += event.unicode

        pygame.display.update()

