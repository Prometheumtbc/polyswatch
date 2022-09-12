from os import listdir
import pygame as pg; from pygame.locals import *                # import only pygame constants
import importlib
import os, sys, time

# Load

def recursiveEnumerate(folder, file_list):                      # iterate through file directories and export module paths to list
    items = os.listdir(folder)
    for item in items:
        file = folder + '.' + item
        path = folder + '/' + item
        if os.path.isfile(path):
            file_list.append(file)
        elif os.path.isdir(path):
            recursiveEnumerate(file, file_list)
    

def importFiles(files):                                         # import files using pre-generated paths
    for file in files:
        importlib.import_module(file[0:-3])

# On Load

clock = pg.time.Clock()
start_time = time.time()
sys.dont_write_bytecode = True                                  # prevents python writing to cache

object_files = []
recursiveEnumerate('objects', object_files)
importFiles(object_files)                                       # import all object files
room_files = []
recursiveEnumerate('objects', room_files)
importFiles(room_files)

pg.init()
fps = 60
vec = pg.math.Vector2

DISPLAY = pg.display.Info()

display_surface = pg.display.set_mode((DISPLAY.current_w, DISPLAY.current_h))
pg.display.set_caption("Polyswatch")

