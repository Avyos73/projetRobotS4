
import pygame
from robot import Robot, Led
from connectionServ import connectToServ
from time import sleep
import board

def square():
    rbt = Robot("blue")
    rbt.getOnController()
    rbt.goto(1,0,0)
    sleep(1)
    rbt.goto(0,1,0)
    sleep(1)
    rbt.goto(-1,0,0)
    sleep(1)
    rbt.goto(0,-1,0)
    sleep(1)

def spin():
    rbt = Robot("blue")
    rbt.getOnController()
    rbt.goto(0,0,1)
    sleep(10)

l = Led(board.D14,33)
l.rainbow()