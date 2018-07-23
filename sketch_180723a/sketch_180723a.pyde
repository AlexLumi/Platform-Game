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
    line(20, 400, 120, 400)
    line(200, 300, 300, 300)
    line(400, 500, 500, 500)
    line(200,500,300,500)
    line(200,700,300,700)
    line(800,200,900,200)
    line(600, 700, 700, 700)
    line(800, 800, 900, 800)
    line(900, 900, 1000, 900)

        
    
    
    
