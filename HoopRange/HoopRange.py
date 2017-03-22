from gamelib import *

game= Game(800, 600, "Hoop Range")
game.setMusic("HoopRange Sounds\\Statement.wav")

bk= Image("HoopRange Pictures\\court.jpg",game)
bk.resizeTo(800, 600)
game.setBackground(bk)

hoop= Image("HoopRange Pictures\\Basketball_Net.png", game)
hoop.resizeBy(-90)
hoop.setSpeed(3,75)
hoop.moveTo(200,200)

basketball= Image("HoopRange Pictures\\basketball.png", game)
basketball.resizeBy(-95)
game.time=180

#PreGame
game.drawBackground()
game.drawText("Hoop Range", game.width/2-120, game.height/2, Font(blue,72,yellow,"arial bold"))
game.drawText("Use Left Button To Shoot And The Mouse To Move", game.width/2-120, game.height/2 + 100)
game.drawText("Press [ESC] to Begin", game.width/2-220, game.height/2 + 200)
game.update()
game.wait(K_ESCAPE)

shoot= Sound("HoopRange Sounds\\swish.wav",1)
game.playMusic()

while not game.over:
    game.processInput()
    
    bk.draw()
    hoop.move(True)
    basketball.moveTo(mouse.x,mouse.y)

    if hoop.collidedWith(mouse) and mouse.LeftButton:
        xCoordinate = randint(150, 650)
        yCoordinate = randint(150, 450)
        hoop.moveTo(xCoordinate, yCoordinate)
        game.score += 1
        shoot.play()
    if game.score ==10:
        hoop.setSpeed(6,75)
    if game.score ==25:
        hoop.setSpeed(9,75)
    if game.score ==40:
        hoop.setSpeed(12,75)
     
    if game.score ==100 or game.time <=1:
        game.over=True
        game.stopMusic()    


    game.drawText("Score: " +str(game.score),100,5)
    game.drawText("High Score:100" ,400,5)
    game.displayTime(5)
    game.update(120)
game.drawText("Game Over: ",game.width/4,game.height/2,Font(red,80,black))
game.drawText("Press [ESC] to End", game.width/6, game.height/2+100,Font(black,70,red))
game.drawText("Thanks For Playing!", game.width/12, game.height/2+200,Font(black,80,red))
game.update(120)
game.wait(K_ESCAPE)
game.quit()
