import disp as display
import numpy as np
from Tkinter import *
import cProfile
import pstats
import time
import random
import colorsys
import plmt

st = time.time()
root = Tk()
display = display.Screen(root, 1920, 1080)
root.update()

def drawsquare(xp,yp, col, size = 50):
    m = np.zeros((size, size))
    m.fill(col)
    display.todisp[xp-size/2:xp+size/2,yp-size/2:yp+size/2] = m

def runloop():
    print 'started!'
    col = 0
    yp = 1080/2
    xp = 1920/2
    size = 50
    s = size/2
    while 1:
        col += .0001
        if col > 1:
            col = 0
        color = colorsys.hsv_to_rgb(col, 1, 0.5)
        color = sum((int(val*256)*256**i for i, val in enumerate(color)))
        yp += random.randint(-1,1)
        xp += random.randint(-1,1)
        if xp < s:
            xp = 1920-s
        if xp > 1920-s:
            xp = s
        if yp < s:
            yp = 1080 - s
        if yp > 1080-s:
            yp = s
        drawsquare(xp, yp, color, size = size)

for x in xrange(3):
    plmt.mt(runloop)

if False:
    root.after(0,display.naiveloop) #this is slow
else:
    root.after(0,display._mainloop) #this is fast

root.mainloop()

display.go = False

print time.time()-st, 'total'
