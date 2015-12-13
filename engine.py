print "Loading Physics"
import phys

MAXHP = 100

class gun:
    ammo = 1
    dmg = 1
    msPeriod = 1000
    def __init__(self, gundata=0):
        self.guns = gundata

fist = gun()
fist.ammo = 5
fist.msPeriod=0.300

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
