from phys import vector
from comp import folder
from os import listdir

class planet:
    def __init__(self, dataarray, size):
        S, x, y, r, f, fr, i, t, c = dataarray
        self.spawn = (S=='*')
        self.radius = int(r)
        self.fradius = int(fr)
        self.force = int(f)
        self.vPos = vector(int(x),-int(y))+vector(size, size)
        self.items = i
        self.period = int(t)
        self.lastspawn = self.period
        self.color = tuple(map(int, c.split(',')))
    def spawnnow(self):
        self.lastspawn = self.period
        print "Planet " + str(self.vPos) + ' should have spawned a thing.'

class ssyst:
    def __init__(self, file):
        self.radius = 4096
        self.title = 'unnamed'
        self.author = 'unknown'
        self.pl = (1,99)
        self.planets = list()
        file = open(file)
        for line in file:
            line = line.strip()
            if line[0] == ':':
                if line[1] == 'r':
                    self.radius = int(line[2:])
                elif line[1] == 'p':
                    self.pl = tuple(map(int,line[2:].split(',')))
                elif line[1] == 'a':
                    self.author = line[2:]
                elif line[1] == 't':
                    self.title = line[2:]
                continue
        ## planet: [((x,y), radius, force, (randomdropinfo), color/text), ...] hopeigettoletyouknow
        ##randdrinf: (((nuthin, 40), (ubergun,10), (candy,50)), period)        beforetheylockmesillyarseaway
            line = line.split(';')
            self.planets.append(planet(line, self.radius))
    def __str__(self):
        line = 'Sistema ' + self.title + '.\n'
        line += 'Made by ' + self.author + ' for ' + str(self.pl[0])
        line += ' to ' + str(self.pl[1]) + ' players.\n'
        line += '\nContains ' + str(len(self.planets)) + ' planets in a '
        line += str(self.radius) + ' radius:\n\n'
        line += 'POS\t\tSize\tSpawner\tGrav\n'
        for plan in self.planets:
            line += str(plan.vPos).ljust(16) + '\t'.join(map(str, [plan.radius, plan.spawn, plan.force])) + '\n'
        return line

ssyslist = list()
maplist = listdir(folder('maps'))
for lvl in maplist:
    ssyslist.append(ssyst(folder('maps', lvl)))
