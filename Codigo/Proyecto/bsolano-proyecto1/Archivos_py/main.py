import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from map import *



#Clase principal
class Game:
    def __init__(self):
        pg.init()
        #Dimension de ventana
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        #Titulo de juego
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        #pg.key.set_repeat(500, 100)
        self.load_data()

    #Mediante este metodo se logran cargar los diferentes archivos
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'img')
        self.map = Map(path.join(game_folder))
        self.player_img = pg.image.load(path.join(img_folder,PLAYER_IMG)).convert_alpha()
        self.dummy_img = pg.image.load(path.join(img_folder, DUMMY_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img,(TILESIZE, TILESIZE))
        self.linelap_img = pg.image.load(path.join(img_folder, LINELAP_IMG)).convert_alpha()
        self.linelap_img = pg.transform.scale(self.linelap_img, (TILESIZE, TILESIZE))
        self.pasto_img = pg.image.load(path.join(img_folder, PASTO_IMG)).convert_alpha()
        self.pasto_img = pg.transform.scale(self.pasto_img, (TILESIZE, TILESIZE))
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.bullet_img = pg.transform.scale(self.bullet_img, (TILESIZE, TILESIZE))

    #mediante este metodo se inicializan las variables que intervienen en el juego
    def new(self):

        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.linelap = pg.sprite.Group()
        self.pasto = pg.sprite.Group()
        self.dummys = pg.sprite.Group()

        #Se sustituye cada parte del mapa por el objeto que se necesita
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'p':
                    self.player = Player(self, col, row)
                if tile == 'd':
                     Dummy(self, col, row)
                if tile =='h':
                   lapline(self, col, row)
                if tile == 'o':
                   pasto(self, col, row)
        self.bullets = pg.sprite.Group()



    #Loop del juego
    def run(self):

        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()
    #actualizar el loop
    def update(self):

        self.all_sprites.update()

    #Se realiza el mapeo para localizar los objetos en el mapa
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    #se definen caracteristicas de la ventana
    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        pg.display.flip()


    #Mediante este metodo se realizan los eventos principales
    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()








g = Game()

while True:
    g.new()
    g.run()
    g.show_go_screen()
