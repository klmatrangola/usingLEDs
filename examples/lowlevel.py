# Example of low-level Python wrapper for rpi_ws281x library.
# Author: Tony DiCola (tony@tonydicola.com), Jeremy Garff (jer@jers.net)
#
# This is an example of how to use the SWIG-generated _rpi_ws281x module.
# You probably don't want to use this unless you are building your own library,
# because the SWIG generated module is clunky and verbose.  Instead look at the
# high level Python port of Adafruit's NeoPixel Arduino library in strandtest.py.
#
# This code will animate a number of WS281x LEDs displaying rainbow colors.
import time

import _rpi_ws281x as ws

# LED configuration.
LED_CHANNEL    = 0
LED_COUNT      = 144         # How many LEDs to light.
LED_FREQ_HZ    = 800000     # Frequency of the LED signal.  Should be 800khz or 400khz.
LED_DMA_NUM    = 5          # DMA channel to use, can be 0-14.
LED_GPIO       = 18         # GPIO connected to the LED signal line.  Must support PWM!
LED_BRIGHTNESS = 255        # Set to 0 for darkest and 255 for brightest
LED_INVERT     = 0          # Set to 1 to invert the LED signal, good if using NPN
							# transistor as a 3.3V->5V level converter.  Keep at 0
							# for a normal/non-inverted signal.

# Define colors which will be used by the example.  Each color is an unsigned
# 32-bit value where the lower 24 bits define the red, green, blue data (each
# being 8 bits long).
DOT_COLORS = [  0x200000,   # red
				0x201000,   # orange
				0x202000,   # yellow
				0x002000,   # green
				0x002020,   # lightblue
				0x000020,   # blue
				0x100010,   # purple
				0x200010 ]  # pink


# Create a ws2811_t structure from the LED configuration.
# Note that this structure will be created on the heap so you need to be careful
# that you delete its memory by calling delete_ws2811_t when it's not needed.
leds = ws.new_ws2811_t()

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


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		pygame.mixer.init()
		pygame.mixer.music.load("JingleBellRock.mp3")
		pygame.mixer.music.play()
		print ('Blinkey lights')
		print('guitar')
		blink(strip,Color(0, 0, 0), Color(0,255,0), 4, 7)
		blink(strip, Color(0, 0, 0), Color(0, 255, 0), 4,7)
		blink(strip, Color(0, 0, 0), Color(0, 255, 0), 1, 17)
		blink(strip, Color(0, 0, 0), Color(0, 0, 255), 2, 12)
		blink(strip, Color(0, 0, 0), Color(0, 30, 30), 5, 10)
		blink(strip, Color(0, 0, 0), Color(0, 255, 0), 1, 25)
		blink(strip, Color(0, 0, 0), Color(0, 255, 0), 8, 17)
		print('halfs')
		print('jingle bell')
		halfs(strip, Color(225,0,0), Color(0,255,0), 40)
		halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 35)
		halfs(strip, Color(225, 0, 0), Color(0, 255, 0), 37)
		halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 30)
		halfs(strip, Color(225, 0, 0), Color(0, 255, 0), 35)
		halfs(strip, Color(0, 255, 0), Color(255, 0, 0), 30)
		halfs(strip, Color(0, 0, 0), Color(0, 255, 0), 1, 55)
		print('fade in green')
		print('rock!')
		fade_in_green(strip,2)
		print ('Color wipe animations.')
		print('jigle bell swing and jingle bell bling')
		colorWipe(strip, Color(255, 0, 0))  # Red wipe
		colorWipe(strip, Color(0, 255, 0))  # Green wipe
		print('halfs')
		print('snowin and blowin')
		halfs(strip, Color(0,0,0), Color(0,0,225), 50)
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
		colorWipe(strip, Color(0,255,0),40)
		colorWipe(strip, Color(0,0,255,0),40)
		colorWipe(strip,Color(0,0,0),40)
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
		print ('Theater chase animations.')
		theaterChase(strip, Color(127, 127, 127))  # White theater chase
		theaterChase(strip, Color(127,   0,   0))  # Red theater chase
		theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
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
		every_other(strip, Color(225, 0, 0), Color(0, 255, 0),2, 2, 40)
		print('blink')
		blink(strip, Color(120, 120, 120), Color(0, 0, 0), 2, 40)
		print('jingle bell time')
		print('halfs')
		halfs(strip, Color(255, 0, 0), Color(0, 0, 0),2, 15)
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
		every_other(strip, Color(255,0,0), Color(0,255,0),4, 3, 30)
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
		fade_in_green(strip,2)
		blink(strip, Color(0, 0, 0), Color(0, 0, 0), 2, 55)
		blink(strip, Color(0, 255, 0), Color(255, 0, 0), 2, 55)
		blink(strip, Color(0, 0, 0), Color(0, 0, 0), 2, 55)



