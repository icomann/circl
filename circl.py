#!/bin/python2

print "Loading engine"
import engine
print "Loading maps"
import mapinfo
print "Loading languages"
import locale
print "Loading pygame"
import pygame

while True:
    mp = int(raw_input('Choose Map> '))
    if mp >= 0 and mp < len(mapinfo.ssyslist):
        mp = mapinfo.ssyslist[mp]
        break

print mp
