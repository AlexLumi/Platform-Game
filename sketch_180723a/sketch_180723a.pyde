def setup():
    global speed_x, speed_y,letter,speed,background_v
    size(1000,1000)
    background_v = True
    speed_x = 0
    speed_y = 10
    speed = 0
    

def draw():
    global speed_x,speed_y, letter,speed,background_v
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
    line(0, 400, 100, 400) #started first line at 0 !
    line(200, 300, 300, 300)#!
    line(400, 500, 500, 500)#!
    line(200,500,300,500)#!
    line(200,700,300,700)#!
    line(800,200,900,200)#!
    line(600, 700, 700, 700)
    line(800, 800, 900, 800)
    line(900, 900, 1000, 900)
    if speed_y >= 400 and speed_y<=405 and mouseX >= 0 and mouseX <=100: 
        background_v = False
    if speed_y >= 300 and speed_y<=305 and mouseX >= 200 and mouseX <=300:
        background_v = False
    if speed_y >= 500 and speed_y <= 505 and mouseX >= 400 and mouseX <= 500:
        background_v = False
    if speed_y >= 200 and speed_y <=205 and mouseX >= 800 and mouseX <= 900:
        background_v = False
    if speed_y >= 700 and speed_y <=705 and mouseX >= 600 and mouseX <=700:
        background_v = False
    if speed_y >= 900 and speed_y <=905 and mouseX >= 900 and mouseX <=1000:
        background_v = False
    
        


        
    
    
    
