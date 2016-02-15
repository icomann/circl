#!/bin/python2

import pygame
import engine
import phys
from phys import vector
from time import clock
pygame.init()
pygame.display.set_mode((640,480))
screen = pygame.display.get_surface()
pygame.mouse.set_visible(False)
pygame.joystick.Joystick(0).init()

mse = pygame.image.load('sprites/aim.png').convert()
msa = pygame.image.load('sprites/bull.png').convert()
mse.set_colorkey((0,0,0))
msa.set_colorkey((0,0,0))
msr = pygame.image.load('sprites/ret.png').convert()
msr.set_colorkey((0,0,0))
fonte = pygame.font.SysFont('asdf', 36)
y = 480 - fonte.size('wea')[1]
t0 = clock()

ret = vector()
wn = engine.shooter()
wn.phsobj.vPos = vector(320,240)
wn.phsobj.maxspeed = 4900
engine.gunlist.append(engine.gun(wn))
wn.gun = engine.gunlist[1]
stick = vector()

while True:
    screen.fill((100,50,50))
    delta = clock()-t0
    t0 = clock()
    for event in pygame.event.get():
        if event.type == 12:
            quit()
        elif event.type == 7:
            if event.axis == 0:
                stick.x = event.value
            elif event.axis == 1:
                stick.y = event.value
            elif event.axis == 2:
                ret.x = 320+event.value*320
            elif event.axis == 3:
                ret.y = 240+event.value*240
        elif event.type == 6 or event.type == 11:
            aim = (ret-wn.phsobj.vPos).dir()
            wn.gun.shoot(aim)
        else:
            print event
    npos = wn.phsobj.vPos
    wn.phsobj.process(delta, stick*500000)
    screen.blit(msr, (ret.x-8, ret.y-8))
    screen.blit(mse, (npos.x-8, npos.y-8))
    for pro in engine.projlist:
        pjs = pro.phsobj
        pjs.process(delta)
        screen.blit(msa, (pjs.vPos.x-8,pjs.vPos.y-8))
        if pjs.vPos.x > 640 or pjs.vPos.x < 0:
            pro.hit()
    line =' '.join(map(str,map(int,[npos.x,npos.y,ret.x,ret.y,1/delta])))
    screen.blit(fonte.render(line, 0, (255,255,255)), (0,y))
    pygame.display.update()

