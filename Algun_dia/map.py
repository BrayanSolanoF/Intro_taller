import pygame as pg
from settings import *
from PIL import Image



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

#     #self.listRGB = ([1,0,0])
    #     image = Image.open(filename)
    #     x = np.array(image)
    #     map =''
    #     for i in x:
    #         for y in i:
    #             if(self.detectSame(y,[0,0,0,255])):
    #                 map += '1'
    #             elif(self.detectSame(y,[221,44,0,255])):
    #                 map +='p'
    #             else:
    #                 map += '.'
    #         self.data.append(map)
    #         map = ''
    #
    #
        # self.tilewidth = len(self.data[0])
        # self.tileheight = len (self.data)
        # self.width = self.tilewidth = TILESIZE
        # self.height = self.tileheight = TILESIZE
    #
    # def detectSame(self,a, b):
    #     for i in range(len(a)):
    #         if (a[i] != b[i]):
    #             return False
    #     return True

    #def detectmany_RGB(self,a):
        #for rgb in self.listRGB:
            #if(self.detectSame(a,rgb)):
                #return True
        #return False
