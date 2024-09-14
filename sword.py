import pygame

# Constants
SWORD_SWING_DURATION = 200
SWORD_DAMAGE = 10
BLUE = (0, 0, 255)

class Sword:
    """Handles sword behavior and drawing."""

    def __init__(self, player):
        self.player = player
        self.attack_power = SWORD_DAMAGE
        self.sword_swing_time = 0  # Time when sword was last swung
        self.attack_direction = None

    def swing(self, direction):
        """Swing the sword in a given direction."""
        self.attack_direction = direction
        self.sword_swing_time = pygame.time.get_ticks()
        print("swung")

    def get_sword_rect(self):
        """Return the sword's collision rectangle based on the attack direction."""
        if self.attack_direction == 'up':
            return pygame.Rect(self.player.rect.centerx - 10, self.player.rect.top - 20, 20, 40)
        elif self.attack_direction == 'down':
            return pygame.Rect(self.player.rect.centerx - 10, self.player.rect.bottom, 20, 40)
        elif self.attack_direction == 'left':
            return pygame.Rect(self.player.rect.left - 40, self.player.rect.centery - 10, 40, 20)
        elif self.attack_direction == 'right':
            return pygame.Rect(self.player.rect.right, self.player.rect.centery - 10, 40, 20)
        return pygame.Rect(0, 0, 0, 0)

    def draw(self,screen):
        """Draw the sword for a short duration after the swing."""
        if pygame.time.get_ticks() - self.sword_swing_time < SWORD_SWING_DURATION:
            print("display sword")
            sword_rect = self.get_sword_rect()
            pygame.draw.rect(screen, BLUE, sword_rect)

    def upgrade(self, additional_damage):
        """Upgrade the sword's attack power."""
        self.attack_power += additional_damage
