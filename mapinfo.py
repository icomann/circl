from phys import vector

class planet:
    def __init__(self, dataarray):
        S, x, y, r, f, fr, i, t, c = dataarray
        self.pos = vector(x,y)
        self.spawn = (S=='*')
        self.radius = r
        self.fradius = fr
        self.force = f
        self.items = i
        self.period = t
        self.color = tuple(c.split('-')

class ssyst:
    def __init__(self, file):
        self.radius = 4096
        self.title = 'unnamed'
        self.author 'unknown'
        self.pl = (1,99)
        self.planets = list()
        file = open(file)
        for line in file:
            line = line.strip()
            if line[0] == '-':
                if line[1] == 'r':
                    self.radius = int(line[2:])
                elif line[1] == 'p':
                    self.pl = tuple(line[2:].split(','))
                elif line[1] == 'a':
                    self.author = line[2:0]
                elif line[1] == 't':
                    self.title = line[2:0]
            continue
        ## planet: [((x,y), radius, force, (randomdropinfo), color/text), ...] hopeigettoletyouknow
        ##randdrinf: (((nuthin, 40), (ubergun,10), (candy,50)), period)        beforetheylockmesillyarseaway
            line = line.split(';')
            self.planets.append(line)
