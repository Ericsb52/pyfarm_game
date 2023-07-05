from settings import *
from player import *
from overlay import *
from sprites import*


class Level:
    def __init__(self):
        self.display_surf = pg.display.get_surface()
        self.all_sprites = CameraGroup()
        self.collision_sprites = pg.sprite.Group()
        self.setup()

    def setup(self):
        tmx_data = load_pygame("assets/data/map.tmx")
        # lowest parts of house
        for layer in ["HouseFloor","HouseFurnitureBottom"]:
            for x,y,surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x*TILE_SIZE,y*TILE_SIZE),surf,self.all_sprites,layers["house bottom"])
        # top parts of house and fence
        for layer in ["HouseWalls","HouseFurnitureTop"]:
            for x,y,surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x*TILE_SIZE,y*TILE_SIZE),surf,self.all_sprites,layers["main"])
        for layer in ["Fence"]:
            for x,y,surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x*TILE_SIZE,y*TILE_SIZE),surf,[self.all_sprites,self.collision_sprites],layers["main"])
        # water
        water_frames = import_folder("assets/graphics/water")
        for x,y,surf in tmx_data.get_layer_by_name("Water").tiles():
            Water((x*TILE_SIZE,y*TILE_SIZE),water_frames,self.all_sprites)
        # flowers
        for obj in tmx_data.get_layer_by_name("Decoration"):
            WildFlower((obj.x,obj.y),obj.image,[self.all_sprites,self.collision_sprites])
        # trees
        for obj in tmx_data.get_layer_by_name("Trees"):
            Tree((obj.x, obj.y), obj.image, [self.all_sprites,self.collision_sprites],obj.name)
        # collision layer
        for x, y, surf in tmx_data.get_layer_by_name("Collision").tiles():
            Generic((x*TILE_SIZE,y*TILE_SIZE),pg.Surface((TILE_SIZE,TILE_SIZE)),self.collision_sprites)


        for obj in tmx_data.get_layer_by_name("Player"):
            if obj.name == "Start":
                self.player = Player((obj.x,obj.y),self.all_sprites,self.collision_sprites)
        Generic(pos=(0, 0),
                surf=pg.image.load(floor_path).convert_alpha(),
                groups=self.all_sprites,
                layer=layers["ground"])
        self.hud = Overlay(self.player)

    def run(self,dt):
        self.display_surf.fill("black")
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
        self.hud.display()


class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pg.display.get_surface()
        self.offset = pg.math.Vector2()

    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - SCREEN_W / 2
        self.offset.y = player.rect.centery - SCREEN_H / 2

        for layer in layers.values():
            for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surf.blit(sprite.image,offset_rect)


