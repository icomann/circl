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

while True: ##map select
    mp = int(raw_input('Choose Map> '))
    if mp >= 0 and mp < len(mapinfo.ssyslist):
        mp = mapinfo.ssyslist[mp]
        break

print mp



class gamestate:
    def __init__(mp, mode, time, playerlist):
        self.ssys = mp
        self.mode = mode
        self.timeleft = timedata
        self.playerset = set(playerlist)
        self.playerc = len(self.playerlist)
        self.itemset= set()
        self.projset = set()



#pygame init
pygame.init()
window = pygame.display.set_mode((config.grw, config.grh), pygame.RESIZABLE)

#Here goes mainrender thingie, this needs to be moved to gameloop
mainrender = sprites.load('stars.png', window)
mainrender = pygame.transform.scale(background, (mp.radius, mp.radius))
#draw planets on background

displaysize = (config.grw, config.grh)
views = [0]
views[0] = pygame.Surface(displaysize).convert()
#make different sizes for later


def physloop(gs, dT):
    for player in gs.playerset:
        player.phsobj.tick(dT)#get forces later
        player.pshobj.movement(dT)
    for bullet in gs.projset:
        bullet.movement(dT)

    #HITSCAN KOMMT HIER

    for player in gs.playerset:
        player.move()
    for bullet in gs.projset()
        bullet.move()


def gameloop(gamestate, window):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()



