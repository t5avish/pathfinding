import pygame, os.path, sys
from settings import *
from tiles import Tile
from support import *
from data import *
from menu import Menu
from graph import Graph
from player import Player

class Editor():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reset_objects()
        
        self.ground_layout = import_csv_layout(map_assets['ground'])
        self.ground_sprites = self.create_tile_group(self.ground_layout, 'ground')

        self.menu = Menu(540, 70)
        self.selection_index = None
        self.active = True
        
        self.objects_layout = import_csv_layout(map_assets['objects'])
        self.player = pygame.sprite.GroupSingle()

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = (col_index * TILE_SIZE)
                    y = ((row_index + 1) * TILE_SIZE)
                    if type == 'ground':
                        ground_tile_list = import_cut_graphics(os.path.dirname(__file__) + '/../graphics/tiles/ground.png')
                        tile_surface = ground_tile_list[int(val)]
                        sprite = Tile(TILE_SIZE, x, y, tile_surface)    
                        
                    if type == 'objects':
                        objects_tile_list = import_cut_graphics(os.path.dirname(__file__) + '/../graphics/tiles/objects.png')
                        tile_surface = objects_tile_list[int(val)]
                        sprite = Tile(TILE_SIZE, x , y ,tile_surface)
                    sprite_group.add(sprite)
        return sprite_group
    
    def get_clicked_cell(self):
        x = int(pygame.mouse.get_pos()[0] / TILE_SIZE)
        y = int(pygame.mouse.get_pos()[1] / TILE_SIZE)
        if x < 1 or x > 19 or y < 1 or y > 9 or (x % 2 == 0 and y % 2 == 0):
            x = -1
            y = -1
        else:
            x -= 1
            y -= 1
        return x, y

    def menu_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.menu.rect.collidepoint(pygame.mouse.get_pos()):
            self.selection_index = self.menu.click(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
            if self.selection_index == -2:
                self.path_finding()
            if self.selection_index == -3:
                self.reset()

    def add_object(self):
        cords = self.get_clicked_cell()
        if cords == (-1,-1) or self.selection_index is None or self.selection_index < -1:
            return
        edit_csv_file(map_assets['objects'], (cords[0]+1),cords[1]+1, self.selection_index)
        
    def setup_objects(self):
        self.objects_layout = import_csv_layout(map_assets['objects'])
        self.objects_sprites = self.create_tile_group(self.objects_layout, 'objects')
        self.objects_sprites.draw(self.display_surface)
        self.objects_sprites.update()
    
    def reset_objects(self):
        for x in range(VERTICAL_TILES-1):
            for y in range(HORIZONTAL_TILES-1):
                edit_csv_file(map_assets['objects'], y, x, -1)

    def path_finding(self):
        path = None
        graph = Graph(self.ground_layout, self.objects_layout)
        path = graph.get_path()

        if path is None:
            return
        self.active = False
        self.menu.active = False
        edit_csv_file(map_assets['objects'], graph.player_vertex.x + 1, graph.player_vertex.y + 1, -1)
        sprite = Player(graph.player_vertex.x, graph.player_vertex.y, path)
        self.player.add(sprite)

    def reset(self):
        self.reset_objects()
        if len(self.player.sprites()) != 0:
            self.player.sprite.kill()
        self.selection_index = None
        self.active = True
        self.menu.active = True

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.reset_objects()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.active:
                    self.add_object()
            self.menu_click(event)

    def run(self):
        self.event_loop()
        self.ground_sprites.update()
        self.ground_sprites.draw(self.display_surface)
        self.setup_objects()
        self.player.update()
        self.player.draw(self.display_surface)
        self.menu.display(self.selection_index)
