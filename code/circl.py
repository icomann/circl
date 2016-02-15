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

for a in mapinfo.ssyslist:
    print a.title

while True: ##map select
    mp = int(raw_input('Choose Map> '))
    if mp >= 0 and mp < len(mapinfo.ssyslist):
        mp = mapinfo.ssyslist[mp]
        break

print mp


bsprites = dict()






class gamestate:
    def __init__(self, mp, mode, time, playerlist, resp):
        self.ssys = mp
        self.mode = mode
        self.timeleft = time
        self.respawntime = resp
        self.playerlist = playerlist
        self.playerc = len(self.playerlist)
        self.itemset= set()
        self.missset = set()
        self.projset = set()
        self.mainrender = pygame.Surface((self.ssys.radius*2, self.ssys.radius*2)).convert()
        self.bg = pygame.Surface(self.mainrender.get_size()).convert()

        try:
            a = pygame.image.load(folder('sprites', 'maps', ssys.bgs), 'bg')
        except:
            a = pygame.image.load(folder('sprites', 'maps', "default.png"),'bg')

        a.convert()
        self.bg.fill((20,20,60))
        self.bg.blit(a, (0,0))
        del a

        for plan in self.ssys.planets:
            pygame.draw.circle(self.bg, (min(255, plan.force/8),50,50+max(0, 120-plan.force/4)), plan.vPos.tup(), plan.fradius, 5+plan.force/70)
        for plan in self.ssys.planets:
            pygame.draw.circle(self.bg, plan.color, plan.vPos.tup(), plan.radius)

        self.mainrender.blit(self.bg, (0,0))

        p = 0
        for player in self.playerlist:
            player.pov = pygame.Surface((config.grw/self.playerc, config.grh))
            player.povpos = (p*config.grw/self.playerc, 0)
            p += 1


def controlloop(gs):
    playercenter = engine.phys.vector(config.grw/6, config.grh/2)
    for event in pygame.event.get():
        #print event
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == 32:
                gs.playerlist[0].phsobj.stop()
        elif event.type == 'changeaxis':
            print 'wot'
        elif event.type == 5:#SHOOT CODE

            pos = event.pos
            rDir = engine.phys.vector(pos[0], pos[1]) - engine.phys.vector(config.grw/6, config.grh/2)
            rDir.y = rDir.y*-1
            #the second vector should be the shooter's screen position once we've got controls working

            if rDir.mag() != 0:
                rDir = rDir.dir()
            else:
                rDir = engine.phys.vector()
            new = gs.playerlist[0].gun.shoot(rDir)
            if new != None:
                gs.projset.add(new)
    return True


def gravforce(player, planets):
    for planet in planets:
        d = planet.vPos-player.vPos
        dm = d.mag()
        if dm < planet.fradius and dm > planet.radius:
            player.vNForce += d.dir()*planet.force

def physloop(gs, dT):
    for player in gs.playerlist:
        player = player.phsobj
        gravforce(player, gs.ssys.planets)
        player.tick(dT)
        player.movementT(dT)

    for missile in gs.missset:
        missile = missile.phsobj
        gravforce(missile, gs.ssys.planets)
        missile.tick(dT)
        missile.movementT(dT)

    for bullet in gs.projset:
        bullet = bullet.phsobj
        bullet.movementF(dT)

#    for player in gs.playerlist:
#        hits = hitscan(gs, player)
#    for player in gs.missset:
#        hits = hitscan(gs, player)
#    for bullet in gs.projset:
#        hits = hitscan(gs, bullet)

    for player in gs.playerlist:
        player.phsobj.move()
    for missile in gs.missset:
        missile.phsobj.move()
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





def renderloop(gs, window):
    for bullet in gs.projset:
        sprite.cleanthing(gs, bullet)
    for player in gs.playerlist:
        sprite.cleanthing(gs, player)
    for missile in gs.missset:
        sprite.cleanthing(gs, missile)

    for bullet in gs.projset:
        sprite.renderthing(gs, bullet)
    for player in gs.playerlist:
        sprite.rotatething(player)
        sprite.renderthing(gs, player)
    for missile in gs.missset:
        sprite.rotatething(missile)
        sprite.renderthing(gs, missile)



    for player in gs.playerlist:
        helper = pygame.transform.rotate(player.pov, player.phsobj.aDir)
        helper.blit(gs.mainrender, (0,0), helper.get_rect(center=player.phsobj.vPos.tup()))
        helper = pygame.transform.rotate(helper, -player.phsobj.aDir)
        player.pov.blit(helper, (0,0), player.pov.get_rect(center=(helper.get_size()[0]/2, helper.get_size()[1]/2)))

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
    ph = gamestate.playerlist[0].phsobj
    
    if not controlloop(gamestate):
        return False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ph.vPos -= engine.phys.vector(0,1)*500*deltat
    elif keys[pygame.K_DOWN]:
        ph.vPos += engine.phys.vector(0,1)*500*deltat
    if keys[pygame.K_RIGHT]:
        ph.vPos += engine.phys.vector(1,0)*500*deltat
    elif keys[pygame.K_LEFT]:
        ph.vPos -= engine.phys.vector(1,0)*500*deltat
    if keys[pygame.K_e]:
        ph.aDir -= 90*deltat
    if keys[pygame.K_q]:
        ph.aDir += 90*deltat
  

    physloop(gamestate, deltat)
    spawnloop(gamestate, deltat)
    renderloop(gamestate, window)
    return rulesloop(gamestate, deltat)




#pygame init and stuff goes here
pygame.init()
pywindow = pygame.display.set_mode((config.grw, config.grh))

sprite.renderer = pywindow
bsprites['pew'] = sprite.load('bull.png')
engine.defb = bsprites['pew']

players = []
for a in range(0,3):
    players.append(engine.shooter('char/shirtdude.png', engine.phys.vector(mp.radius+128*a, mp.radius)))
for wn in players:
    wn.gun = engine.gun(wn)
    wn.gun.bsprite = bsprites['pew']
players[1].phsobj.aDir = 30
players[1].sprite = sprite.load('char/randdude.png')

settings = gamestate(mp, 2, 60, players, 5)

a=True
now = clock()
while a:
    b = clock()-now
    now += b
    a = gameloop(settings, b, pywindow)
