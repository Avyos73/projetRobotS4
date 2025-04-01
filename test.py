
# Importation des bibliothèques nécessaires
from time import sleep  # Pour les délais
import RPi.GPIO as GPIO  # Pour contrôler les broches GPIO

# Configuration des broches GPIO
GPIO.setmode(GPIO.BCM)  # Mode BCM pour les numéros de broches
GPIO.setwarnings(False)  # Désactiver les avertissements GPIO

# Fréquence PWM
pwmFreq = 100  # Fréquence PWM en Hz

# Configuration des broches pour le contrôleur moteur TB6612FNG
GPIO.setup(2, GPIO.OUT)  # PWMA
GPIO.setup(3, GPIO.OUT)  # AIN1
GPIO.setup(4, GPIO.OUT)  # AIN2
GPIO.setup(17, GPIO.OUT)  # STBY
GPIO.setup(10, GPIO.OUT)  # PWMB
GPIO.setup(22, GPIO.OUT)  # BIN1
GPIO.setup(27, GPIO.OUT)  # BIN2

# Initialisation des PWM
pwma = GPIO.PWM(2, pwmFreq)  # PWMA sur la broche 18
pwmb = GPIO.PWM(10, pwmFreq)  # PWMB sur la broche 12
pwma.start(100)  # Démarrer avec un rapport cyclique de 100%
pwmb.start(100)  # Démarrer avec un rapport cyclique de 100%

# Fonctions pour contrôler les moteurs
def forward(spd):
    runMotor(0, spd, 0)
    runMotor(1, spd, 0)

def reverse(spd):
    runMotor(0, spd, 1)
    runMotor(1, spd, 1)

def turnLeft(spd):
    runMotor(0, spd, 0)
    runMotor(1, spd, 1)

def turnRight(spd):
    runMotor(0, spd, 1)
    runMotor(1, spd, 0)

def runMotor(motor, spd, direction):
    # Activer le mode STBY
    GPIO.output(25, GPIO.HIGH)  # STBY activé

    # Configuration des broches pour le moteur
    if motor == 0:  # Moteur A
        in1 = 23
        in2 = 24
        pwm = pwma
    elif motor == 1:  # Moteur B
        in1 = 22
        in2 = 27
        pwm = pwmb

    # Définir la direction
    if direction == 1:  # Marche arrière
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
    elif direction == 0:  # Marche avant
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)

    # Définir la vitesse
    pwm.ChangeDutyCycle(spd)

# Exemple d'utilisation
if __name__ == "__main__":
    try:
        forward(50)  # Avancer à 50% de la vitesse
        sleep(2)  # Attendre 2 secondes
        reverse(50)  # Reculer à 50% de la vitesse
        sleep(2)  # Attendre 2 secondes
        turnLeft(50)  # Tourner à gauche
        sleep(2)  # Attendre 2 secondes
        turnRight(50)  # Tourner à droite
        sleep(2)  # Attendre 2 secondes
    finally:
        # Nettoyer les GPIO à la fin
        pwma.stop()
        pwmb.stop()
        GPIO.cleanup()
