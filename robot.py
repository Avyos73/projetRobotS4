from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from math import sqrt,asin
import board
from time import sleep

import neopixel

from connectionServ import connectToServ


class Motor:
    def __init__(self,pin1,pin2,pin3):
        self.forward =  DigitalOutputDevice(pin1)
        self.backward =  DigitalOutputDevice(pin2)
        self.vel = PWMOutputDevice(pin3, frequency=1000)
        
class Led:

    def __init__(self,ledpin,nbrLed):
        self.strip = neopixel.NeoPixel(ledpin, nbrLed, brightness=0.1, auto_write=False)

    def allumerLed(self,numLed, color):
        self.pixels[numLed] = color
        self.pixels.show()
    
    def eteindreLed(self,numLed):
        self.pixels[numLed] = (0,0,0)
        
    def rainbow(self):
        for i in range(255):
            self.strip.fill((i,255-i,0))
            self.strip.show()
            sleep(0.1)
        for i in range(255):
            self.strip.fill((255-i,0,i))
            self.strip.show()
            sleep(0.1)
        for i in range(255):
            self.strip.fill((0,i,255-i))
            self.strip.show()
            sleep(0.1)
        self.strip.fill((0,0,0))
        self.strip.show()


class Robot:
    def __init__(self,color):
        self.posX = 0
        self.posY = 0
        self.motors = [Motor(4,3,2),Motor(27,22,10),Motor(13,6,5)]
        self.controller1 = DigitalOutputDevice(17)
        self.controlleur2 = DigitalOutputDevice(19)
        self.color = color
        self.led = Led(board.D14,33)
        self.score = 0

    def getOnController(self):
        self.controller1.value = True
        self.controlleur2.value = True
    
    def getOffController(self):
        self.controller1.value = False
        self.controlleur2.value = False


    def getCoor(self):
        self.posX,self.posY = connectToServ("192.168.0.1",12345,f"G{self.color[0].upper()}P")
    
    def getScore(self):
        self.score = connectToServ("192.168.0.1",12345,f"G{self.color[0].upper()}S")

    def getObjectif(self):
        x, y = connectToServ("192.168.0.1",12345,'GTP')
        return (x,y)

    def getRobotRad(self):
        lstcoord = []
        for i in range(0,3,2):
            self.led.allumerLed(i,self.color)
            lstcoord.append(self.getCoor())
            self.led.eteindreLed(i)
        rad = asin((lstcoord[0][1]-lstcoord[1][1])/sqrt((lstcoord[1][0]-lstcoord[0][0])**2+(lstcoord[1][1]-lstcoord[0][1])**2))
        return rad
    
    def goto(self,x,y,w):
        lst = [(2/3)*x  + (1/3)*w,
               (-1/3)*x + (-sqrt(3)/3)*y + (1/3)*w,
               (-1/3)*x + (sqrt(3)/3)*y  + (1/3)*w]
        if lst[0] != 0 and lst[1] != 0 and lst[2] != 0:
            coef = 1/max(abs(lst[0]),abs(lst[1]),abs(lst[2]))
        else:
            coef = 1

        for i in range(3):
            self.motors[i].forward.value = False
            self.motors[i].backward.value = False
            if lst[i] > 0:
                self.motors[i].forward.value = True
                self.motors[i].vel.value = abs(lst[i] * coef*0.25)
            elif lst[i] < 0:
                self.motors[i].backward.value = True
                self.motors[i].vel.value = abs(lst[i] * coef*0.25)


    def stop(self):
        for m in self.motors:
            m.forward.value = False
            m.backward.value = False
            m.vel.value = 0

    