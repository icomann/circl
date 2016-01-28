#!/bin/python2

print "Loading engine"
import engine
print "Loading maps"
import mapinfo
print "Loading languages"
import locale
print "Loading pygame"
import pygame
print "Loading configuration"
import config
import sprite
from comp import folder
from time import clock

while True: ##map select
    mp = int(raw_input('Choose Map> '))
    if mp >= 0 and mp < len(mapinfo.ssyslist):
        mp = mapinfo.ssyslist[mp]
        break

print mp








class gamestate:
    def __init__(self, mp, mode, time, playerlist, resp):
        self.ssys = mp
        self.mode = mode
        self.timeleft = time
        self.respawntime = resp
        self.playerlist = set(playerlist)
        self.playerc = len(self.playerlist)
        self.itemset= set()
        self.projset = set()
        self.mainrender = pygame.Surface((self.ssys.radius*2, self.ssys.radius*2)).convert()
        self.bg = pygame.Surface(self.mainrender.get_size()).convert()

        try:
            a = pygame.image.load(folder('sprites', 'maps', 'wea'))
        except:
            a = pygame.image.load(folder('sprites', 'maps', "default.png"))

        pygame.transform.scale(a, self.mainrender.get_size())
        a.convert()
        self.bg.blit(a, (0,0))
        del a

        for plan in self.ssys.planets:
            pygame.draw.circle(self.bg, plan.color, (plan.vPos.x-plan.radius, plan.vPos.y-plan.radius), plan.radius)

        self.mainrender.blit(self.bg, (0,0))

        p = 0
        for player in self.playerlist:
            player.pov = pygame.Surface((config.grw/self.playerc, config.grh))
            player.povpos = (p*config.grw/self.playerc, config.grh)
            p += 1


def physloop(gs, dT):
    for player in gs.playerlist:
        player.phsobj.tick(dT)#get forces later
        player.phsobj.movement(dT,1)
    for bullet in gs.projset:
        bullet.movement(dT)

    #HITSCAN KOMMT HIER

    for player in gs.playerlist:
        player.phsobj.move()
    for bullet in gs.projset:
        bullet.phsobj.move()


def spawnloop(gs, dT):
    for player in gs.playerlist:
        if player.ded != 0:
            if player.ded <= dT:
                player.respawn(phys.vector(0,0))#find spawnpoint
            else:
                player.ded -= dT

    for planet in gs.ssys.planets:
        if planet.lastspawn <= dT:
            planet.spawnnow()
        else:
            planet.lastspawn -= dT



def prevcorner(obj):
    return obj.sprite.get_rect(center = (obj.phsobj.vPos-obj.phsobj.vMov).tup())

def nowcorner(obj):
    return obj.sprite.get_rect(center = obj.phsobj.vPos.tup())

def renderloop(gs, window):
    for bullet in gs.projset:
        prev = prevcorner(bullet)
        gs.mainrender.blit(gs.bg, prev, prev)
    for player in gs.playerlist:
        prev = prevcorner(player)
        gs.mainrender.blit(gs.bg, prev, prev)

    for bullet in gs.projset:#MUST ROTATE LTER
        bullet.sprite.blit(gs.mainrender, nowcorner(bullet))
    for player in gs.playerlist:
        player.sprite.blit(gs.mainrender, nowcorner(player))



    for player in gs.playerlist:
        helper = pygame.transform.rotate(player.pov, player.aDir)
        gs.mainrender.blit(helper, (0,0), helper.get_rect(center=player.phsobj.vPos.tup()))
        helper = pygame.transform.rotate(helper, -player.aDir)
        player.pov.blit(helper, (0,0), player.pov.get_rect(center=(helper.get_size()[0]/2, helper.get_size()[1]/2)))

        window.blit(gs.bg, (0,0))
        window.blit(player.pov, player.povpos)

        #DRAW HUD HERE
        
    pygame.display.flip()
    


def rulesloop(gs, delta):
    if gs.timeleft <= delta:
        return False
    else:
        gs.timeleft -= delta

    return True



def gameloop(gamestate, deltat, window):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    physloop(gamestate, deltat)
    spawnloop(gamestate, deltat)
    renderloop(gamestate, window)
    return rulesloop(gamestate, deltat)




#pygame init
pygame.init()
pywindow = pygame.display.set_mode((config.grw, config.grh))

players = [engine.shooter(engine.phys.vector(mp.radius, mp.radius))]
for wn in players:
    wn.sprite = sprite.load('char/randdude.png', pywindow)
settings = gamestate(mp, 2, 60, players, 5)

a=True
now = clock()
while a:
    b = clock()-now
    now += b
    a = gameloop(settings, b, pywindow)


