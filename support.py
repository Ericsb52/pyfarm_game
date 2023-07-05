from os import walk
import pygame

def import_folder(path):
    surf_list = []

    for folder_name, sub_folder,img_file in walk(path):
        for img in img_file:
            new_path = path+"/"+img
            img_surf = pygame.image.load(new_path).convert_alpha()
            surf_list.append(img_surf)


    return surf_list