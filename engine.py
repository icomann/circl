print "Loading Physics"
import phys
import time


MAXHP = 100

def placeholder(asdf):
    print asdf

class bullet:
    def __init__(self, gSrc, pos, vel):
        self.gSrc = gSrc
        self.physobj = (0, vel)
        self.vPos = pos

def wot():
    a = 1

class gun:
    def __init__(self, gundata=(0,0,5000,wot)):
        self.ammo = gundata[0]
        self.lastfired = 0
	self.dmg = gundata[1]
	self.msPeriod = gundata[2]
        self.effect = gundata[3]
    def shoot(self):
        if self.ammo == 0 or (time.clock()*1000-self.lastfired)>self.msPeriod:
            return None
        self.ammo -= 1
        self.lastfired = time.clock()
        return bullet(self, phys.vector(0,0), phys.vector(0,0))

fist = gun((5, 1, 300, placeholder))
k = fist.shoot()
k.gSrc.effect(k) ## should give list of people hit

class shooter:
    def __init__(self):
        self.phsobj = phys.physicsobj()
        self.theta = 0
        self.invis = True
        self.vPos = phys.vector(0,0)
        self.hp = MAXHP
        self.active = False
    def respawn(self,vPos,t):
        self.hp = MAXHP
        self.active = True
        self.vPos = vPos
        self.theta = t
        self.invul = False
    def move(self, vMovement):
        self.pos.suma(vMovement)
