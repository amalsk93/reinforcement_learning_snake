import pygame
import random
import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox
import sys

width = 500
cell_size = 25
flag = True
win = pygame.display.set_mode((width, width))
clock = pygame.time.Clock()


class Cube():
    def __init__(self, color=(255, 0, 0), size=cell_size, pos=None):
        if pos is None:
            pos = [250, 250]
        self.color = color
        self.size = size
        self.pos = pos

    def create_cube(self, surf):
        x = self.pos[0]
        y = self.pos[1]
        pygame.draw.rect(surf, self.color, (x, y, x + self.size, y + self.size))


def draw_grids(wid=width, size=cell_size):
    xpos = 0
    for i in range(0, wid, size):
        xpos = xpos + i
        pygame.draw.line(win, (0, 0, 0), (i, 0), (i, wid), 1)
        pygame.draw.line(win, (0, 0, 0), (0, i), (wid, i), 1)


def generate_snack_cube(width):
    x_pos = random.randrange(0, 500, 10)
    y_pos = random.randrange(0, 500, 10)
    return x_pos, y_pos


while flag:
    win.fill((255, 255, 255))
    draw_grids(win, width, cell_size)
    pygame.display.update()
    pygame.time.delay(50)
    clock.tick(10)
    flag = False
