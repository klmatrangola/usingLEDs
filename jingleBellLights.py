import time
import pygame

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

def blink(strip, color1, color2, repeat, wait_ms=20, iterations=5):
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

def fade_in_green(strip, wait_ms=20):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i,Color(255, 255, 255) )
	strip.show()
	time.sleep(wait_ms / 10.0)
	for i in range(strip.numPixels()):
		strip.setPixelColor(i,Color(200, 255, 200) )
	strip.show()
	time.sleep(wait_ms / 10.0)
	for i in range(strip.numPixels()):
		strip.setPixelColor(i,Color(150, 255, 150) )
	strip.show()
	time.sleep(wait_ms / 10.0)
	for i in range(strip.numPixels()):
		strip.setPixelColor(i,Color(100, 255, 100) )
	strip.show()
	time.sleep(wait_ms / 10.0)
	for i in range(strip.numPixels()):
		strip.setPixelColor(i,Color(50, 255, 50) )
	strip.show()
	time.sleep(wait_ms / 10.0)
	for i in range(strip.numPixels()):
		strip.setPixelColor(i,Color(0, 255, 0) )
	strip.show()
	time.sleep(wait_ms / 10.0)



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/10000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

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
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def every_other(strip, color1, color2, skip, repeat, wait_ms=20):
	for j in range(repeat):
		for i in range(0,strip.numPixels(),skip):
			strip.setPixelColor(i, color1)
		for i in range(1,strip.numPixels(),skip):
				strip.setPixelColor(i, color2)
		strip.show()
		time.sleep(wait_ms / 100.0)
		for i in range(0, strip.numPixels(), skip):
			strip.setPixelColor(i, color2)
		for i in range(1, strip.numPixels(), skip):
			strip.setPixelColor(i, color1)
		strip.show()
		time.sleep(wait_ms / 100.0)

def lG_beat(strip,repeat):
	for i in range(repeat):
		blink(strip, Color(0, 0, 0), Color(0, 0, 0), 1, 10)
		every_other(strip, Color(100, 0, 0), Color(0, 100, 255), 2, 5)
def lip_gloss():
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	theaterChaseRainbow(strip, 10)
	lG_beat(strip, 10)
	fade_in_green(strip, 20)
	lG_beat(strip, 14)
	wheel(255)
	lG_beat(20)
	halfs(strip, Color(200, 200, 0), Color(255, 255, 255), 5, 4)
	lG_beat(20)


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		print("Lip Gloss")
		lip_gloss()

