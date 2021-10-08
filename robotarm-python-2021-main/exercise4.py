from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for i in range(2):
    robotArm.moveRight()
robotArm.drop()
for i in range(2):
    robotArm.moveLeft()
robotArm.grab()
for i in range(3):
    robotArm.moveRight()
robotArm.drop()
for i in range(3):
    robotArm.moveLeft()
robotArm.grab()
for i in range(4):
    robotArm.moveRight()
robotArm.drop()
for i in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
for i in range(2):
    robotArm.moveRight()
robotArm.grab()
for i in range(2):
    robotArm.moveLeft()
robotArm.drop()
for i in range(3):
    robotArm.moveRight()
robotArm.grab()
for i in range(3):
    robotArm.moveLeft()
robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()