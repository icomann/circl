killnot = {}
killtype = ['bullet', 'dakka', 'generic', 'gibs', 'laser', 'nuke', 'overkill', 'quick', 'short', 'space', 'spree', 'track']
for kfile in killtype:
    killnot[kfile] = set()
    kf = open("locale/kills/"+kfile)
    if kfile == 'spree':
        killnot[kfile] = list()
        store = set()
        for line in kf:
            line = line.strip()
            if line == '' or line == ' ':
                continue
            elif line[0] == '-':
                killnot[kfile].append(store)
                store = set()
                continue
            store.add(line)
    for line in kf:
        line = line.strip()
        if line == '' or line == ' ':
            continue
        killnot[kfile].add(line)

