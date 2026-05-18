import pygame
from backend.config.db import get_top_scores


def ranking(screen,username):

    clock = pygame.time.Clock()
    running = True

    font_title = pygame.font.Font(None, 55)
    font_text = pygame.font.Font(None, 32)

    while running:

        scores = get_top_scores()

        screen.fill((20, 20, 30))

        pygame.draw.rect(
            screen,
            (20, 20, 30),
            (140, 40, 520, 620)
        )

        title = font_title.render(
            "Classement joueur",
            True,
            (255, 255, 255)
        )

        screen.blit(title, (250, 80))

        start_x = 190
        start_y = 170
        row_height = 45
        width = 420

        pygame.draw.line(
            screen,
            (255, 255, 255),
            (290, start_y),
            (290, start_y + row_height * 10),
            2
        )

        for i in range(11):
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (start_x, start_y + i * row_height),
                (start_x + width, start_y + i * row_height),
                2
            )

        positions = [
            "1st", "2nd", "3rd", "4th", "5th",
            "6th", "7th", "8th", "9th", "10th"
        ]

        for i, score_data in enumerate(scores):

            username = score_data["username"]
            score = score_data["score"]

            rank = font_text.render(
                positions[i],
                True,
                (255, 255, 255)
            )

            value = font_text.render(
                f"{username} - {score}",
                True,
                (255, 255, 255)
            )

            y = start_y + 10 + i * row_height

            screen.blit(rank, (220, y))
            screen.blit(value, (320, y))

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit", username

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu", username

        clock.tick(60)