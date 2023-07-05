from settings import *

class Overlay:
    def __init__(self,player):
        self.display_surf = pg.display.get_surface()
        self.player = player


        self.tools_surf = {tool:pg.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
        self.seeds_surf = {seed:pg.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}

    def display(self):
        # tools
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_surf = pg.transform.scale(tool_surf,(TILE_SIZE,TILE_SIZE))
        tool_rect  =  tool_surf.get_rect(midtop = overlay_positions["tool"])
        self.display_surf.blit(tool_surf,tool_rect)

        # Seeds
        seed_surf = self.seeds_surf[self.player.selected_seed]
        seed_surf = pg.transform.scale(seed_surf, (TILE_SIZE, TILE_SIZE))
        seed_rect = tool_surf.get_rect(midtop = overlay_positions["seed"])
        self.display_surf.blit(seed_surf, seed_rect)

