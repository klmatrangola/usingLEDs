import time

from examples.neopixel import *

# LED strip configuration:
LED_COUNT      = 144       # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


def blink(strip, color1, color2, repeat, wait_ms=10, iterations=5):
	for j in range(repeat):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, color1)
		strip.show()
		time.sleep(wait_ms/100.0)
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, color2)
		strip.show()
		time.sleep(wait_ms / 100.0)

def halfs(strip, color1, color2, wait_ms=20, iterations=5):
	for i in range(strip.numPixels()/2):
		strip.setPixelColor(i, color1)
	for i in range(strip.numPixels() / 2, strip.numPixels()):
		strip.setPixelColor(i, color2)
	strip.show()
	time.sleep(wait_ms / 100.0)
