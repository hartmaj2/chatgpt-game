import pygame
from sword import Sword

# Constants
PLAYER_START_HEALTH = 100

class Player(pygame.sprite.Sprite):
    """The player controlled by the user."""

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))  # White
        self.rect = self.image.get_rect(center=(400, 300))
        self.health = PLAYER_START_HEALTH
        self.level = 1
        self.exp = 0
        self.money = 50
        self.speed = 5
        self.sword = Sword(self)

    def move(self, keys):
        """Move the player based on key inputs."""
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def attack(self, enemies):
        """Perform an attack in the current direction, checking for collisions."""
        sword_rect = self.sword.get_sword_rect()
        for enemy in enemies:
            if sword_rect.colliderect(enemy.rect):
                enemy.take_damage(self.sword.attack_power)
                if enemy.is_dead():
                    enemy.kill()
                    self.exp += 10
                    self.money += 5
                    self.check_level_up()

    def check_level_up(self):
        """Increase level and reset experience if the player has enough EXP."""
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            self.health = PLAYER_START_HEALTH
            print(f'Level up! Now level {self.level}.')

    def take_damage(self, amount):
        """Reduce player health when damaged by an enemy."""
        self.health -= amount
        if self.health <= 0:
            print("Game Over!")
            pygame.quit()
            quit()
