import pygame as pg
from settings import *



#Clase para mapear el juego
class Map:
    def __init__(self, filename):
        self.data = []
        testList = [
            '1111111111111111111111111111111111111111111111111111111111111111',
            '1..............................................................1',
            '1..............................................................1',
            '1..............................................................1',
            '1..............................................................1',
            '1.......111111111111111111111111111111111111111111111111.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1hhhhhhh1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.p..d..1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......1oooooooooooooooooooooooooooooooooooooooooooooo1.......1',
            '1.......111111111111111111111111111111111111111111111111.......1',
            '1..............................................................1',
            '1..............................................................1',
            '1..............................................................1',
            '1..............................................................1',
            '1111111111111111111111111111111111111111111111111111111111111111',



        ]
        for i in testList:
            self.data.append(i)

