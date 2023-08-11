############################ IMPORTS ##################################

from pygame import *
from maze_generator import *
from time import sleep

############################ FUNCTIONS ################################

#print(maze)
output()

############################ START ####################################

x = display.set_mode((650, 410))
run = True
background_color = (255, 255, 255)

############################ MAIN-FUNCTION ############################

init()

x.fill(background_color)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    display.update()
    sleep(1)

quit()