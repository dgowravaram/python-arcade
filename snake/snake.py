import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass


def drawGrid(w, rows, surface):
    sizeBtwn = w//rows

    x = 0
    y = 0
    for l in range(rows):
        x+=sizeBtwn
        y+=sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))

def redrawWindow(surface):
    global rows, width
    win.fill((0,0,0))
    drawGrid(width, rows,  surface)
    pygame.display.update()


def main():
    global width
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((225,0,0), (10,10)) # red,

    clock = pygame.time.Clock()
    flag = True
    while flag:
        pygame.time.delay(50) # delay so doesn't run too fast
        clock.tick(10) #run 10 blocks in 1 sec

        redrawWindow(win)
