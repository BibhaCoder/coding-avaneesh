from processing import*
import random
import time
def setup():

  size(500,500)
  global ySpeed, gravity, birdY
  gravity = 0.1
  ySpeed = 0
  global flappyImage
  global pipeImage
  global topPipeY
  topPipeY = random.randint(-300, -100)
  flappyImage = loadImage("download (1).png")
  pipeImage = loadImage("FlappyBird12.jpg")
  global bottomPipeX, bottomPipeY
  bottomPipeY = topPipeY + 300 + 150
  bottomPipeX = 100
  global topPipeX
  
  topPipeX = 500
  birdY = 200

start_time = int(time.time())
birdSpeed = 5

def draw():
  global ySpeed, gravity, birdY, flappyImage, topPipeX, bottomPipeX, pipeImage, topPipeY, bottomPipeY, birdSpeed
  background(7, 250, 234)  
  #rect(100,birdY,30,30) 
  image(flappyImage, birdSpeed,birdY,50,50)
  ySpeed -= gravity
  end_time = int(time.time())
  elapsed_time = end_time - start_time 
  if (birdY < topPipeY + 300 or birdY + 50 > bottomPipeY) and 100 + 50 > topPipeX and 100 < topPipeX + 50:
    print("hit")
    print ("You survived for " + str(elapsed_time) + " seconds")
    quit()
  
    
      

  image(pipeImage, bottomPipeX, bottomPipeY, 50, 200)
  bottomPipeX -= 5

  image(pipeImage, topPipeX, topPipeY, 50, 300)
  topPipeX -= 5
  birdY -= ySpeed
  
  bottomPipeX = topPipeX
  if topPipeX < -50:
    topPipeX = 500
    topPipeY = random.randint(-250, -100)
    topPipeX += 10
    #print birdSpeed
    
    bottomPipeY = topPipeY + 340 + 150
    #print elapsed_time
    
  if keyPressed:
    if key == " ":
      ySpeed = 3
  if birdY > 500:
    birdY = 300
    quit()






run()
