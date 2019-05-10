# pip3 install rpi_ws281x adafruit-circuitpython-neopixel
import board
import neopixel
import time
import random

N_LEDS = 60
MAX_REVS = 15000
pixels = neopixel.NeoPixel(board.D18, N_LEDS)

def revs_to_n(revs):
	return int(N_LEDS * (revs/MAX_REVS));

while True:
	revs = random.randint(1, 15000);
	print('R', revs);
	rev_counter = revs_to_n(revs);
	print('N', rev_counter);

	for x in range(0, N_LEDS):
		if x <= rev_counter:
			g = int(100 - (x * 100/(N_LEDS - 1)))
			r = int((x * 255/(N_LEDS - 1)))
			pixels[x] = (r, g, 0)
		else:
			pixels[x] = (0, 0, 0)
	time.sleep(1)
