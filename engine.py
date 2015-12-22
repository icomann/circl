print "Loading Physics"
import phys
import time

projlist = []

MAXHP = 100

def placeholder(asdf):
    print asdf

class bullet:
    def __init__(self, gSrc, vel):
        self.gSrc = gSrc
        self.physobj = (0, vel)
        self.owner = gSrc.owner
        self.vPos = gSrc.owner.vPos
        projlist.append(self)

def wot():
    a = 1

class gun:
    def __init__(self, own, gundata=(0,0,5000,wot,50)):
        self.owner = own
        self.ammo = gundata[0]
        self.lastfired = 0
        self.dmg = gundata[1]
        self.mV = gundata[4]
        self.msPeriod = gundata[2]
        self.effect = gundata[3]
    def shoot(self, angle):
        if self.ammo == 0 or (time.clock()*1000-self.lastfired)>self.msPeriod:
            return False
        self.ammo -= 1
        self.lastfired = time.clock()
        bullet(self, angle*self.mV)
	return True

class shooter:
    def __init__(self):
        self.phsobj = phys.physicsobj()
        self.vDir = vector(1,0)
        self.invis = True
        self.vPos = phys.vector(0,0)
        self.hp = MAXHP
        self.active = False
    def hurt(self, dmg):
        if dmg < self.hp:
            self.hp -= dmg
            ## lil bloodsplatter
        else:
            self.active = False
            return True
    def respawn(self,vPos,t):
        self.hp = MAXHP
        self.active = True
        self.vPos = vPos
        self.invul = False
    def proc(self):
        self.pos += self.phsobj.process()


