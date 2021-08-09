



import pygame,math
import numpy as np
pygame.init()

clock = pygame.time.Clock()
wn_width = 800
wn_height = 700
wn = pygame.display.set_mode((wn_width,wn_height))

Black = (0,0,0)
Blue = (0,0,255)
cyan = (0,255,255)
Green= (0,255,0)
purple = (255,0,255)
Red= (255,0,0)
white = (255,255,255)

state = True

while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state=False
            
            
            
    
            
    wn.fill(Black)
    
    
    
  
  
    
    
    def scaling():
        pygame.display.set_caption('Scaling cyan = original triangle and Blue = Scaled triangle')
        sx,sy = (5,5)
        angle = math.pi
        x1,y1 = (10,4)
        x2,y2 = (35,4)
        x3,y3 = (35,25)
        
        s_matrix = [[sx,0,0],[0,sy,0],[0,0,1]]
        
        pygame.draw.polygon(wn,cyan,[[x1,y1],[x2,y2],[x3,y3]])
        
        h_coordinate = [[x1,x2,x3],[y1,y2,y3],[1,1,1]]
        
        
        ans = np.dot(s_matrix, h_coordinate)
        #Scaled Triangle coordinates
        s_x1,s_y1 = (ans[0][0], ans[1][0])
        s_x2,s_y2 = (ans[0][1], ans[1][1])
        s_x3,s_y3 = (ans[0][2], ans[1][2])
        
        pygame.draw.polygon(wn,Blue,[[s_x1,s_y1],[s_x2,s_y2],[s_x3,s_y3]])
        
        
        
        
        
    def translate():
        pygame.display.set_caption('Translation cyan = original triangle and Blue = Translated triangle')
        tx,ty = (30,100)
        x1,y1 = (100,40)
        x2,y2 = (300,80)
        x3,y3 = (200,120)
        t_matrix = [[1,0,tx],[0,1,ty],[0,0,1]]
        h_coordinate = [[x1,x2,x3],[y1,y2,y3],[1,1,1]]
        
        pygame.draw.polygon(wn,cyan,[[x1,y1],[x2,y2],[x3,y3]])
        
        
        
        ans = np.dot(t_matrix, h_coordinate)
        #Translated Triangle coordinates
        t_x1,t_y1 = (ans[0][0], ans[1][0])
        t_x2,t_y2 = (ans[0][1], ans[1][1])
        t_x3,t_y3 = (ans[0][2], ans[1][2])
        
        #make final triangle
        pygame.draw.polygon(wn,Blue,[[t_x1,t_y1],[t_x2,t_y2],[t_x3,t_y3]])
        
        
    def rotation():
        pygame.display.set_caption('Rotation cyan = original triangle and Blue = rotated triangle')
        angle = 120
        x1,y1 = (30,12)
        x2,y2 = (105,12)
        x3,y3 = (210,75)
        r_matrix = [[math.cos(angle),-math.sin(angle),0],[math.sin(angle),math.cos(angle),0],[0,0,1]]
        h_coordinate = [[x1,x2,x3],[y1,y2,y3],[1,1,1]]
        # initial triangle
        pygame.draw.polygon(wn,cyan,[[x1,y1],[x2,y2],[x3,y3]])
        
        
        ans = np.dot(r_matrix, h_coordinate)
        #Rotated Triangle coordinates
        r_x1,r_y1 = (ans[0][0], ans[1][0])
        r_x2,r_y2 = (ans[0][1], ans[1][1])
        r_x3,r_y3 = (ans[0][2], ans[1][2])
        
        # final trianfle
        pygame.draw.polygon(wn,Blue,[[r_x1,r_y1],[r_x2,r_y2],[r_x3,r_y3]])
    
        
    def reflection():
        pygame.display.set_caption('Reflection cyan = original triangle and Blue = reflected triangle')
        
        x1,y1 = (30,12)
        x2,y2 = (105,12)
        x3,y3 = (105,75)
    #reflection_when x=y
        rf_matrix = [[0,1,0],[1,0,0],[0,0,1]]

        h_coordinate = [[x1,x2,x3],[y1,y2,y3],[1,1,1]]
        pygame.draw.polygon(wn,cyan,[[x1,y1],[x2,y2],[x3,y3]])
        
    #initial triangle
        ans = np.dot(rf_matrix, h_coordinate)
         #Reflected Triangle co-ordinate
        rf_x1,rf_y1 = (ans[0][0], ans[1][0])
        rf_x2,rf_y2 = (ans[0][1], ans[1][1])
        rf_x3,rf_y3 = (ans[0][2], ans[1][2])
        pygame.draw.polygon(wn,Blue,[[rf_x1,rf_y1],[rf_x2,rf_y2],[rf_x3,rf_y3]])
            
    def shearing():
        pygame.display.set_caption('Shearing cyan = original triangle and Blue = Sheared triangle')
        x1,y1 = (90,36)
        x2,y2 = (315,36)
        x3,y3 = (315,225)
        shx,shy = (1,2)
        #reflection_about_X axis
        sh_matrix = [[1,shx,0],[0,1,0],[0,0,1]]
        
        h_coordinate = [[x1,x2,x3],[y1,y2,y3],[1,1,1]]
        pygame.draw.polygon(wn,cyan,[[x1,y1],[x2,y2],[x3,y3]])
        
        
        # initial triangle
        
        ans = np.dot(sh_matrix, h_coordinate)
        #Sheared Triangle coordinates
        sh_x1,sh_y1 = (ans[0][0], ans[1][0])
        sh_x2,sh_y2 = (ans[0][1], ans[1][1])
        sh_x3,sh_y3 = (ans[0][2], ans[1][2])
        pygame.draw.polygon(wn,Blue,[[sh_x1,sh_y1],[sh_x2,sh_y2],[sh_x3,sh_y3]])
    # scaling()
    # translate()
    # rotation()
    # reflection()
    shearing()          
    pygame.display.update()
    clock.tick(30)
pygame.display.flip()           
pygame.quit()
quit()