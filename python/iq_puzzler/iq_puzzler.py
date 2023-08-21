############################ IMPORT'S ###############################

from pygame import *

############################ Declare Variables ######################

w, h = 11, 5
multi = 70
abstand = 5

array = [[11, 44, 44, 44, 44, 55, 55, 10, 10, 10, 00],   # 1=pink, 2=dark blue, 3=light_blue
         [11, 11, 13, 44, 55, 55, 00, 00, 10, 00, 00],   # 4=yellow, 5=orange, 6=light red, 7=red
         [22, 11, 13, 13, 77, 55, 00, 00, 00, 00, 00],   # 8=light lila, 9=dark lila
         [22, 11, 13, 33, 77, 77, 14, 14, 00, 00, 00],   # 10=light green, 13=dark green
         [22, 22, 22, 33, 33, 77, 14, 14, 14, 00, 00]]   # 14=turquise
color_array = ["PINK", "DARK_BLUE", "LIGHT_BLUE", "YELLOW", "ORANGE", "LIGHT_RED", "RED", "LIGHT_LILA", "DARK_LILA", "LIGHT_GREEN", "DARK_GREEN", "TURQUISE"]
############################ START ##################################

# pygame
fenster = display.set_mode((w*multi, h*multi))
display.set_caption("IQ-Puzzle solver")
run = True
clock = time.Clock()
# Farben
WHITE = (255, 255, 255)
GRAY = (177, 177, 177)
PINK = (255, 79, 117)
DARK_BLUE = (50, 107, 120)
LIGHT_BLUE = (137, 208, 224)
YELLOW = (255, 183, 0)
ORANGE = (255, 111, 0)
LIGHT_RED", "RED", "LIGHT_LILA", "DARK_LILA", "LIGHT_GREEN", "DARK_GREEN", "TURQUISE"
# Funktionen
def zeichnen(width, height, color):
    draw.rect(fenster, color, (height*multi+abstand, width*multi+abstand, multi-abstand, multi-abstand))

def output():
    for i in range(h):
        for j in range(w):
                zeichnen(i, j, color_array[array[i][j]])

############################ Main ###################################

fenster.fill(WHITE)
output()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.flip()
    clock.tick(10)

quit()