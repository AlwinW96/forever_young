#alwin Wezenbeek 99060433
from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 1

for j in range(5):
    for i in range(5):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
        robotArm.moveLeft()
        robotArm.moveLeft()
    for i in range(1):
        robotArm.moveLeft()
        robotArm.moveLeft()
        robotArm.moveLeft()
        robotArm.moveLeft()
        robotArm.moveLeft()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()