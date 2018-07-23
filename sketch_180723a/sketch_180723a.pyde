def setup():
    global speed_x, speed_y,letter,speed
    size(1000,1000)
    background(0)
    speed_x = 0
    speed_y = 10
    speed = 0
    

def draw():
    global speed_x,speed_y, letter,speed
    background(255)
    fill(0,255,230)
    ellipse(mouseX,speed_y,50, 50)
    fill(255)
    if mouseX>=1000:
       speed = -3
    elif mouseX<=0:
       speed = 3
    speed_y=speed_y+speed

        
    
    
    
