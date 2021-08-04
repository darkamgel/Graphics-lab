import sys, pygame, math
from pygame import gfxdraw


class midpoint:
    

    def __init__(
        self, screen=pygame.display.set_mode((1000, 600)), x1=0, y1=0, x2=0, y2=0
    ):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.screen = screen
        self.slopeGreaterThanZero = False
        self.dx = self.x2 - self.x1
        self.dy = self.y2 - self.y1

        if abs(self.dx) < abs(self.dy):  # If |k| > 1, swap the coordinates
            self.x1, self.y1 = self.y1, self.x1
            self.x2, self.y2 = self.y2, self.x2
            self.slopeGreaterThanZero = 1
        if self.x1 > self.x2:  # Making sure that self.x1 < self.x2
            self.x1, self.x2 = self.x2, self.x1
            self.y1, self.y2 = self.y2, self.y1

        self.a = self.y1 - self.y2
        self.b = self.x2 - self.x1
        self.d = self.a + (self.b / 2)

        pygame.display.set_caption("Midpoint Algorithm Line Drawing : Red color = M > 1 , Blue color = M<1")

    def draw(self):
        "Draw the line"
        if self.y1 < self.y2:  # If slope > 0
            self.x = self.x1
            self.y = self.y1
            while self.x < self.x2:
                if self.d < 0:
                    self.y = self.y + 1
                    self.x = self.x + 1
                    self.d = self.d + self.a + self.b
                else:
                    self.d = self.d + self.a
                    self.x = self.x + 1
                if self.slopeGreaterThanZero:  # Slope > 0
                    gfxdraw.pixel(
                        self.screen,
                        math.ceil(self.y),
                        math.ceil(self.x),
                        (255, 255, 255),
                    )
                else:
                    gfxdraw.pixel(
                        self.screen,
                        math.ceil(self.x),
                        math.ceil(self.y),
                        (0, 0, 128),
                    )
        else:  # If slope <= 0
            self.x = self.x2
            self.y = self.y2
            while self.x > self.x1:
                if self.d < 0:
                    self.y = self.y + 1
                    self.x = self.x - 1
                    self.d = self.d - self.a + self.b
                else:
                    self.x = self.x - 1
                    self.d = self.d - self.a
                if self.slopeGreaterThanZero:
                    gfxdraw.pixel(
                        self.screen,
                        math.ceil(self.y),
                        math.ceil(self.x),
                        (200, 0, 0 ),
                    )
                else:
                    gfxdraw.pixel(
                        self.screen,
                        math.ceil(self.x),
                        math.ceil(self.y),
                        (200, 0, 0 ),
                    )
        pygame.display.flip()

    __call__ = draw


if __name__ == "__main__":
    midpoint(x1=100, y1=200, x2=450, y2=350).draw() # when slope is less than <1
    midpoint(x1=600, y1=200, x2=550, y2=550).draw() # when slope is less than >1
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()
