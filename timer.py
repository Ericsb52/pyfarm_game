
from settings import *

class Timer:
    def __init__(self,dur,func = None):
        self.dur = dur
        self.func = func
        self.start_time = 0
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = pg.time.get_ticks()
    def deactivate(self):
        self.active = False
        self.start_time = 0
    def update(self):
        cur_time = pg.time.get_ticks()
        if cur_time - self.start_time >= self.dur:
            self.deactivate()
            if self.func:
                self.func()


