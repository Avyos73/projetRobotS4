
import pygame
from robot import Robot
from connectionServ import connectToServ
from time import sleep

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
