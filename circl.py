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
import sprites
from comp import folder
from time import clock

while True: ##map select
    mp = int(raw_input('Choose Map> '))
    if mp >= 0 and mp < len(mapinfo.ssyslist):
        mp = mapinfo.ssyslist[mp]
        break

print mp








class gamestate:
    def __init__(mp, mode, time, playerlist, resp):
        self.ssys = mp
        self.mode = mode
        self.timeleft = time
        self.respawntime = resp
        self.playerlist = set(playerlist)
        self.playerc = len(self.playerlist)
        self.itemset= set()
        self.projset = set()
        self.mainrender = pygame.Surface((self.ssys.radius*2, self.ssys.radius*2)).convert()
        self.bg = pygame.Surface((self.ssys.radius*2, self.ssys.radius*2)).convert()

        try:
            a = pygame.image.load('bulshit').convert()
            self.bg.blit(a)
            del a
        except:
            self.bg.fill(pygame.BLACK)

        for plan in self.ssys.planets:
            pygame.draw.circle(bg, plan.color, (self.vPos-vector(plan.radius, plan.radius)/2).tup(), plan.radius)

        self.mainrender.blit(self.bg)

        p = 0
        for player in self.playerlist:
            player.pov = pygame.Surface(config.grw/playerc, config.grh)
            player.povpos = (p*config.grw/playerc, config.grh)
            p += 1


def physloop(gs, dT):
    for player in gs.playerlist:
        player.phsobj.tick(dT)#get forces later
        player.pshobj.movement(dT,1)
    for bullet in gs.projset:
        bullet.movement(dT)

    #HITSCAN KOMMT HIER

    for player in gs.playerlist:
        player.move()
    for bullet in gs.projset()
        bullet.move()


def spawnloop(gs, dT):
    for player in gs.playerlist:
        if player.ded != 0:
            if player.ded <= dT:
                player.respawn(phys.vector(0,0))#find spawnpoint
            else:
                player.ded -= dT

    for planet in gs.ssys.planets:
        if planet.lastspawn <= dT:
            planet.spawn()
        else:
            planet.lastspawn -= dT



def prevcorner(obj):
    return obj.sprite.get_rect(center = (obj.pshobj.vPos-obj.phsobj.vMov).tup())

def nowcorner(obj)
    return obj.sprite.get_rect(center = obj.pshobj.vPos.tup())

def renderloop(gs, window):
    for bullet in gs.proyset:
        gs.mainrender.blit(bg, prevcorner(bullet))
    for player in gs.playerlist:
        gs.mainrender.blit(bg, prevcorner(player))

    for bullet in gs.proyset:#MUST ROTATE LTER
        bullet.sprite.blit(mainrender, nowcorner(bullet))
    for player in gs.playerlist:
        player.sprite.blit(mainrender, nowcorner(player))



    for player in gs.playerlist:
        helper = player.pov.pygame.transform(player.aDir)
        gs.mainrender.blit(helper, (0,0), helper.get_rect(center=player.phsobj.vPov.tup()))
        helper = helper.pygame.transform(-player.aDir)
        player.pov.blit(helper, (0,0), player.pov.get_rect(center=(helper.get_size()[0]/2, helper.get_size()[1]/2)))

        window.blit(player.pov, player.povpos)

        #DRAW HUD HERE
        
    


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
pywindow = pygame.display.set_mode((config.grw, config.grh), pygame.RESIZABLE)

players = [engine.shooter()]
settings = gamestate(mp, 2, 60, players, 5)

a=True
now = clock()
while a:
    b = clock()-now
    now += b
    a = gameloop(settings, b, pywindow)


