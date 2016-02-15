import pygame
from comp import folder

size = dict()
size['char'] = 96,128
size['bg'] = ,128
size['char'] = 96,128
size['char'] = 96,128

def load(filename, typee='no'):
    try:
        texture = pygame.image.load(folder('sprites', filename)).convert(renderer)
	texture.set_colorkey((255,0,255))
        texture.convert()
        if typee != 'no':
            texture = pygame.transform.scale(texture, size[typee])
    except:
        return None
    return texture 

def nowcorner(obj):
    return obj.rosprite.get_rect(center = obj.phsobj.vPos.tup())

def lastnew(thing):
    thing.last = nowcorner(thing)

def rotth(thing):
    thing.rosprite = pygame.transform.rotate(thing.sprite, thing.phsobj.aDir)
    thing.phsobj.lDir = thing.phsobj.aDir

def init(thing, texture=None):
    if texture != None:
        texture = load(texture)
        thing.sprite = texture
    rotth(thing)
    lastnew(thing)

def rotatething(thing):
    if thing.phsobj.aDir == thing.phsobj.lDir:
        return
    rotth(thing)
    lastnew(thing)

def renderthing(gs, thing):
    gs.mainrender.blit(thing.rosprite, thing.last)

def cleanthing(gs, thing):
    gs.mainrender.blit(gs.bg, thing.last, thing.last)
    lastnew(thing)
