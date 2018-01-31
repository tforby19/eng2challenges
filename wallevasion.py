import setup
import RoboPiLib as RPL
import threading

motorL = 0
motorR = 1

motorR_forward = 2000
motorR_backward = 1000
motorL_forward = 1000
motorL_backward = 2000


counter = 0

def forward():
  RPL.servoWrite(motorL,motorL_forward)
  RPL.servoWrite(motorR,motorR_forward)

def stop():
  RPL.servoWrite(motorL, 0)
  RPL.servoWrite(motorR, 0)

def turnR():
      RPL.servoWrite(motorL,1450)
      RPL.servoWrite(motorR,motorR_forward)

def turnL():
      RPL.servoWrite(motorL,motorL_forward)
      RPL.servoWrite(motorR, 1550)



while counter == 0:


    front_obstacle = RPL.digitalRead(17)
    right_obstacle = RPL.digitalRead(16)
    left_obstacle = RPL.digitalRead(18)

    if front_obstacle == 1:
        forward()

    if front_obstacle == 0:
        turnL()

    if right_obstacle = 0:
        turnL()
    
