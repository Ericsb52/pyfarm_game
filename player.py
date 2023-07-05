from settings import *
from timer import *

class Player(pg.sprite.Sprite):
    def __init__(self,pos,group,collision_group):
        super().__init__(group)

        self.import_assets()

        self.status = "down_idle"
        self.frame_index = 0

        # self.image = pg.Surface((32,64))
        # self.image.fill("green")
        self.image = self.animations[self.status][self.frame_index]

        self.rect = self.image.get_rect(center = pos)
        self.hit_box = self.rect.copy().inflate((-126,-70))
        self.collision_group = collision_group
        self.z = layers["main"]

        # movment
        self.dir = pg.math.Vector2()
        self.pos = pg.math.Vector2(self.rect.center)
        self.speed = player_speed

        self.timers = {
            "tool_use": Timer(350,self.use_tool),
            "tool_switch":Timer(200),
            "seed_use": Timer(350, self.use_tool),
            "seed_switch": Timer(200)

        }

        #tools
        self.tool_index = 0
        self.tools = ["hoe","axe","water"]
        self.selected_tool = self.tools[self.tool_index]

        #seeds
        self.seeds = ["corn","tomato"]
        self.seed_index = 0
        self.selected_seed = self.seeds[self.seed_index]

    def input(self):
        keys = pg.key.get_pressed()
        if not self.timers["tool_use"].active:
            # up and down movment
            if keys[pg.K_UP] or keys[pg.K_w]:
                self.dir.y = -1
                self.status = "up"
            elif keys[pg.K_DOWN] or keys[pg.K_s]:
                self.dir.y = 1
                self.status = "down"
            else:
                self.dir.y = 0

            # left and right movment
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.dir.x = 1
                self.status = "right"
            elif keys[pg.K_LEFT] or keys[pg.K_a]:
                self.dir.x = -1
                self.status = "left"
            else:
                self.dir.x = 0


            # tool use
            if keys[pg.K_SPACE]:
                self.timers["tool_use"].activate()
                self.dir = pg.math.Vector2()
                self.frame_index = 0

            # change tools
            if keys[pg.K_TAB] and not self.timers["tool_switch"].active:
                self.timers["tool_switch"].activate()
                self.tool_index+=1
                if self.tool_index >= len(self.tools):
                    self.tool_index = 0
                self.selected_tool = self.tools[self.tool_index]


            #seed use
            if keys[pg.K_LALT] and not self.timers["seed_use"].active:
                self.timers["seed_use"].activate()
                self.dir = pg.math.Vector2()
                self.frame_index = 0
                print("planted a "+self.selected_seed)

            #change seed
            if keys[pg.K_LSHIFT] and not self.timers["seed_switch"].active:
                self.timers["seed_switch"].activate()
                self.seed_index+=1
                if self.seed_index >= len(self.seeds):
                    self.seed_index = 0
                self.selected_seed = self.seeds[self.seed_index]
                print(self.selected_seed)


    def collision(self,dir):
        for sprite in self.collision_group.sprites():
            if hasattr(sprite,"hit_box"):
                if sprite.hit_box.colliderect(self.hit_box):
                    if dir == "horizontal":
                        if self.dir.x > 0:
                            self.hit_box.right = sprite.hit_box.left
                        if self.dir.x < 0:
                            self.hit_box.left = sprite.hit_box.right
                        self.rect.centerx = self.hit_box.centerx
                        self.pos.x = self.hit_box.centerx
                    if dir == "vertical":
                        if self.dir.y > 0:
                            self.hit_box.bottom = sprite.hit_box.top
                        if self.dir.y < 0:
                            self.hit_box.top = sprite.hit_box.bottom
                        self.rect.centery = self.hit_box.centery
                        self.pos.y = self.hit_box.centery
    def move(self,dt):
        if (self.dir.magnitude() > 0):
            self.dir = self.dir.normalize()

        self.pos.x += self.dir.x * self.speed * dt
        self.hit_box.centerx = round(self.pos.x)
        self.rect.centerx = self.hit_box.centerx
        self.collision("horizontal")

        self.pos.y += self.dir.y * self.speed * dt
        self.hit_box.centery = round(self.pos.y)
        self.rect.centery = self.hit_box.centery
        self.collision("vertical")

    def update(self,dt):
        self.input()
        self.get_ststus()
        self.move(dt)
        self.animate(dt)
        self.update_timers()

    def import_assets(self):

        self.animations = {"up":[],"down":[],"left":[],"right":[],
                           "up_idle":[],"down_idle":[],"right_idle":[],"left_idle":[],
                           "up_hoe":[],"down_hoe":[],"right_hoe":[],"left_hoe":[],
                           "up_axe":[],"down_axe":[],"right_axe":[],"left_axe":[],
                           "up_water":[],"down_water":[],"right_water":[],"left_water":[]}
        for anim in self.animations.keys():
            path = anim_path+anim
            self.animations[anim] = import_folder(path)
        print(self.animations)

    def animate(self,dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def get_ststus(self):
        # idle
        if (self.dir.magnitude() == 0):
            self.status = self.status.split("_")[0]+"_idle"
        # tools
        if self.timers["tool_use"].active:
            self.status = self.status.split("_")[0]+"_"+self.selected_tool

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def use_tool(self):
        pass
    def use_seed(self):
        pass



