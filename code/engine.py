print "Loading Physics"
import phys
import time
import sprite

MAXHP = 100

def placeholder(asdf):
    print asdf

class bullet:
    def __init__(self, gSrc, vDir):
        self.gSrc = gSrc
        self.sprite = gSrc.bsprite
        self.owner = gSrc.owner
        self.phsobj = phys.physobj(0, self.owner.phsobj.vPos, vDir*gSrc.mV)
        self.phsobj.aDir = vDir.ang()
        sprite.init(self)
    def hit(self):
        self.gSrc.effect()
        self.gSrc.ammo += 1 ## REMOVE THIS LATER
        del self

def wot():
    print 'uw0tm8?'

class gun:
    def __init__(self, own, gundata=(20,0,500,wot,500, None, None)):
        self.owner = own
        self.ammo, self.dmg, self.mPeriod, self.effect, self.mV, self.sprite, self.bsprite= gundata
        self.lastfired = time.clock()
    def shoot(self, vDir):
        if self.ammo == 0 or (time.clock()*1000-self.lastfired)<self.mPeriod:
            return
        self.ammo -= 1
        vDir.rotate(self.owner.phsobj.aDir)
        vDir.y = vDir.y*-1
        self.lastfired = time.clock()*1000
        bull = bullet(self, vDir)
        return bull

class shooter:
    def __init__(self, sprit, vPos=phys.vector(0,0)):
        self.phsobj = phys.physobj(20, vPos)
        self.hp = MAXHP
        sprite.init(self, sprit)
        self.gun = None
        self.ded = 0 #gameloop analyses or respawns depending on this
    def hurt(self, dmg):
        if dmg < self.hp:
            self.hp -= dmg
            ## lil bloodsplatter
        else:
            return True
    def respawn(self,vPos):
        self.hp = MAXHP
        self.ded = 0
        self.phsobj.vPos = vPos
        self.phsobj.stop()

