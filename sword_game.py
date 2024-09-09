import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game Clock
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5
        self.health = 100
        self.level = 1
        self.exp = 0
        self.money = 50  # Start with some money for items

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def attack(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.health -= 10
                if enemy.health <= 0:
                    enemy.kill()
                    self.exp += 10
                    if self.exp >= 100:
                        self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.health = 100
        print(f'Level Up! You are now level {self.level}.')

    def buy_item(self, item):
        if self.money >= item['cost']:
            self.money -= item['cost']
            if item['type'] == 'sword':
                print("Upgraded sword!")
            elif item['type'] == 'armor':
                self.health += 20
                print("Bought armor!")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
        self.speed = 2
        self.health = 50

    def update(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        if self.rect.y > player.rect.y:
            self.rect.y -= self.speed

# Main game loop
def game_loop():
    player = Player()
    enemies = pygame.sprite.Group()

    for _ in range(5):  # Spawn 5 enemies at the start
        enemies.add(Enemy())

    running = True
    while running:
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        if keys[pygame.K_SPACE]:
            player.attack(enemies)

        # Update enemies
        enemies.update(player)

        # Draw player and enemies
        screen.blit(player.image, player.rect)
        enemies.draw(screen)

        # Display player info
        font = pygame.font.SysFont(None, 36)
        text = font.render(f'Health: {player.health}  Level: {player.level}  Exp: {player.exp}  Money: {player.money}', True, WHITE)
        screen.blit(text, (20, 20))

        # Check if player wants to buy an item
        if keys[pygame.K_b]:  # 'b' to buy item
            sword = {'type': 'sword', 'cost': 30}
            player.buy_item(sword)

        # Refresh the screen
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    game_loop()
