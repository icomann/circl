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
from comp import folder

while True:
    mp = int(raw_input('Choose Map> '))
    if mp >= 0 and mp < len(mapinfo.ssyslist):
        mp = mapinfo.ssyslist[mp]
        break

print mp

pygame.init()
window = pygame.display.set_mode((config.grw, config.grh), pygame.RESIZABLE)
mainrender = pygame.transform.scale(pygame.image.load(folder('sprites','stars.png')).convert(), (mp.radius, mp.radius))
window.blit(mainrender, (-2048,-2048))
pygame.display.flip()

raw_input()
print "bai bai"
