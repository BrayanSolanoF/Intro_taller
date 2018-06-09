import pygame as pg
vec = pg.math.Vector2
#Atributos de color para el juego
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (221,44,0,255)
BRIGHT_RED = (200,0,0)
BRIGHT_GREEN =(0,200,0)

# Configuraciones del juego
WIDTH = 1024  # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "DEATH RACE"
BGCOLOR = DARKGREY
#FONT_NAME = "arial"

TILESIZE = 8
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#Configuraciones del jugador
PLAYER_HEALTH = 100
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'Black_viper.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)




#Configuraciones del muro
WALL_IMG = "barrier_red.png"
GRASS_IMG = "land_grass04.png"
FINISH_IMG = "arrow_yellow.png"
#Configuraciones del disparo
BULLET_IMG = 'Cone.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10



#Configuraciones del dummy vehicle
DUMMY_IMG = "Police.png"
DUMMY_SPEED = 250
DUMMY_HIT_RECT = pg.Rect(0, 0, 35, 35)
DUMMY_HEALTH = 100
DUMMY_DAMAGE = 10
DUMMY_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 300

#Efectos
MUZZLE_FLASHHES = ["whitePuff15.png","whitePuff16.png","whitePuff17.png","whitePuff18.png"]
FLASH_DURATION = 40

#LAYERS

WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
DUMMY_LAYER = 2
EFFECTS_LAYER = 4

#Sounds
BG_MUSIC = "espionage.ogg"
PLAYER_HIT_SOUND = ["420356__eponn__crash.wav"]
DUMMY_SOUND =[ "70938__guitarguy1985__police2.wav"]
WEAPON_SOUNDS_GUN = ['sfx_weapon_singleshot2.wav']
DUMMY_HIT_SOUND =["420356__eponn__crash.wav"]
PLAYER_SOUND = ["formula+1.wav"]





