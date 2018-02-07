import setup
import RoboPiLib as RPL

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

def turnL():
      RPL.servoWrite(motorL,1460)
      RPL.servoWrite(motorR,motorR_forward)

def turnR():
      RPL.servoWrite(motorL,motorL_forward)
      RPL.servoWrite(motorR, 1540)

while counter == 0:
    wallR = RPL.digitalRead(16)
    wallF = RPL.digitalRead(17)

    if wallF == 0:
        turnL()
    if wallR == 1: #nothing is there
        turnR()
    if wallR == 0: #something is there
        turnL()
