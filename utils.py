import pygame

def draw_text(screen, text, position, color, size=36):
    """Utility function to draw text on the screen."""
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)
