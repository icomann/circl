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

    def tup(self):
        return self.x, self.y

    def __radd__(self, vect):
        return self
    
    def __sub__(self, vect):
        return self + -1*vect

    def __mul__(self,r):
        if not isinstance(r, vector):
            return vector(self.x*r, self.y*r)
	return self.x*r.x+self.y+r.y
        
    def __rmul__(self,r):
        return self*r

    def __div__(self,r):
        return vector(self.x/r, self.y/r)

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

    def mag(self):
        return (self.x**2 + self.y**2)**0.5

    def dir(self):
        ma = self.mag()
	if not ma:
		return None
        return self/ma

class polarC:
    def __init__(self, r=0, ang=0, inrad=True):
        self.r = r
        self.inrad = inrad
        if not inrad:
            ang = rCAng(ang)
        self.ang = ang
        
class physobj:
    def __init__(self, mass=10, vPos =vector(0,0), vel=vector(0,0)):
        self.a = vector(0,0)
        self.v = vel
        self.vPos = vPos
        self.vMov = vector(0,0)
        self.vNForce = vector(0,0)
        self.m = float(mass)

    def tick(self,deltat):#do not use on massless object
        self.a = self.vNForce/self.m
        self.v += self.a*deltat
        self.vNForce = vector(0,0)

    def stop(self):
        self.v = 0

    def movement(self,deltat, mass=0):
        self.vMov = self.v*deltat-mass*self.a*((deltat*deltat)/2)

    def move(self):
	self.vPos += self.vMov

def rAng(pos1, pos2):
    return atan(float(pos1.y)-pos2.y/pos1.x-pos2.x)
    
def aAnd(pos1, pos2):
    return aCRad(rAng(pos1,pos2))

def vCPolar(r,rad):
    return vector(cos(rad), sen(rad), r)
    
def pCVect(vect):
    return polarC(atan(float(vect.y)/vect.x))

def rectCof(vP1, vP2, vD1, vD2):
    dP = vP2-vP1
    det = vD1.x*vD2.y-vD2.x*vD1.y
    l1 = dP.x*vD2.y-vD2.x*dP.y
    l2 = vD1.x*dP.y-dP.x*vD1.y
    l1 /= float(det)
    l2 /= float(-det)
    return l1, l2

def objCol():
    return 'k3k'
