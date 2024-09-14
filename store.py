import pygame
from utils import draw_text

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Store:
    """Handles the store between waves, allowing the player to buy items."""

    def __init__(self, player):
        self.player = player

    def show(self):
        """Display the store and allow the player to buy items."""
        store_active = True
        while store_active:
            pygame.display.get_surface().fill(BLACK)
            draw_text(pygame.display.get_surface(), f'Money: {self.player.money}', (20, 20), WHITE)
            draw_text(pygame.display.get_surface(), '1. Sword (+5 damage): 50', (20, 80), WHITE)
            draw_text(pygame.display.get_surface(), '2. Health Potion (+50 HP): 30', (20, 120), WHITE)
            draw_text(pygame.display.get_surface(), '3. Exit Store', (20, 160), WHITE)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 and self.player.money >= 50:
                        self.player.sword.upgrade(5)
                        self.player.money -= 50
                    elif event.key == pygame.K_2 and self.player.money >= 30:
                        self.player.health = min(self.player.health + 50, 100)
                        self.player.money -= 30
                    elif event.key == pygame.K_3:
                        store_active = False
