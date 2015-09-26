import pygame as pg
import os
from Tkinter import *
import random
import threading
import darray
import numpy as np
import time
from pygame.locals import *

pg.font.init()

class Screen(Frame):
    def __init__(self, parent, w, h):
        Frame.__init__(self, parent, width = w, height = h)
        self.w = w
        self.h = h
        self.ui()
        self.settings()
        self.pack()
        self.pginit()
    def ui(self):
        pass
    def settings(self):
        os.environ['SDL_WINDOWID'] = str(self.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        self.curdisp = np.zeros((self.w, self.h))
        self.todisp = np.zeros((self.w, self.h))
    def pginit(self):
        pg.display.init()
        self.board = pg.display.set_mode((self.w,self.h))
    def _mainloop(self, lfps = 0):
        st = time.time()
        pg.display.flip()
        self.master.update()
        #self.master.update()
        parts = darray.replacearr(self.curdisp, self.todisp, xparts = self.w/300, yparts = self.h/300)
        for part, (x1, x2, y1, y2) in parts:
            self.curdisp[x1:x2, y1:y2] = part
            tsrect = pg.Rect(x1, y1, x2-x1, y2-y1)
            tempsurf = self.board.subsurface(tsrect)
            pg.surfarray.blit_array(tempsurf, part)
        #print fps

        ft = 1./(time.time()-st)
        print ft
        _font = pg.font.Font(None, 36)
        if lfps == 0 or random.random() > 0.9: #update
            text = _font.render("FPS:" + str(min(int(ft),99)), 1, (255, 255,255))
        else: #noupdate
            text = _font.render("FPS:" + str(min(int(lfps),99)), 1, (255, 255,255))
        textpos = text.get_rect()
        #textpos.centerx = self.board.get_rect().centerx
        self.board.fill((0,0,0),textpos)
        self.board.blit(text, textpos)
        if lfps == 0 or random.random() > 0.9:
            self.after(0, self._mainloop, ft)
        else:
            self.after(0, self._mainloop, lfps)
            
    def naiveloop(self, lfps = 0):
        st = time.time()
        pg.display.flip()
        self.master.update()
        pg.surfarray.blit_array(self.board,self.todisp)
        ft = 1./(time.time()-st)
        
        print ft
        #copy pasted
        _font = pg.font.Font(None, 36)
        if lfps == 0 or random.random() > 0.9: #update
            text = _font.render("FPS:" + str(min(int(ft),99)), 1, (255, 255,255))
        else: #noupdate
            text = _font.render("FPS:" + str(min(int(lfps),99)), 1, (255, 255,255))
        textpos = text.get_rect()
        self.board.fill((0,0,0),textpos)
        self.board.blit(text, textpos)
        if lfps == 0 or random.random() > 0.9:
            self.after(0, self.naiveloop, ft)
        else:
            self.after(0, self.naiveloop, lfps)
