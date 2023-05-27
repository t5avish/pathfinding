import pygame, os
from settings import TILE_SIZE
from data import buttons_assets
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, path):
        super().__init__()
        self.image = pygame.image.load(os.path.dirname(__file__) + buttons_assets['player'])
        self.current_pos = [(x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE]
        self.rect = self.image.get_rect(topleft = (self.current_pos[0], self.current_pos[1]))
        
        self.active = True
        self.path = path
        self.moving = None
        self.direction = pygame.math.Vector2()
        self.speed = 2

        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
    
    def moving_direction(self, origin, destination):
        if origin.x - destination.x < 0:
            self.direction.x = -1
            self.moving = 'left'
        elif origin.x - destination.x > 0:
            self.direction.x = 1
            self.moving = 'right'
        else:
            self.direction.x = 0

        if origin.y - destination.y < 0:
            self.direction.y = -1
            self.moving = 'up'
        elif origin.y - destination.y > 0:
            self.direction.y = 1
            self.moving = 'down'
        else:
            self.direction.y = 0

    def move(self, speed):
        origin = self.path[0]
        destination = self.path[1]

        self.moving_direction(destination, origin)
        self.rect.center += self.direction * speed
        
        if self.rect.topleft == ((destination.x + 1) * 64, (destination.y + 1) * 64):
            self.path.pop(0)

        if len(self.path) == 1:
            self.moving = 'down'
            self.frame_index = 0
            self.active = False

    def import_character_assets(self):
        character_path = os.path.dirname(__file__) + '/../graphics/character/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}
        
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.moving]
        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def update(self):
        if self.active:
            self.move(self.speed)
            self.animate()                          
