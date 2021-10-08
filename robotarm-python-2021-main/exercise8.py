#alwin Wezenbeek 99060433
from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()