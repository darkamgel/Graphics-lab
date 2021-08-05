from pygame import gfxdraw
import sys,pygame
pygame.init()

screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))
pygame.display.flip()
white = (255,255,255)
BLUE = (0, 56, 147)

pygame.display.set_caption("Midpoint Ellipse drawing algorithm")

# finding the symmetric points
def symmetry(x,y):
	x,y = int(x),int(y)
	gfxdraw.pixel(screen,x+150,y+150,BLUE)
	gfxdraw.pixel(screen,-x+150,y+150,BLUE)
	gfxdraw.pixel(screen,x+150,-y+150,BLUE)
	gfxdraw.pixel(screen,-x+150,-y+150,BLUE)

def ellipse(rx,ry):
	rx,ry = float(rx),float(ry)
	x = 0
	y = ry
 #initial value of decison parameter in region-1
	d1 = (ry**2)-(rx*rx*ry)+(1/(4*rx*rx))
	dx = float(2*ry*ry*x)
	dy = float(2*rx*rx*y)

	while dx < dy:
		if d1 < 0:
			x += 1
			dx += 2*ry*ry
			d1 += dx + ry*ry
		else:
			x += 1
			y -= 1
			dx += 2*ry*ry
			dy -= 2*rx*rx
			d1 += dx-dy+ry*ry
		symmetry(x,y)
##initial value of decison parameter in region-2
	d2=(ry*ry)*((x+1/2.0)*(x+1/2.0))+(rx*rx*(y-1)*(y-1))-(rx*rx*ry*ry)

	while y > 0:
		if d2 > 0:
			y -= 1
			dy -= 2*rx*rx
			d2 -= dy + rx*rx
		else:
			x += 1
			y -= 1
			dy -= 2*rx*rx
			dx += 2*ry*ry
			d2 += dx-dy+rx*rx
		symmetry(x,y)
	pygame.display.flip()
 #taking two different radius as ellipse has two different radius
ellipse(100,60)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()