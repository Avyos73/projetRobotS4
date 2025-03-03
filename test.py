from rpi_ws281x import PixelStrip, Color
import time

# Paramètres du bandeau de LED
LED_COUNT = 60        # Nombre de LED dans le bandeau
LED_PIN = 18          # GPIO pin auquel les LED sont connectées
LED_FREQ_HZ = 800000 # Fréquence du signal
LED_DMA = 10          # DMA channel
LED_BRIGHTNESS = 255  # Luminosité des LED (0-255)
LED_INVERT = False    # Inverser le signal

# Initialisation de l'instance du bandeau de LED
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

# Fonction pour allumer toutes les LED en rouge
def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)  # Définit la couleur
        strip.show()  # Met à jour les LED
        time.sleep(wait_ms / 1000.0)

# Exemple d'utilisation : allumer toutes les LED en rouge
colorWipe(strip, Color(255, 0, 0))  # Couleur rouge (R, G, B)

# Attendre 2 secondes avant d'éteindre les LED
time.sleep(2)

# Éteindre toutes les LED
colorWipe(strip, Color(0, 0, 0))  # Éteindre toutes les LED