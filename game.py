import random

import pygame
import hero
import tool
from params import *
from maze import *

pygame.init()
mac = hero.Hero()
background_dict, height, width = import_maze("pattern.txt")
mac.pos, exit, corridor = get_positions(background_dict)

tools_positions = random.sample([pos for pos in corridor.keys()
                                   if pos not in [mac.pos, exit]], 3)
tools = ether, needle, tube = [tool.Tool(letter, pos) for letter, pos in 
                               zip(("e", "n", "t"), tools_positions)]
for tool in tools :
    background_dict[tool.pos] = tool.letter

                 
# Managing MacGyver movements
new_coord = mac.pos
display_layout(background_dict, width, height)

while mac.pos != exit:
     
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_DOWN:
                new_coord = mac.down() 
            elif event.key == pygame.K_UP:
                new_coord = mac.up() 
            elif event.key == pygame.K_LEFT:
                new_coord = mac.left() 
            elif event.key == pygame.K_RIGHT:
                new_coord = mac.right() 
                
    if new_coord in corridor:
        background_dict[mac.pos]= "_"
        background_dict[new_coord] = "*"    
        mac.pos = new_coord
        display_layout(background_dict, width, height)
    
    for tool in tools:
        if mac.pos == tool.pos:
            mac.bag.append(tool)
            tools.remove(tool)        

    
    if mac.pos == exit:
        if tools == []:
            print("Gagné !")
        else:
            print("Perdu...")    
           
pygame.quit()         