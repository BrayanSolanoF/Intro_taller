import pygame as pg
from random import uniform, choice, randint, random
from settingsnew import *
from collidenew import *
vec = pg.math.Vector2


#Mediante este metodo se definen las colisiones con los muros o limites del mapa
def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.velx = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y


#Clase jugador para definir sus caracteristicas, posicion y asigancion de teclas.
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        # print("x", self.x)
        # print("y", self.y)
        self.rot = 0
        self.last_shot = 0
        self.health = PLAYER_HEALTH



    #asignacion de teclas jugador
    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
        if keys[pg.K_z]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_x]:
            self.rot_speed = -PLAYER_ROT_SPEED
        # if keys[pg.K_c]:
        #     self.rot_speed = PLAYER_ROT_SPEED
        # if keys[pg.K_v]:
        #     self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = self.pos + BARREL_OFFSET.rotate(-self.rot)
                bullet(self.game, pos, dir )
                self.vel = vec(-KICKBACK, 0).rotate(-self.rot)
                choice(self.game.weapon_sounds["gun"]).play()
                MuzzleFlash(self.game, pos)


        #print(self.pos.x,self.pos.y)
        self.detectGoal(self.pos.x,self.pos.y)







    # def collide_with_walls(self, dir):
    #
    #     if dir == 'x':
    #         hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
    #         if hits:
    #             if  self.vel.x > 0:
    #                 self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
    #             if self.vel.x < 0:
    #                 self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
    #             self.vel.x = 0
    #             self.hit_rect.centerx = self.pos.x
    #     if dir == 'y':
    #         hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
    #         if hits:
    #             if self.vel.y > 0:
    #                 self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
    #             if self.vel.y < 0:
    #                 self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
    #             self.vel.y = 0
    #             self.hit_rect.centery = self.pos.y







    #colision con linea de meta
    def collide_with_finish(self,dir):
        self.detectGoal(self.pos.x, self.pos.y)
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.finish, False, collide_hit_rect)
            #print("1")
            if hits:
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.finish, False, collide_hit_rect)
            #print('2')
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
                    #self.score += 1
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
                    # print("----------------------")
                    #
                    # self.laps += 1
                    # print(self.laps)
                    # print("----------------------")
                    # return self.laps



                self.vel.y = 0
                self.hit_rect.centery = self.pos.y




    #Metodo para la implementacion de cesped al centro
    def collide_with_grass(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.grass, False, collide_hit_rect)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.velx = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.grass, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y

    def collide_with_Dummy(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.Dummy, False, collide_hit_rect)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.velx = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.Dummy, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y




    #Update del jugador
    def update(self):
        #choice(self.game.player_sounds).play()
        self.get_keys()
        self.rot =(self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls,'x')
        self.collide_with_finish("x")
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls,'y')
        self.collide_with_finish("y")
        self.rect.center = self.hit_rect.center


    def detectGoal(self,x,y):
        if (int(x) == 465 and int(y) in range(25,142)):
            print("lap")


#clase para los disparos
class bullet(pg.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self._layer = BULLET_LAYER
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-GUN_SPREAD,GUN_SPREAD)
        self.vel = dir.rotate(spread) * BULLET_SPEED
        self.spawn_time = pg.time.get_ticks()
   #actualizacion de cada disparo
    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pg.time.get_ticks() - self.spawn_time > BULLET_LIFETIME:
            self.kill()

#Clase para el dummy vehicle
class Dummy(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = DUMMY_LAYER
        self.groups = game.all_sprites, game.dummys
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.dummy_img.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = DUMMY_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.rect.center = self.pos
        self.rot = 0
        self.health = DUMMY_HEALTH
        #self.speed = choice(DUMMY_SPEED)
        self.target = game.player

    def avoid_dummys(self):
        for dummy in self.game.dummys:
            if dummy != self:
                dist = self.pos - dummy.pos
                if 0 < dist.length() < AVOID_RADIUS:
                    self.acc += dist.normalize()


    def collide_with_walls(self, dir):

        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y

    # # #actualizacion de el dummy vehicle en cuanto posicion, angulo y colision
    def update(self):
        target_dist = self.target.pos - self.pos
        if target_dist.length_squared() < DETECT_RADIUS**2:
            if random() < 0.002:
                choice(self.game.dummy_sounds).play()
            self.rot = target_dist.angle_to(vec(1,0))
            self.image = pg.transform.rotate(self.game.dummy_img, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.acc = vec(DUMMY_SPEED, 0).rotate(-self.rot)
            self.acc += self.vel * -1
            self.vel += self.acc * self.game.dt
            self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
            self.hit_rect.centerx = self.pos.x
            self.collide_with_walls("x")
            self.hit_rect.centery = self.pos.y
            self.collide_with_walls("y")
            self.rect.center = self.hit_rect.center
        if self.health <= 0:
            choice(self.game.dummy_hit_sounds).play()
            self.kill()

    def draw_health(self):
        if self.health > 60:
            col = GREEN
        elif self.health > 30:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width* self.health / DUMMY_HEALTH)
        self.health_bar = pg.Rect(0,0,width,7)
        if self.health < DUMMY_HEALTH:
            pg.draw.rect(self.image, col, self.health_bar)



class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = WALL_LAYER
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class finish(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.finish
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.finish_img
        self.rect = self.image.get_rect()
        self.x = x
        #print("x", self.x)
        self.y = y
        #print("y", self.y)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class grass(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.grass
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.grass_img
        self.rect = self.image.get_rect()
        self.x = x

        self.y = y

        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class MuzzleFlash(pg.sprite.Sprite):
    def __init__(self,game, pos):
        self._layer = EFFECTS_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        size = randint(20,50)
        self.image = pg.transform.scale(choice(game.gun_flashes),(size,size))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = pos
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.spawn_time > FLASH_DURATION:
            self.kill()












