import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from map import *
#from tilemap import *
from menu import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    # def draw_text(self, text, font_name, size, color, x, y, align="nw"):
    #     font = pg.font.Font(font_name, size)
    #     text_surface = font.render(text, True, color)
    #     text_rect = text_surface.get_rect()
        # if align == "nw":
        #     text_rect.topleft = (x, y)
        # if align == "ne":
        #     text_rect.topright = (x, y)
        # if align == "sw":
        #     text_rect.bottomleft = (x, y)
        # if align == "se":
        #     text_rect.bottomright = (x, y)
        # if align == "n":
        #     text_rect.midtop = (x, y)
        # if align == "s":
        #     text_rect.midbottom = (x, y)
        # if align == "e":
        #     text_rect.midright = (x, y)
        # if align == "w":
        #     text_rect.midleft = (x, y)
        # if align == "center":
        #     text_rect.center = (x, y)
        #self.screen.blit(text_surface, text_rect)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'img')
        self.map = Map(path.join(game_folder,'pixil-frame-0.png'))
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


    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.linelap = pg.sprite.Group()
        self.pasto = pg.sprite.Group()
        self.dummys = pg.sprite.Group()


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



        #self.camera = Camera(self.map.width, self.map.height)
        self.bullets = pg.sprite.Group()

    # def message_display(text):
    #     largeText = pg.font.Font('freesansbold.ttf',115)
    #     TextSurf, TextRect = text_objects(text, largeText)
    #     TextRect.center = ((display_width/2),(display_height/2))
    #     gameDisplay.blit(TextSurf, TextRect)
    #
    #     pg.display.update()
    #
    #     time.sleep(2)



    # def game_menu(self):
    #     menu = True
    #     while menu:
    #         for event in pg.event.get():
    #             if event.type ==pg .QUIT:
    #                 pg.quit()
    #                 quit()
    #
    #         gameDisplay.fill(WHITE)
    #         largeText = pg.font.Font('freesansbold.ttf',115)
    #         TextSurf, TextRect = text_objects("DEATH RACE", largeText)
    #         TextRect.center = ((display_width/2),(display_height/2))
    #         gameDisplay.blit(TextSurf, TextRect)
    #         pg.display.update()
    #         clock.tick(15)



    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        #self.camera.update(self.player)
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))

        self.screen.fill(BGCOLOR)
        #self.draw_grid()
        self.all_sprites.draw(self.screen)
        # self.font = pg.font.Font(font_name, size)
        # self.text_surface = font.render(text, True, WHITE)
        # self.text_rect = text_surface.get_rect()
        # self.text_rect.midtop = (x, y)
        # self.surf.blit(text_surface, text_rect)
        # self.draw_text(self.screen, str(lap), 18, WIDTH / 2, 10)
        #for sprite in self.all_sprites:
            #self.screen.blit(sprite.image, self.camera.apply(sprite))
        #pg.draw.rect(self.screen, WHITE, self.camera.apply(self.player), 2)
        pg.display.flip()



    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    # def text_objects(self,text,font):
    #     textSurface = font.render(text, True, BLACK)
    #     return textSurface, textSurface.get_rect()

    #def show_start_screen(self):
    #     self.screen.fill(LIGHTGREY)
    #     self.draw_text(self,"DEATH RACE",'freesansbold.ttf', 100, RED, WIDTH / 2, HEIGHT / 2,)
    #     self.draw_text(self,"Press a key to start",'freesansbold.ttf', 75, WHITE, WIDTH / 2, HEIGHT * 3 / 4,)
    #     pg.display.flip()
    #     self.wait_for_key()


    #def show_go_screen(self):
    #    self.screen.fill(BLACK)
    #     self.draw_text("GAME OVER", self.title_font,100, RED, WIDTH/2, HEIGHT/2, align="center")
    #     self.draw_text("Press a key to start", self.tittle_font, 75, WHITE, WIDTH/2, HEIGHT * 3/4, align="center")
    #     pg.display.flip()
    #     self.wait_for_key()

    # def wait_for_key(self):
    #     waiting = True
    #     while waiting:
    #         self.clock.tick(FPS)
    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 waiting = False
    #                 self.quit()
    #
    #
    #         self.mouse = pg.mouse.get_pos()
    #         self.click = pg.mouse.get_pressed()
    #
    #         print(self.mouse)
    #         print(self.click)




# create the game object

g = Game()
#g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
