def setup():
    global speed_x, speed_y,letter,speed,background_v,level1_1,level1_2,level1_3,level1_4,level1_5,level1_6,level1_7,level1_8,level1_9
    size(1000,1000)
    background_v = True
    speed_x = 0
    speed_y = 10
    speed = 0
#-----------------------------------------------------------------------------------------------------------------------
    level1_1=True
    level1_2=True
    level1_3=True
    level1_4=True
    level1_5=True
    level1_6=True
    level1_7=True
    level1_8=True
    level1_9=True
#______________________________________________________________________________________________________________________    

def draw():
    global speed_x,speed_y, letter,speed,background_v,level1_1,level1_2,level1_3,level1_4,level1_5,level1_6,level1_7,level1_8,level1_9
    fill(0,255,230)
    if background_v:
        background(255)
        fill(0,255,230)
        ellipse_x = ellipse(mouseX,speed_y,50, 50)
    else:
        background(0)
        fill(random(255),random(255),random(255))
        textSize(32)
        text("GAME OVER", 400,500)
    #fill(0,255,230)
    #ellipse_x = ellipse(mouseX,speed_y,50, 50) #made the ball a variable0
    # ellipse(mouseX,speed_y,50, 50)
    fill(255)
    if mouseX>=1000:
       speed = -3
    elif mouseX<=0:
       speed = 3
    
    speed_y=speed_y+speed
    #if level1_1:
        #line(0, 400, 100, 400) #!
    #if level1_2:
        #line(200, 300, 300, 300)#!
    #if level1_3:
        #line(400, 500, 500, 500)#!
    #if level1_4:
        #line(200,500,300,500)#!
    #if level1_5:
        #line(200,700,300,700)#!
    #if level1_6:
        #line(800,200,900,200)#!
    #if level1_7:
        #line(600, 700, 700, 700)#!
    #if level1_8:
        #line(800, 800, 900, 800)#!
    #if level1_9:
        #line(900, 900, 1000, 900)#!
    
    # if speed_y >= 400 and speed_y<=405 and mouseX >= 0 and mouseX <=100 and level1_1 == True: 
    #     background_v = False
    # if speed_y >= 300 and speed_y<=305 and mouseX >= 200 and mouseX <=300 and level1_2 == True:
    #     background_v = False
    # if speed_y >= 500 and speed_y <= 505 and mouseX >= 400 and mouseX <= 500 and level1_3 == True:
    #     background_v = False
    # if speed_y >= 200 and speed_y <=205 and mouseX >= 800 and mouseX <= 900 and level1_4 == True:
    #     background_v = False
    # if speed_y >= 700 and speed_y <=705 and mouseX >= 600 and mouseX <=700 and level1_5 == True:
    #     background_v = False
    # if speed_y >= 900 and speed_y <=905 and mouseX >= 900 and mouseX <=1000 and level1_6 == True:
    #     background_v = False
    # if speed_y >= 500 and speed_y <= 505 and mouseX >= 200 and mouseX<= 300 and level1_7 == True:
    #     background_v = False
    # if speed_y >= 700 and speed_y <= 705 and mouseX >= 200 and mouseX <= 300 and level1_8 == True:
    #     background_v = False
    # if speed_y >= 800 and speed_y <= 805 and mouseX >= 800 and mouseX <= 900 and level1_9 == True:
    #     background_v = False
        
    if speed_y>=1010:
        speed_y = -10
        level1_1=False
        level1_2=False
        level1_3=False
        level1_4=False
        level1_5=False
        level1_6=False
        level1_7=False
        level1_8=False
        level1_9=False
        speed = 6
        
    #Level2lines
    line(300, 200, 400, 200)
    line(350, 700, 550,  700)
    line(700, 200, 900, 200)
    line(0, 500, 100, 500)
    line(10, 300, 210, 300)
    line(900, 300, 1000, 300)
    line(500, 500, 700, 500)
    line(600, 400, 660, 400)
    line(300, 500, 450, 500)
    line(0, 800, 200, 800)
    line(700, 100, 800, 100)
    line(800, 800, 1000, 800)
    line(600, 600, 800, 600)
    line(800, 400, 900, 400)
    line(500, 900, 800, 900)
    line(200, 700, 500, 700)
    line(0, 100, 100, 100)
    line(600, 100, 800, 100)
