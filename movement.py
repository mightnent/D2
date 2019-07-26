#coding:utf-8
import os
import sys
import time
import keyboard
import RPi.GPIO as GPIO



ENA = 13	
ENB = 20	
IN1 = 19	
IN2 = 16	
IN3 = 21	
IN4 = 26	
GPIO.setwarnings(False)

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)


def Motor_Forward():
    init()
    print('motor forward')
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1,True)
    GPIO.output(IN2,False)
    GPIO.output(IN3,True)
    GPIO.output(IN4,False)
    GPIO.cleanup()
    

def Motor_Backward():
    init()
    print('motor_backward')
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1,False)
    GPIO.output(IN2,True)
    GPIO.output(IN3,False)
    GPIO.output(IN4,True)
    GPIO.cleanup()

def Motor_TurnLeft():
    init()
    print('motor_turnleft')
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1,True)
    GPIO.output(IN2,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,True)
    time.sleep(1)
    GPIO.cleanup()

def Motor_TurnRight():
    init()
    print('motor_turnright')
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1,False)
    GPIO.output(IN2,True)
    GPIO.output(IN3,True)
    GPIO.output(IN4,False)
    time.sleep(1)
    GPIO.cleanup()

def Motor_Stop():
    init()
    print('motor stop')
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)
    GPIO.cleanup()
    

#def Thinking(n):
#   init()
#    i=1
#    while i<n:
#        print('Thinking')
#        Motor_Stop()
#        Motor_Forward()
#        i+=1
#    GPIO.cleanup()


