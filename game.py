import pygame
from player import Player
from enemy import Enemy
from store import Store
from utils import draw_text

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
ENEMY_START_HEALTH = 50
ENEMY_START_SPEED = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Game:
    """Main class that runs the game logic."""

    def __init__(self):
        self.player = Player()
        self.enemies = pygame.sprite.Group()
        self.store = Store(self.player)
        self.wave_number = 1
        self.running = True

    def spawn_wave(self, wave_number: int):
        """Spawn a new wave of enemies."""
        num_enemies = 5 + wave_number
        enemy_health = ENEMY_START_HEALTH + wave_number * 10
        enemy_speed = ENEMY_START_SPEED + wave_number * 0.5
        for _ in range(num_enemies):
            self.enemies.add(Enemy(health=enemy_health, speed=enemy_speed))

    def game_loop(self):
        """Main game loop that updates the game state."""
        self.spawn_wave(self.wave_number)

        while self.running:
            screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            # Handle player attacks
            if keys[pygame.K_w]:
                self.player.sword.swing('up')
                self.player.attack(self.enemies)
            elif keys[pygame.K_s]:
                self.player.sword.swing('down')
                self.player.attack(self.enemies)
            elif keys[pygame.K_a]:
                self.player.sword.swing('left')
                self.player.attack(self.enemies)
            elif keys[pygame.K_d]:
                self.player.sword.swing('right')
                self.player.attack(self.enemies)

            # Update enemies
            self.enemies.update(self.player)

            # Draw player, sword, and enemies
            screen.blit(self.player.image, self.player.rect)
            self.player.sword.draw(screen)
            self.enemies.draw(screen)

            # Display player stats
            draw_text(screen, f'Health: {self.player.health}', (20, 20), WHITE)
            draw_text(screen, f'Level: {self.player.level}', (20, 60), WHITE)
            draw_text(screen, f'Money: {self.player.money}', (20, 100), WHITE)

            # Check for wave completion
            if len(self.enemies) == 0:
                self.store.show()
                self.wave_number += 1
                self.spawn_wave(self.wave_number)

            pygame.display.flip()
            clock.tick(FPS)

# Run the game
if __name__ == "__main__":
    game = Game()
    game.game_loop()
    pygame.quit()
