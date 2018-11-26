import time

from neopixel import *

import argparse
import signal
import sys
from Performance import *


class Wreath(Performance):
    # LED strip configuration:
    LED_COUNT = 144  # Number of LED pixels.
    LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
    # LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 10  # DMA channel to use for generating signal (try 5)
    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
    LED_STRIP = ws.WS2811_STRIP_GRB  # Strip type and colour ordering

    def blink(strip, color1, color2, repeat, wait_ms=20, iterations=5):
        for j in range(repeat):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, color1)
            strip.show()
            time.sleep(wait_ms / 100.0)
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, color2)
            strip.show()
            time.sleep(wait_ms / 100.0)

    def halfs(strip, color1, color2, wait_ms=20, iterations=5):
        for i in range(strip.numPixels() / 2):
            strip.setPixelColor(i, color1)
        for i in range(strip.numPixels() / 2, strip.numPixels()):
            strip.setPixelColor(i, color2)
        strip.show()
        time.sleep(wait_ms / 100.0)

    def fade_in_green(strip, wait_ms=20):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(255, 255, 255))
        strip.show()
        time.sleep(wait_ms / 10.0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(200, 255, 200))
        strip.show()
        time.sleep(wait_ms / 10.0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(150, 255, 150))
        strip.show()
        time.sleep(wait_ms / 10.0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(100, 255, 100))
        strip.show()
        time.sleep(wait_ms / 10.0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(50, 255, 50))
        strip.show()
        time.sleep(wait_ms / 10.0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 255, 0))
        strip.show()
        time.sleep(wait_ms / 10.0)

    # Define functions which animate LEDs in various ways.
    def colorWipe(strip, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms / 10000.0)

    def theaterChase(strip, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, color)
                strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, 0)

    def wheel(pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbow(strip, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256 * iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((i + j) & 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)

    def rainbowCycle(strip, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256 * iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)

    def theaterChaseRainbow(strip, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, wheel((i + j) % 255))
                strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i + q, 0)

    def every_other(strip, color1, color2, skip, repeat, wait_ms=20):
        for j in range(repeat):
            for i in range(0, strip.numPixels(), skip):
                strip.setPixelColor(i, color1)
            for i in range(1, strip.numPixels(), skip):
                strip.setPixelColor(i, color2)
            strip.show()
            time.sleep(wait_ms / 100.0)
            for i in range(0, strip.numPixels(), skip):
                strip.setPixelColor(i, color2)
            for i in range(1, strip.numPixels(), skip):
                strip.setPixelColor(i, color1)
            strip.show()
            time.sleep(wait_ms / 100.0)

    # Main program logic follows:
    if __name__ == '__main__':
        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL,
                                  LED_STRIP)
        # Intialize the library (must be called once before other functions).
        strip.begin()

        print('Press Ctrl-C to quit.')
        while True:
            pygame.mixer.init()
            pygame.mixer.music.load("JingleBellRock.mp3")
            pygame.mixer.music.play()
            print('Blinkey lights')
            print('guitar')
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 4, 7)
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 4, 7)
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 1, 17)
            blink(strip, Color(0, 0, 0), Color(0, 0, 255), 2, 12)
            blink(strip, Color(0, 0, 0), Color(0, 30, 30), 5, 10)
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 1, 25)
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 8, 17)
            print('halfs')
            print('jingle bell')
            halfs(strip, Color(225, 0, 0), Color(0, 255, 0), 40)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 35)
            halfs(strip, Color(225, 0, 0), Color(0, 255, 0), 37)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 30)
            halfs(strip, Color(225, 0, 0), Color(0, 255, 0), 35)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 30)
            halfs(strip, Color(0, 0, 0), Color(0, 255, 0), 1, 55)
            print('fade in green')
            print('rock!')
            fade_in_green(strip, 2)
            print('Color wipe animations.')
            print('jigle bell swing and jingle bell bling')
            colorWipe(strip, Color(255, 0, 0))  # Red wipe
            colorWipe(strip, Color(0, 255, 0))  # Green wipe
            print('halfs')
            print('snowin and blowin')
            halfs(strip, Color(0, 0, 0), Color(0, 0, 225), 50)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 50)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 25)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 50)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 25)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 30)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 15)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 15)
            print('Color wipe animations.')
            print('now the jingle hop has begun')
            colorWipe(strip, Color(255, 0, 0), 40)  # Red wipe
            colorWipe(strip, Color(0, 255, 0), 40)
            colorWipe(strip, Color(0, 0, 255, 0), 40)
            colorWipe(strip, Color(0, 0, 0), 40)
            print('jingle bell')
            halfs(strip, Color(225, 0, 0), Color(0, 255, 0), 40)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 35)
            halfs(strip, Color(225, 0, 0), Color(0, 255, 0), 37)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 30)
            halfs(strip, Color(225, 0, 0), Color(0, 255, 0), 35)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 30)
            halfs(strip, Color(255, 0, 0), Color(0, 255, 0), 1, 55)
            print('fade in green')
            print('rock!')
            fade_in_green(strip, 2)
            print('Color wipe animations.')
            print('jigle bell swing and jingle bell bling')
            colorWipe(strip, Color(255, 0, 0))  # Red wipe
            colorWipe(strip, Color(0, 255, 0))  # Green wipe
            print('halfs')
            print('dancin and prancin')
            halfs(strip, Color(0, 0, 0), Color(0, 0, 225), 50)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 50)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 25)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 50)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 25)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 30)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 225), 15)
            halfs(strip, Color(0, 0, 225), Color(0, 0, 0), 15)
            print('Color wipe animations.')
            print('in the frosty air')
            colorWipe(strip, Color(255, 0, 0), 40)  # Red wipe
            colorWipe(strip, Color(0, 0, 0), 40)  # Red wipe
            print('Theater chase animations.')
            print('freakout')
            theaterChase(strip, Color(127, 127, 127))  # White theater chase
            theaterChase(strip, Color(127, 0, 0))  # Red theater chase
            theaterChase(strip, Color(120, 255, 255))  # Cyan theater chase
            theaterChase(strip, Color(128, 255, 0))  # Lime theater chase
            rainbow(strip, 5)
            print('blinky lights')
            blink(strip, Color(135, 0, 0), Color(0, 215, 0), 1, 20)
            blink(strip, Color(0, 0, 0), Color(255, 0, 0), 1, 20)
            print('swipe')
            theaterChase(strip, Color(0, 127, 0))  # White theater chase
            theaterChase(strip, Color(127, 0, 0))  # Red theater chase
            blink(strip, Color(135, 0, 0), Color(0, 215, 0), 1, 20)
            blink(strip, Color(0, 0, 0), Color(255, 0, 0), 1, 20)
            print("rainbow blink")
            blink(strip, Color(135, 0, 0), Color(255, 128, 0), 1, 20)
            blink(strip, Color(255, 255, 0), Color(0, 255, 0), 1, 20)
            blink(strip, Color(0, 0, 255), Color(0, 215, 0), 1, 20)
            blink(strip, Color(0, 0, 0), Color(127, 0, 255), 1, 20)
            print('fade in green')
            fade_in_green(strip, 3)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 225), 50)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 50)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 25)
            print('halfs')
            halfs(strip, Color(255, 255, 0), Color(0, 0, 0), 15)
            halfs(strip, Color(0, 0, 0), Color(255, 255, 0), 15)
            halfs(strip, Color(255, 255, 0), Color(0, 0, 0), 15)
            print('Color wipe animations.')
            print('Theater chase animations.')
            theaterChase(strip, Color(127, 127, 127))  # White theater chase
            theaterChase(strip, Color(127, 0, 0))  # Red theater chase
            theaterChase(strip, Color(0, 0, 127))  # Blue theater chase
            print('blinky lights')
            every_other(strip, Color(135, 0, 0), Color(0, 215, 0), 2, 1, 10)
            every_other(strip, Color(0, 0, 0), Color(255, 0, 0), 2, 1, 10)
            print("rainbow blink")
            blink(strip, Color(135, 0, 0), Color(255, 128, 0), 1, 20)
            blink(strip, Color(255, 255, 0), Color(0, 255, 0), 1, 20)
            blink(strip, Color(0, 0, 255), Color(0, 215, 0), 1, 20)
            blink(strip, Color(0, 0, 0), Color(127, 0, 255), 1, 20)
            print('halfs')
            halfs(strip, Color(135, 0, 0), Color(255, 128, 0), 15)
            halfs(strip, Color(255, 255, 0), Color(0, 255, 0), 15)
            halfs(strip, Color(0, 0, 255), Color(0, 215, 0), 15)
            halfs(strip, Color(0, 0, 0), Color(127, 0, 255), 15)
            print('chace rainbow')
            theaterChaseRainbow(strip, 1)
            print("whipe white")
            colorWipe(strip, Color(127, 127, 127), 20)
            print('jingle bell')
            print('blink')
            every_other(strip, Color(225, 0, 0), Color(0, 255, 0), 2, 2, 40)
            print('blink')
            blink(strip, Color(120, 120, 120), Color(0, 0, 0), 2, 40)
            print('jingle bell time')
            print('halfs')
            halfs(strip, Color(255, 0, 0), Color(0, 0, 0), 2, 15)
            halfs(strip, Color(0, 0, 0), Color(255, 255, 0), 15)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 30)
            halfs(strip, Color(225, 0, 0), Color(0, 255, 0), 35)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 20)
            print("drum")
            theaterChase(strip, Color(0, 255, 0))
            print('halfs')
            halfs(strip, Color(0, 0, 0), Color(0, 0, 225), 30)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 30)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 35)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 30)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 30)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 30)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 50)
            halfs(strip, Color(255, 0, 0), Color(0, 255, 0), 50)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 25)
            halfs(strip, Color(255, 0, 0), Color(0, 255, 0), 50)
            print('blink')
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 2, 25)
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 4, 17)
            print("rainbow blink")
            blink(strip, Color(135, 0, 0), Color(255, 128, 0), 1, 40)
            blink(strip, Color(255, 255, 0), Color(0, 255, 0), 1, 40)
            blink(strip, Color(0, 0, 255), Color(0, 215, 0), 1, 40)
            blink(strip, Color(0, 0, 0), Color(127, 0, 255), 1, 40)
            print('to go ridin')
            colorWipe(strip, Color(255, 0, 0), 40)
            colorWipe(strip, Color(0, 255, 0), 40)
            print('giddy up')
            halfs(strip, Color(0, 0, 0), Color(0, 0, 225), 30)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 30)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 35)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 30)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 30)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 30)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 225), 30)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 30)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 35)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 30)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 30)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 30)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 10)
            print('jingle around')
            colorWipe(strip, Color(255, 0, 0), 30)
            colorWipe(strip, Color(0, 255, 0), 30)
            print('clock')
            theaterChase(strip, Color(127, 127, 127))
            print('mix and a mingle')
            halfs(strip, Color(255, 0, 0), Color(0, 255, 0), 30)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 30)
            halfs(strip, Color(255, 0, 0), Color(0, 255, 0), 35)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 30)
            halfs(strip, Color(255, 0, 0), Color(0, 255, 0), 30)
            halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 30)
            print('jingglin beat')
            blink(strip, Color(0, 0, 0), Color(0, 30, 30), 5, 30)
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 1, 25)
            print('thatts the jinggle bell')
            colorWipe(strip, Color(255, 0, 0), 40)
            colorWipe(strip, Color(0, 255, 0), 40)
            colorWipe(strip, Color(255, 0, 0), 40)
            print('rock')
            theaterChase(strip, Color(127, 0, 0))
            print('blinky lights')
            blink(strip, Color(135, 0, 0), Color(0, 215, 0), 1, 20)
            blink(strip, Color(0, 0, 0), Color(255, 0, 0), 1, 20)
            print('every other')
            every_other(strip, Color(255, 0, 0), Color(0, 255, 0), 4, 3, 30)
            print('blinky lights')
            blink(strip, Color(135, 0, 0), Color(0, 215, 0), 1, 20)
            blink(strip, Color(0, 0, 0), Color(255, 0, 0), 1, 20)
            print('swipe')
            theaterChase(strip, Color(0, 127, 0))  # White theater chase
            theaterChase(strip, Color(127, 0, 0))  # Red theater chase
            blink(strip, Color(135, 0, 0), Color(0, 215, 0), 1, 20)
            blink(strip, Color(0, 0, 0), Color(255, 0, 0), 1, 20)
            print("rainbow blink")
            blink(strip, Color(135, 0, 0), Color(255, 128, 0), 1, 20)
            blink(strip, Color(255, 255, 0), Color(0, 255, 0), 1, 20)
            blink(strip, Color(0, 0, 255), Color(0, 215, 0), 1, 20)
            blink(strip, Color(0, 0, 0), Color(127, 0, 255), 1, 20)
            print('fade in green')
            fade_in_green(strip, 3)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 225), 50)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 50)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 25)
            print('halfs')
            halfs(strip, Color(255, 255, 0), Color(0, 0, 0), 15)
            halfs(strip, Color(0, 0, 0), Color(255, 255, 0), 15)
            halfs(strip, Color(255, 255, 0), Color(0, 0, 0), 15)
            print('every other')
            every_other(strip, Color(0, 0, 0), Color(255, 255, 255), 2, 10, 10)
            every_other(strip, Color(255, 0, 0), Color(0, 255, 0), 4, 10, 10)
            every_other(strip, Color(0, 0, 0), Color(255, 255, 255), 2, 10, 10)
            blink(strip, Color(0, 0, 0), Color(255, 255, 255), 2, 20)
            every_other(strip, Color(255, 0, 0), Color(0, 255, 0), 4, 2, 10)
            print('halfs')
            halfs(strip, Color(135, 0, 0), Color(255, 128, 0), 15)
            halfs(strip, Color(255, 255, 0), Color(0, 255, 0), 15)
            halfs(strip, Color(0, 0, 255), Color(0, 215, 0), 15)
            halfs(strip, Color(0, 0, 0), Color(127, 0, 255), 15)
            print('bell')
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 4, 7)
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 4, 7)
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 1, 17)
            blink(strip, Color(0, 0, 0), Color(0, 0, 255), 2, 12)
            blink(strip, Color(0, 0, 0), Color(0, 30, 30), 5, 10)
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 1, 25)
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 8, 17)
            print('halfs')
            halfs(strip, Color(0, 0, 0), Color(0, 0, 225), 60)
            halfs(strip, Color(0, 0, 255), Color(0, 0, 0), 60)
            halfs(strip, Color(0, 0, 0), Color(0, 0, 255), 65)
            print('blink')
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 1, 17)
            blink(strip, Color(0, 0, 0), Color(0, 0, 255), 2, 12)
            blink(strip, Color(0, 0, 0), Color(0, 30, 30), 5, 10)
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 1, 25)
            print('color whipe')
            colorWipe(strip, Color(255, 0, 0), 40)
            colorWipe(strip, Color(0, 255, 0), 40)
            print('Theater chase animations.')
            theaterChase(strip, Color(127, 127, 127))  # White theater chase
            theaterChase(strip, Color(127, 0, 0))  # Red theater chase
            print('every other')
            every_other(strip, Color(0, 0, 0), Color(255, 255, 255), 2, 10, 10)
            every_other(strip, Color(255, 0, 0), Color(0, 255, 0), 4, 10, 10)
            print('blink')
            blink(strip, Color(0, 0, 0), Color(0, 255, 0), 5, 55)
            theaterChase(strip, Color(127, 127, 127))  # White theater chase
            fade_in_green(strip, 2)
            blink(strip, Color(0, 0, 0), Color(0, 0, 0), 2, 55)
            blink(strip, Color(0, 255, 0), Color(255, 0, 0), 2, 55)
            blink(strip, Color(0, 0, 0), Color(0, 0, 0), 2, 55)

    def do_performance(self):
        strip = self.strip
        print('Color wipe animations.')
        colorWipe(strip, Color(255, 0, 0))  # Red wipe
        if not Performance.active: return

        print('Theater chase animations.')
        theaterChase(strip, Color(127, 127, 127))  # White theater chase

        colorWipe(strip, Color(0, 255, 0))  # Blue wipe
        colorWipe(strip, Color(0, 0, 255))  # Green wipe
        if not Performance.active: return

        print('Theater chase animations.')
        theaterChase(strip, Color(127, 127, 127))  # White theater chase
        if not Performance.active: return
        theaterChase(strip, Color(127, 0, 0))  # Red theater chase
        theaterChase(strip, Color(0, 0, 127))  # Blue theater chase

        print('Rainbow animations.')
        if not Performance.active: return
        rainbow(strip)
        if not Performance.active: return
        rainbowCycle(strip)
        if not Performance.active: return
        theaterChaseRainbow(strip)
        if not Performance.active: return
        print('Off')
        colorWipe(strip, Color(0, 0, 0), 5)
