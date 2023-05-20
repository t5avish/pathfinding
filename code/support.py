from csv import reader, writer
from settings import *
from os import walk
import os.path
import pygame

def import_folder(path):
    surface_list = []
    for _, __, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
        return surface_list

def import_csv_layout(path):
    map_list = []
    with open(os.path.dirname(__file__) + path) as map:
        ground = reader(map, delimiter = ',')
        for row in (ground):
            map_list.append(list(row))
    return map_list

def edit_csv_file(path, x, y, value):
    data = import_csv_layout(path)
    if value == 0 or value == 1:
        for row in range(VERTICAL_TILES):
            for col in range(HORIZONTAL_TILES):
                if data[row][col] == str(value):
                    data[row][col] = '-1'

    data[y][x] = value
    with open(os.path.dirname(__file__) + path, 'w+', newline='') as map:
        myFile = writer(map)
        for i in range(len(data)):
            myFile.writerow(data[i])

def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / TILE_SIZE)
    tile_num_y = int(surface.get_size()[1] / TILE_SIZE)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            new_surf = pygame.Surface((TILE_SIZE,TILE_SIZE), flags = pygame.SRCALPHA)
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            cut_tiles.append(new_surf)
    return cut_tiles