import pygame as pg
import sys
from os import path
from settingsnew import *
from spritesnew import *
from mapnew import *
#from menu import *
#from mapnewtwo import

# pg.init()

def draw_player_health(surf,x,y,pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect = pg.Rect(x,y,fill,BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col =RED
    pg.draw.rect(surf,col,fill_rect)
    pg.draw.rect(surf,WHITE,outline_rect, 2)


#Clase principal
class Game:
    def __init__(self):

        #Dimension de ventana
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        #Titulo de juego
        pg.display.set_caption(TITLE)

        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        #self.font_name = pg.font.match_font(FONT_NAME)

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        name = "Username: "
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    #Mediante este metodo se logran cargar los diferentes archivos
    def load_data(self):
        game_folder = path.dirname(__file__)
        snd_folder = path.join(game_folder,'snd')
        music_folder = path.join(game_folder,'music')
        img_folder = path.join(game_folder,'img')
        self.tittle_font = path.join(img_folder, "Techno.ttf")
        self.hud_font = path.join(img_folder,"Impacted2.0.ttf")
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0,0,0,180))
        self.map = Map(path.join(game_folder))
        #self.map = Maptwo(path.join(game_folder))
        self.player_img = pg.image.load(path.join(img_folder,PLAYER_IMG)).convert_alpha()
        self.dummy_img = pg.image.load(path.join(img_folder, DUMMY_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img,(TILESIZE, TILESIZE))
        self.finish_img = pg.image.load(path.join(img_folder, FINISH_IMG)).convert_alpha()
        self.finish_img = pg.transform.scale(self.finish_img, (TILESIZE, TILESIZE))
        self.grass_img = pg.image.load(path.join(img_folder, GRASS_IMG)).convert_alpha()
        self.grass_img = pg.transform.scale(self.grass_img, (TILESIZE, TILESIZE))
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.bullet_img = pg.transform.scale(self.bullet_img, (TILESIZE, TILESIZE))
        self.gun_flashes = []
        for img in MUZZLE_FLASHHES:
            self.gun_flashes.append(pg.image.load(path.join(img_folder, img)).convert_alpha())
        #Sounda
        pg.mixer.music.load(path.join(music_folder,BG_MUSIC))
        # self.effects = {}
        # for type in EFFECTS_SOUNDS:
        #     self.effects_sounds[type] = pg.mixer.Sound(path.join(snd_folder, EFFECTS_SOUNDS[type]))
        self.weapon_sounds = {}
        self.weapon_sounds["gun"] = []
        for snd in WEAPON_SOUNDS_GUN:
            self.weapon_sounds["gun"].append(pg.mixer.Sound(path.join(snd_folder,snd)))
        self.dummy_sounds = []
        for snd in DUMMY_SOUND:
            s = pg.mixer.Sound(path.join(snd_folder,snd))
            s.set_volume(1)
            self.dummy_sounds.append(s)
        self.player_hit_sounds = []
        for snd in PLAYER_HIT_SOUND:
            self.player_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd)))
        self.dummy_hit_sounds = []
        for snd in DUMMY_HIT_SOUND:
            self.dummy_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd)))
        self.player_sounds = []
        # for snd in PLAYER_SOUND:
        #     s = pg.mixer.Sound(path.join(snd_folder, snd))
        #     s.set_volume(0.01)
        #     self.player_sounds.append(s)




    #mediante este metodo se inicializan las variables que intervienen en el juego
    def new(self):
        #self.score = 0
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.players = pg.sprite.Group()
        self.finish = pg.sprite.Group()
        self.grass = pg.sprite.Group()
        self.dummys = pg.sprite.Group()
        self.paused = False
        self.hits = pg.sprite.Group()
       #self.effects_sounds["level_start"].play()



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
                   finish(self, col, row)
                if tile == 'o':
                   grass(self, col, row)
        self.bullets = pg.sprite.Group()



    #Loop del juego
    def run(self):

        self.playing = True
        pg.mixer.music.play(loops=-1)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            if not self.paused:
                self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()
    #actualizar el loop
    def update(self):

        self.all_sprites.update()
        #Dummy golpea jugador
        hits = pg.sprite.spritecollide(self.player, self.dummys, False, collide_hit_rect)
        for hit in hits:
            if random() < 0.7:
                choice(self.player_hit_sounds).play()
            self.player.health -= DUMMY_DAMAGE
            hit.vel = vec(0,0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.pos += vec(DUMMY_KNOCKBACK, 0).rotate(-hits[0].rot)

        #disparos matan dummys
        hits = pg.sprite.groupcollide(self.dummys, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DAMAGE
            hit.vel = vec(0,0)
        #hits = pg.sprite.groupcollide(self.player, self.finish)




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

        for sprite in self.all_sprites:
            if isinstance(sprite,Dummy):
                sprite.draw_health()
        self.all_sprites.draw(self.screen)
        self.draw_text("Score:{}".format(len(self.dummys)),self.hud_font,30, WHITE,WIDTH/2, HEIGHT/2,align="center")
        if self.paused:
            self.screen.blit(self.dim_screen,(0, 0))
            self.draw_text("Paused",self.tittle_font, 105, RED, WIDTH/2, HEIGHT/2, align="center")
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
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
                if event.key == pg.K_p:
                    self.paused = not self.paused






    def show_go_screen(self):
        pass
    #     self.screen.fill(BLACK)
    #     self.draw_text("GAME OVER", self.title_font, 100, RED,
    #                    WIDTH / 2, HEIGHT / 2)
    #     self.draw_text("Press a key to start", self.title_font, 75, WHITE,
    #                    WIDTH / 2, HEIGHT * 3 / 4)
    #     pg.display.flip()
    #     self.wait_for_key()
    #
    # def wait_for_key(self):
    #     pg.event.wait()
    #     waiting = True
    #     while waiting:
    #         self.clock.tick(FPS)
    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 waiting = False
    #                 self.quit()
    #             if event.type == pg.KEYUP:
    #                 waiting = False
    #
    # def draw_text_score(self, text, size, color, x, y):
    #     font = pg.font.Fo nt(self.font_name, size)
    #     text_surface = font.render(text, True, color)
    #     text_rect = text_surface.get_rect()
    #     text_rect.midtop =(x,y)
    #     self.screen.blit(text_surface, text_rect)


# g = Game()
# g.show_start_screen()
# #g.name
# #g.inpt()
# while True:
#     g.new()
#     g.run()
#     g.show_go_screen()
