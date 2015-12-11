import math

def rCAng(ang):
    return math.pi*ang/180
    
def aCRad(rad):
    return rad*180/math.pi
    
def mDist(pos1, pos2):
    return ((pos1.x-pos2.x])**2+(pos1.y+pos2.y)**2)**0.5
    
class vector:
    x=0
    y=0
    def __init__(self, x, y, r=1):
        self.x,self.y = r*x, r*y
        return self
    def suma(self,ex,y='vector'):
        if y == 'vector:
            self.x += ex.x
            self.y += ex.y
            return
        self.x+=ex
        self.y+=y
    def mult(self,r):
        self.x*=r
        self.y*=r
    def diag(self):
        mag = mDist(self,vector(0,0))
        self.x /= mag
        self.y /= mag

class polarC:
    r=0
    rad=0
    inrad=1
    def __init__(self, r, ang, inrad=True):
        self.r = r
        self.inrad = inrad
        if !rad:
            ang = rCAng(ang)
        self.ang = ang
        return self
        
class physicsobj:
    def __init__(self, mass):
        self.mass = mass
        self.a = vector(0,0)
        self.v = vector(0,0)
    def tick(self,deltat,vNetforce=vector(0,0)):
        self.a.suma(vNetforce.mult(1.0/mass))
        self.v.suma(a.mult(deltat))
    def movement(self,deltat):
        mov = vector()

def rAng(pos1, pos2):
    return atan(float(pos1.y)-pos2.y/pos1.x-pos2.x)
    
def aAnd(pos1, pos2):
    return aCRad(rAng(pos1,pos2))

def vCPolar(r,rad):
    return vector(cos(rad), sen(rad), r)
    
def pCVect(vect):
    return polarC(atan(float(vect.y)/vect.x))
