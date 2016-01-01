print "Loading Physics"
import phys
import time

projlist = set()

MAXHP = 100

def placeholder(asdf):
    print asdf

class bullet:
    def __init__(self, gSrc, dire):
        self.gSrc = gSrc
        self.owner = gSrc.owner
        self.phsobj = phys.physobj(0, self.owner.phsobj.vPos, dire*gSrc.mV)
        projlist.add(self)
    def hit(self):
        self.gSrc.effect()
        projlist.remove(self)
        self.gSrc.ammo += 1 ## REMOVE THIS LATER
        del self

def wot():
    print 'uw0tm8?'

class gun:
    def __init__(self, own, gundata=(20,0,500,wot,500)):
        self.owner = own
        self.ammo = gundata[0]
        self.lastfired = time.clock()
        self.dmg = gundata[1]
        self.mV = gundata[4]
        self.sPeriod = gundata[2]
        self.effect = gundata[3]
    def shoot(self, angle):
        if self.ammo == 0 or (time.clock()*1000-self.lastfired)<self.mPeriod:
            return
        self.ammo -= 1
        self.lastfired = time.clock()*1000
        bullet(self, angle)

class shooter:
    def __init__(self):
        self.phsobj = phys.physobj()
        self.vDir = phys.vector(1,0)
        self.hp = MAXHP
        self.gun = None
        self.active = False #gameloop analyses or respawns depending on this
    def hurt(self, dmg):
        if dmg < self.hp:
            self.hp -= dmg
            ## lil bloodsplatter
        else:
            self.active = False
    def respawn(self,vPos,t):
        self.hp = MAXHP
        self.active = True
        self.vPos = vPos

