import setup
import RoboPiLib as RPL
import time
import threading

motorL = 0
motorR = 1

motorR_forward = 2000
motorR_backward = 1000
motorL_forward = 1000
motorL_backward = 2000

counter = 0

on_off = 0

def forward():
  RPL.servoWrite(motorL,motorL_forward)
  RPL.servoWrite(motorR,motorR_forward)

def stop():
  RPL.servoWrite(motorL, 0)
  RPL.servoWrite(motorR, 0)

def motor(x):
    if x == 0:
        stop()
    if x == 1:
        forward()


def power():
    global on_off
    on_off = on_off + 1
    on_off = on_off % 2
    return on_off

def run():
    threading.Timer(1.0, run).start #goes through it every second
    x = power()
    motor(x)


run()
