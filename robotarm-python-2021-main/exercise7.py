from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:

# color = robotArm
# while color == 'blue':
robotArm.speed = 4

for j in range(5):
    for i in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for i in range(2):
        robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()