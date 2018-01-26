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

while counter == 0:

    RPL.digitalRead(17)

    obstacle = RPL.digitalRead(17)

    if obstacle == 1:

        forward()

    if obstacle == 0:
        RPL.servoWrite(motorL,1500)
        RPL.servoWrite(motorR,1500)
        
        stop()
        counter = counter + 1
