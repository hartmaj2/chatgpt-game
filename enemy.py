import pygame
import random

class Enemy(pygame.sprite.Sprite):
    """Enemies that attack the player."""

    def __init__(self, health: int, speed: float):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Red
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 600)
        self.speed = speed
        self.health = health

    def update(self, player):
        """Move towards the player and deal damage if colliding."""
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        if self.rect.y > player.rect.y:
            self.rect.y -= self.speed

        # Deal damage if touching the player
        if self.rect.colliderect(player.rect):
            player.take_damage(5)
            self.kill()

    def take_damage(self, amount: int):
        """Reduce enemy health when attacked."""
        self.health -= amount

    def is_dead(self):
        """Return True if the enemy's health is 0 or less."""
        return self.health <= 0
