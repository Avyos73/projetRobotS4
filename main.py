import pygame
from robot import Robot
from connectionServ import connectToServ

def manual():
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("Aucune manette détectée.")
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print(f"Manette détectée : {joystick.get_name()}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                print(f"Axe {event.axis} déplacé, valeur : {event.value}")

def auto():
    pass

if __name__ == "__main__":
    manual()