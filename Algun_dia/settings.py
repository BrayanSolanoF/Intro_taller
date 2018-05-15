import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (221,44,0,255)

# game settings0
WIDTH = 1024  # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "DEATH RACE"
BGCOLOR = DARKGREY

TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'Black_viper.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)


#WALL SETTINGS
WALL_IMG = "barrier_red.png"
PASTO_IMG = "land_grass04.png"
LINELAP_IMG = "arrow_yellow.png"
#Gun settings
BULLET_IMG = 'Cone.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150

#text
font_name = pg.font.match_font('arial')

#dummy setttings
DUMMY_IMG = "Police.png"
DUMMY_SPEED = 250
DUMMY_HIT_RECT = pg.Rect(0, 0, 35, 35)






