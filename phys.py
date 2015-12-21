import math

def rCAng(ang):
    return math.pi*ang/180
    
def aCRad(rad):
    return rad*180/math.pi
    
def mDist(pos1, pos2):
    return ((pos1.x-pos2.x)**2+(pos1.y+pos2.y)**2)**0.5
    
class vector:
    def __init__(self, x=0, y=0, r=1):
        self.x,self.y = r*x, r*y

    def __add__(self,vect):
        if not isinstance(vect, vector):
            return self
        return vector(self.x+vect.x, self.y+vect.y)

    def __mul__(self,r):
        if not isinstance(r, vector):
            return vector(self.x*r, self.y*r)
	return self.x*r.x+self.y+r.y
        
    def mag(self):
        return mDist(self,vector(0,0))

    def dir(self):
        ma = self.mag()
	if not ma:
		return vector()
        return self*(1.0/ma)

class polarC:
    def __init__(self, r=0, ang=0, inrad=True):
        self.r = r
        self.inrad = inrad
        if not inrad:
            ang = rCAng(ang)
        self.ang = ang
        
class physobj:
    def __init__(self, vel=vector(0,0), acc=vector(0,0)):
        self.a = acc
        self.v = vel
    def tick(self,deltat,vNetforce=vector(0,0)):
        self.a = vNetforce
        self.v += self.a*deltat
    def movement(self,deltat):
        return self.v*deltat+self.a*(deltat*deltat/2)
    def process(self, dt, vF=0):
        self.tick(dt, vF)
        return self.movement(dt)

def rAng(pos1, pos2):
    return atan(float(pos1.y)-pos2.y/pos1.x-pos2.x)
    
def aAnd(pos1, pos2):
    return aCRad(rAng(pos1,pos2))

def vCPolar(r,rad):
    return vector(cos(rad), sen(rad), r)
    
def pCVect(vect):
    return polarC(atan(float(vect.y)/vect.x))
