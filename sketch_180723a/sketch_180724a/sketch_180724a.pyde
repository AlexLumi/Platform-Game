def setup():
    global speed_x, speed_y,letter,speed,background_v,level1,level2, strx, stry, randomPoints
    size(1000,1000)
    global imageList, imageIndex
    imageIndex = 0
    imageList = [loadImage("Sonic1.png"),loadImage("Sonic2.png"),loadImage("Sonic1.png"),loadImage("Sonic5.png")]
<<<<<<< HEAD
    
    randomPoints = RandomXYPoints(30)
=======
    loading_time = 0
    aLoading = 0
    timer_text = 0
    background(50,50,50)
>>>>>>> 1064dfb70a00c440058ac93cde7a0f31c22a5094

    background_v = True
    speed_x = 0
    speed_y = 10
    speed = 0
    strx = random(0,950)
    stry = random(100,900)
#-----------------------------------------------------------------------------------------------------------------------
    level1=True
#______________________________________________________________________________________________________________________   
    level2 = False
#______________________________________________________________________________________________________________________

def draw():
    global speed_x,speed_y, letter,speed,background_v,level1,level2, strx, stry, randomPoints
    global imageList, imageIndex
    
#______________________________________________________________ Under Here is the Game Over Screen
    if background_v:
        background(255)
        fill(0,255,230)
        #ellipse_x = ellipse(mouseX,speed_y,50, 50)
        #image(imageList[imageIndex],mouseX-15,speed_y-20,35,50)
        #if frameCount%50 == 0:
            #imageIndex= imageIndex + 1
            #imageIndex = imageIndex%len(imageList)
            #fill(0,255,230)
        if mouseX <= 449:
            image(imageList[3],mouseX-15,speed_y-20,35,50)
        if mouseX >= 450 and mouseX <=550 :
            image(imageList[0],mouseX-15,speed_y-20,35,50)
        if mouseX >= 551:
            image(imageList[1],mouseX-15,speed_y-20,35,50)
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
#_____________________________________________________________________________ Level 1
#     if level1:
#         line(0, 400, 100, 400) #!
#         line(200, 300, 300, 300)#!
#         line(400, 500, 500, 500)#!
#         line(200,500,300,500)#!
#         line(200,700,300,700)#!
#         line(800,200,900,200)#!
#         line(600, 700, 700, 700)#!
#         line(800, 800, 900, 800)#!
#         line(900, 900, 1000, 900)#!
    
#     if speed_y >= 400 and speed_y<=405 and mouseX >= 0 and mouseX <=100 and level1 == True: 
#         background_v = False
#     if speed_y >= 300 and speed_y<=305 and mouseX >= 200 and mouseX <=300 and level1 == True:
#         background_v = False
#     if speed_y >= 500 and speed_y <= 505 and mouseX >= 400 and mouseX <= 500 and level1 == True:
#         background_v = False
#     if speed_y >= 200 and speed_y <=205 and mouseX >= 800 and mouseX <= 900 and level1 == True:
#         background_v = False
#     if speed_y >= 700 and speed_y <=705 and mouseX >= 600 and mouseX <=700 and level1 == True:
#          background_v = False
#     if speed_y >= 900 and speed_y <=905 and mouseX >= 900 and mouseX <=1000 and level1 == True:
#         background_v = False
#     if speed_y >= 500 and speed_y <= 505 and mouseX >= 200 and mouseX<= 300 and level1 == True:
#         background_v = False
#     if speed_y >= 700 and speed_y <= 705 and mouseX >= 200 and mouseX <= 300 and level1 == True:
#          background_v = False
#     if speed_y >= 800 and speed_y <= 805 and mouseX >= 800 and mouseX <= 900 and level1 == True:
#          background_v = False
        
#     if speed_y>=1010 and level1 == True:
#         speed_y = -5
#         level1 =False
#         level2 = True
#         speed = 6
# #_______________________________________________________________________ Start of Level 2        
#     #Level2lines
#     if level2 == True:
#         line(300, 200, 400, 200)#!
#         line(350, 700, 550,  700)#!
#         line(700, 200, 900, 200)#!
#         line(0, 500, 100, 500)#!
#         line(10, 300, 210, 300)#!
#         line(900, 300, 1000, 300)#!
#         line(500, 500, 700, 500)#!
#         line(600, 400, 660, 400)#!
#         line(300, 500, 450, 500)#!
#         line(0, 800, 200, 800)#!
#         line(700, 100, 800, 100)#!
#         line(800, 800, 1000, 800)#!
#         line(600, 600, 800, 600)#!
#         line(800, 400, 900, 400)#!
#         line(500, 900, 800, 900)#!
#         line(200, 700, 500, 700)#!
#         line(0, 100, 100, 100)#!
#         line(600, 100, 800, 100)#!
        
#     if speed_y>=1010 and level1 == False:
#         level2 = False
#         speed_y = -5
#         speed = 10
        
<<<<<<< HEAD
#     if speed_y>= 200 and speed_y <=205 and mouseX >=300 and mouseX <= 400 and level2== True:
#         background_v = False
#     if speed_y >= 200 and speed_y <= 205 and mouseX >= 300 and mouseX <= 200 and level2 == True:
#         background_v = False
#     if speed_y >= 700 and speed_y <= 705 and mouseX >= 350 and mouseX <= 550 and level2 == True:
#         background_v = False
#     if speed_y >= 200 and speed_y <= 205 and mouseX >= 700 and mouseX <= 900 and level2 == True:
#         background_v = False
#     if speed_y >= 500 and speed_y <= 505 and mouseX >=0 and mouseX <= 100 and level2 == True:
#         background_v = False
#     if speed_y >= 300 and speed_y <= 305 and mouseX >= 10 and mouseX <= 210 and level2 == True:
#         background_v = False
#     if speed_y >= 300 and speed_y <= 305 and mouseX >= 900 and mouseX <= 1000 and level2 == True:
#         background_v = False
#     if speed_y >= 500 and speed_y <= 505 and mouseX >= 500 and mouseX <= 700 and level2 == True:
#         background_v = False
#     if speed_y >= 400 and speed_y <= 405 and mouseX >= 600 and mouseX <= 660 and level2 == True:
#         background_v = False
#     if speed_y >= 500 and speed_y <=505 and mouseX >= 300 and mouseX <= 450 and level2 == True:
#         background_v = False
#     if speed_y >= 800 and speed_y <= 805 and mouseX >= 0 and mouseX <= 200 and level2 == True:
#         background_v = False
#     if speed_y >= 800 and speed_y <= 805 and mouseX >= 800 and mouseX <= 1000 and level2 == True:
#         background_v = False
#     if speed_y >= 100 and speed_y <= 105 and mouseX >= 700 and mouseX <= 800 and level2 == True:
#         background_v = False
#     if speed_y >= 600 and speed_y <= 605 and mouseX >= 600 and mouseX <= 800 and level2 == True:
#         background_v = False
#     if speed_y >= 400 and speed_y <= 405 and mouseX >= 800 and mouseX <= 900 and level2 == True:
#         background_v = False
#     if speed_y >= 900 and speed_y <= 905 and mouseX >= 500 and mouseX <= 800 and level2 == True:
#         background_v = False
#     if speed_y >= 700 and speed_y <= 705 and mouseX >= 200 and mouseX <= 500 and level2 == True:
#         background_v = False
#     if speed_y >= 100 and speed_y <= 105 and mouseX >= 0 and mouseX <= 100 and level2 == True:
#         background_v = False
#     if speed_y >= 100 and speed_y <= 105 and mouseX >= 600 and mouseX <= 800 and level2 == True:
#         background_v = False
    for point in randomPoints:
        line(point[0], point[1], point[0] + 100, point[1])


def RandomXYPoints(number):
    pointlist = [] 
    
    for _ in range(number):
        strx = random(0,950)
        stry = random(100,900)
        pointlist.append([strx, stry])
    return pointlist


    



    
        
=======
    if speed_y>= 200 and speed_y <=205 and mouseX >=300 and mouseX <= 400 and level2== True:
        background_v = False
    if speed_y >= 200 and speed_y <= 205 and mouseX >= 300 and mouseX <= 200 and level2 == True:
        background_v = False
    if speed_y >= 700 and speed_y <= 705 and mouseX >= 350 and mouseX <= 550 and level2 == True:
        background_v = False
    if speed_y >= 200 and speed_y <= 205 and mouseX >= 700 and mouseX <= 900 and level2 == True:
        background_v = False
    if speed_y >= 500 and speed_y <= 505 and mouseX >=0 and mouseX <= 100 and level2 == True:
        background_v = False
    if speed_y >= 300 and speed_y <= 305 and mouseX >= 10 and mouseX <= 210 and level2 == True:
        background_v = False
    if speed_y >= 300 and speed_y <= 305 and mouseX >= 900 and mouseX <= 1000 and level2 == True:
        background_v = False
    if speed_y >= 500 and speed_y <= 505 and mouseX >= 500 and mouseX <= 700 and level2 == True:
        background_v = False
    if speed_y >= 400 and speed_y <= 405 and mouseX >= 600 and mouseX <= 660 and level2 == True:
        background_v = False
    if speed_y >= 500 and speed_y <=505 and mouseX >= 300 and mouseX <= 450 and level2 == True:
        background_v = False
    if speed_y >= 800 and speed_y <= 805 and mouseX >= 0 and mouseX <= 200 and level2 == True:
        background_v = False
    if speed_y >= 800 and speed_y <= 805 and mouseX >= 800 and mouseX <= 1000 and level2 == True:
        background_v = False
    if speed_y >= 100 and speed_y <= 105 and mouseX >= 700 and mouseX <= 800 and level2 == True:
        background_v = False
    if speed_y >= 600 and speed_y <= 605 and mouseX >= 600 and mouseX <= 800 and level2 == True:
        background_v = False
    if speed_y >= 400 and speed_y <= 405 and mouseX >= 800 and mouseX <= 900 and level2 == True:
        background_v = False
    if speed_y >= 900 and speed_y <= 905 and mouseX >= 500 and mouseX <= 800 and level2 == True:
        background_v = False
    if speed_y >= 700 and speed_y <= 705 and mouseX >= 200 and mouseX <= 500 and level2 == True:
        background_v = False
    if speed_y >= 100 and speed_y <= 105 and mouseX >= 0 and mouseX <= 100 and level2 == True:
        background_v = False
    if speed_y >= 100 and speed_y <= 105 and mouseX >= 600 and mouseX <= 800 and level2 == True:
        background_v = False     
    
    print speed
>>>>>>> 1064dfb70a00c440058ac93cde7a0f31c22a5094
