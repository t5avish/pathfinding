import pygame, os
from settings import *
from data import buttons_assets

class Menu:
    def __init__(self, width, height):
        self.display_surface = pygame.display.get_surface()
        self.width = width
        self.height = height
        self.active = True
        self.create_buttons()

    def create_buttons(self):
        button_margin = 5
        topleft = (WIDTH*(1/3) - TILE_SIZE / 2, HEIGHT - self.height - 20)
        self.rect = pygame.Rect(topleft, (self.width, self.height))

        self.generic_button_rect = pygame.Rect(self.rect.topleft, (self.width / 6, self.rect.height))
        self.player_button_rect = self.generic_button_rect.copy().inflate(-button_margin, -button_margin)
        self.chest_button_rect = self.generic_button_rect.move(self.width / 6, 0).inflate(-button_margin, -button_margin)
        self.obstacle_button_rect = self.generic_button_rect.move(self.width / 6 * 2, 0).inflate(-button_margin, -button_margin)
        self.eraser_button_rect = self.generic_button_rect.move(self.width / 6 * 3, 0).inflate(-button_margin, -button_margin)
        self.start_button_rect = self.generic_button_rect.move(self.width / 6 * 4, 0).inflate(-button_margin, -button_margin)
        self.reset_button_rect = self.generic_button_rect.move(self.width / 6 * 5, 0).inflate(-button_margin, -button_margin)

        self.buttons = pygame.sprite.Group()
        Button(self.player_button_rect,0,self.buttons, buttons_assets['player'])
        Button(self.chest_button_rect,1,self.buttons, buttons_assets['chest'])
        Button(self.obstacle_button_rect,2,self.buttons, buttons_assets['obstacle'])
        Button(self.eraser_button_rect,-1,self.buttons, buttons_assets['eraser'])
        Button(self.start_button_rect, -2,self.buttons, buttons_assets['start'])
        Button(self.reset_button_rect, -3,self.buttons, buttons_assets['reset'])
    
    def click(self, mouse_pos, mouse_button):
        for sprite in self.buttons:
            if sprite.rect.collidepoint(mouse_pos):
                return sprite.index

    def highlight(self, index):
        if index == 0:
            pygame.draw.rect(self.display_surface, BUTTON_LINE_COLOR, self.player_button_rect.inflate(4,4), 5, 4)
        elif index == 1:
            pygame.draw.rect(self.display_surface, BUTTON_LINE_COLOR, self.chest_button_rect.inflate(4,4), 5, 4)
        elif index == 2:
            pygame.draw.rect(self.display_surface, BUTTON_LINE_COLOR, self.obstacle_button_rect.inflate(4,4), 5, 4)
        elif index == -1:
            pygame.draw.rect(self.display_surface, BUTTON_LINE_COLOR, self.eraser_button_rect.inflate(4,4), 5, 4)
        
    def display(self, index):
        self.buttons.update()
        self.buttons.draw(self.display_surface)
        if self.active:
            self.highlight(index)

class Button(pygame.sprite.Sprite):
    def __init__(self, rect, index ,group, path):
        super().__init__(group)
        self.image = pygame.Surface(rect.size)
        surf = pygame.image.load(os.path.dirname(__file__) + path).convert_alpha()
        self.surf = pygame.transform.scale(surf, (TILE_SIZE * 0.75, TILE_SIZE * 0.75))
        self.rect = rect
        self.index = index
    
    def update(self):
        self.image.fill(BUTTON_BG_COLOR)
        rect = self.surf.get_rect(center = (self.rect.width/2, self.rect.height / 2))
        self.image.blit(self.surf, rect)