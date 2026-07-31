import pygame

pygame.init()

fenster = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mein erstes Pygame-Spiel")

    fenster.fill((30, 40, 60))

    pygame.draw.circle(
        fenster,
        (255, 180, 50),
        (400, 300),
        60
    )

    pygame.display.flip()
    uhr.tick(60)

pygame.quit()