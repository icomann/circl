from comp import folder
killnot = {}
killtype = ['tele', 'bullet', 'dakka', 'generic', 'gibs', 'laser', 'nuke', 'overkill', 'quick', 'short', 'space', 'spree', 'track']
for kfile in killtype:
    killnot[kfile] = set()
    kf = open(folder('locale', 'kills', kfile))
    store = set()
    if kfile == 'spree':
        killnot[kfile] = list()
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
    kf.close()

menu = dict()
mfile = open(folder('locale', 'main'))
for line in mfile:
    line = line.strip().split(':')
    menu[line[0]] = line[1]
mfile.close()
