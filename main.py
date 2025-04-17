import pygame
from robot import Robot
from connectionServ import connectToServ
from time import sleep

temps2pi = 2

def manual():
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("Aucune manette détectée.")
        return
    rbt = Robot("blue")
    rbt.getOnController()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print(f"Manette détectée : {joystick.get_name()}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                x_axis = round(joystick.get_axis(0),1)-0.1  # Axe X du stick gauche
                y_axis = round(joystick.get_axis(1),1)
            
            if event.type==pygame.JOYBUTTONDOWN:
                return
        
        # Vérifier périodiquement les valeurs des axes même sans événement
        x_axis = round(joystick.get_axis(0),1)-0.1  # Axe X du stick gauche
        y_axis = round(joystick.get_axis(1),1)
        print(f"x: {x_axis}, y: {y_axis}")

        sleep(0.1)
        rbt.goto(x_axis,y_axis,0)



def auto():
    rbt = Robot("blue")
    rbt.getOnController()
    angle = rbt.getRobotRad()
    rbt.goto(0,0,3)
    sleep(angle*temps2pi/360)
    rbt.goto(0,0,0)

    while rbt.score < 10:
        obj = rbt.getObjectif()
        rbt.goto(obj[0],obj[1],0)
        sleep(1)


def square():
    rbt = Robot("blue")
    rbt.getOnController()
    rbt.goto(1,0,0)
    
    sleep(1.5)
    rbt.goto(0,0,0)
    sleep(0.5)
    rbt.goto(0,1,0)
    sleep(1.5)
    rbt.goto(0,0,0)
    sleep(0.5)
    rbt.goto(-1,0,0)
    sleep(1.5)
    rbt.goto(0,0,0)
    sleep(0.5)
    rbt.goto(0,-1,0)
    sleep(1.5)
    rbt.goto(0,0,0)
    sleep(0.5)

def spin():
    rbt = Robot("blue")
    rbt.getOnController()
    rbt.goto(0,0,1)
    sleep(10)

    
if __name__ == "__main__":
  
    manual()