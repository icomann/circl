from os import sep
foldsep = sep
homeadress = __file__.split(foldsep)
homeadress.pop(len(homeadress)-1)
homeadress = foldsep.join(homeadress)
def folder(*arg):
    line = homeadress
    for argv in arg:
        line += foldsep + argv
    return line