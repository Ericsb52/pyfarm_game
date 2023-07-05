import sys
from settings import *
from level import *

# lest off at https://www.youtube.com/watch?v=R9apl6B_ZgI 1:21:45 creating the overlay section

def main():
    game = Game()
    game.run()



class Game:
    def __init__(self):
        # initialize pygame
        pg.init()
        # window setup
        self.screen = pg.display.set_mode((SCREEN_W,SCREEN_H))
        pg.display.set_caption(TITLE)
        self.icon = pg.Surface((10,10))
        self.icon.fill("red")
        pg.display.set_icon(self.icon)

        # set up clock
        self.clock = pg.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.dt = self.clock.tick(FPS) / 1000
            self.level.run(self.dt)
            pg.display.update()

if __name__ == "__main__":
    main()