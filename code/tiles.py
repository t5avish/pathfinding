import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y, surface):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(bottomleft = (x, y))
        self.image = surface
