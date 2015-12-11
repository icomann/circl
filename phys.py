import math

def rCAng(ang):
    return math.pi*ang/180
    
def aCRad(rad):
    return rad*180/math.pi

class vector:
    x=0
    y=0
    def __init__(self, x, y, r=1):
        self.x,self.y = r*x, r*y
        return self

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

def mDist(pos1, pos2):
    return ((pos1.x-pos2.x])**2+(pos1.y+pos2.y)**2)**0.5


def rAng(pos1, pos2):
    return atan(float(pos1.y)-pos2.y/pos1.x-pos2.x)
    
def aAnd(pos1, pos2):
    return aCRad(rAng(pos1,pos2))

def vCPolar(r,rad):
    return vector(cos(rad), sen(rad), r)
    
def pCVect(vect):
    return polarC(atan(float(vect.y)/vect.x))
