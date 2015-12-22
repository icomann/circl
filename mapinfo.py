from phys import vector
class planet:
    def __init__(self, dataarray):
        S, x, y, r, f, fr, i, c = dataarray
        self.pos = vector(x,y)
        self.spawn = (S=='*')
        self.radius = r
        self.fradius = fr
        self.force = f
        self.items = i
        self.color = tuple(c.split('-')

class ssyst:
    def __init__(self, file):
        self.radius = 4096
        self.title = 'unnamed'
        self.author 'unknown'
        self.pl = (1,99)
        file = open(file)
        for line in file:
            line = line.strip()
        ## planet: [((x,y), radius, force, (randomdropinfo), color/text), ...] hopeigettoletyouknow
        ##randdrinf: (((nuthin, 40), (ubergun,10), (candy,50)), period)        beforetheylockmesillyarseaway
        self.planets = [((90,1024), 512, 20, (0,1), 0), ((180, 2048), 512, 40, (0,2), 0)]
