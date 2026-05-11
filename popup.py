import pygame


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

class Popup:

    def __init__(self):
        self.message = ""
        self.active = False

    def show(self, message):
        self.message = message
        self.active = True

    def hide(self):
        self.active = False

    def draw(self, screen, font):

        if not self.active:
            return

        # background dark overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # popup box
        rect = pygame.Rect(150, 250, 500, 200)
        pygame.draw.rect(screen, (30, 30, 30), rect)
        pygame.draw.rect(screen, (200, 0, 0), rect, 3)

        # message
        draw_text(screen, self.message, font,(255, 255, 255), rect.centerx, rect.y + 70, center=True)

        # button OK
        ok_rect = pygame.Rect(rect.centerx - 50, rect.y + 130, 100, 40)
        pygame.draw.rect(screen, (70, 130, 180), ok_rect)
        draw_text(screen, "OK", font, (255, 255, 255), ok_rect.x + 35, ok_rect.y + 5)

        return ok_rect