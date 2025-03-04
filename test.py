import neopixel

from gpiozero import DigitalOutputDevice, PWMOutputDevice
from time import sleep

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

a = Led(21,10)