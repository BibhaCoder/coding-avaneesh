import time
from processing import *
from random import *

def end_game():
    end_time = int(time.time())
    elapsed_time = end_time - start_time
    print("You dodged projectiles for " + str(elapsed_time) + " seconds!")
    print("Bullet hit player") 
    quit()

def setup():
    size(500, 500)
    global rectX, rectY
    rectX = 0
    rectY = randint(0, 500)

    global ellipseX, ellipseY
    ellipseX = 0
    ellipseY = randint(0, 500)

    global playerX, playerY
    playerX = 250
    playerY = 250

    global RonaldoImage
    RonaldoImage = loadImage("professional-football-player-cristiano-ronaldo-iphone-14wd94415iu2otop.JPEG")

start_time = int(time.time())

def draw():
    global RonaldoImage, playerX, playerY, rectX, rectY, ellipseX, ellipseY

    background(26, 118, 189)

  
    elapsed_time = int(time.time()) - start_time

    
    if elapsed_time > 10:
        rect_speed = 10
        ellipse_speed = 10
    else:
        rect_speed = 5
        ellipse_speed = 5
    if elapsed_time > 20:
        rect_speed = 15
        ellipse_speed = 15
    if elapsed_time > 25:
        rect_speed = 17.5
        ellipse_speed = 17.5
 

    if elapsed_time > 30:
      print "You won!"
      quit()
    fill(224, 13, 52)
    rect(playerX, playerY, 50, 50)
    image(RonaldoImage, playerX, playerY, 50, 50)

    
    fill(255, 0, 0)
    rect(rectX, rectY, 25, 25)
    rectX += rect_speed
    if rectX > 450:
        rectX = 0  
        rectY = randint(0, 500)

    
    fill(0, 255, 0)
    ellipse(ellipseX, ellipseY, 25, 25)
    ellipseX += ellipse_speed
    if ellipseX > 450:
        ellipseX = 0  
        ellipseY = randint(0, 500)

    
    if (playerX < rectX + 25 and playerX + 50 > rectX and 
        playerY < rectY + 25 and playerY + 50 > rectY):
        end_game()

    if (playerX < ellipseX + 25 and playerX + 50 > ellipseX and 
        playerY < ellipseY + 25 and playerY + 50 > ellipseY):
        end_game()

    
    if keyPressed:
        if key == "d":
            playerX += 6
        if key == "a":
            playerX -= 6
        if key == "w":
            playerY -= 6
        if key == "s":
            playerY += 6

run()

