import pygame
from pygame import gfxdraw


wn_height = 500
wn_width = 500

Black = (0,0,0)
Blue = (0,0,255)
cyan = (0,255,255)
Green= (0,255,0)
purple = (255,0,255)
Red= (255,0,0)
white = (255,255,255)
  
pygame.init()
screen = pygame.display.set_mode((wn_width, wn_height))
screen.fill((0,0,0))
pygame.display.set_caption("Cohen Sutherland Line Clipping ALgorithm")
    
# windows coordinates
x_wmax = 380.0
y_wmax = 300.0
x_wmin = 140.0
y_wmin = 140.0

# making window
gfxdraw.polygon(screen, [(x_wmin,y_wmin),(x_wmax, y_wmin),(x_wmax,y_wmax),(x_wmin,y_wmax)], white)

INSIDE = 0 
LEFT = 1 
RIGHT = 2 
BOTTOM = 4 
TOP = 8	 

def computeCode(x, y):
	code = INSIDE
	if x < x_wmin:	 
		code |= LEFT
	elif x > x_wmax: 
		code |= RIGHT
	if y < y_wmin:	 
		code |= BOTTOM
	elif y > y_wmax: 
		code |= TOP

	return code



def cohenSutherlandAlgo(x1, y1, x2, y2):

    gfxdraw.line(screen, x1, y1, x2, y2, Red)

    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            if code_out & TOP:
                x = x1 + (x2 - x1) * \
                                (y_wmax - y1) / (y2 - y1)
                y = y_wmax
            elif code_out & BOTTOM:          
                x = x1 + (x2 - x1) * \
                                (y_wmin - y1) / (y2 - y1)
                y = y_wmin
            elif code_out & RIGHT:              
                y = y1 + (y2 - y1) * \
                                (x_wmax - x1) / (x2 - x1)
                x = x_wmax
            elif code_out & LEFT:               
                y = y1 + (y2 - y1) * \
                                (x_wmin - x1) / (x2 - x1)
                x = x_wmin
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)
    if accept:
        print ("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2))
        gfxdraw.line(screen, int(x1), int(y1), int(x2), int(y2), Blue)
    else:
        print("Line rejected : line lies ouside the window") # line lies ouside the window
        
cohenSutherlandAlgo(150, 150, 450, 450)
cohenSutherlandAlgo(40, 70, 350, 40)
cohenSutherlandAlgo(150,320,273,200)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
