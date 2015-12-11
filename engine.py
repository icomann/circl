print "Loading Physics"
import phys

MAXHP = 100

class gun:
    ammo = 1
    dmg = 1
    msPeriod = 1000
    def __init__(self, gundata=0):
        return self

fist = gun()
fist.ammo = 5
fist.msPeriod=0.300

class shooter:
    def __init__(self):
        self.phsobj = phys.physicsobj()
        self.theta = 0
        self.invis = True
        self.pos = phys.vector(0,0)
        self.hp = MAXHP
        self.active = False
        return self
    def respawn(self,pos,t):
        self.hp = MAXHP
        self.active = True
        self.pos = pos
        self.theta = t
        self.invul = False
