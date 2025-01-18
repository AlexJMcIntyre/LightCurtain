import plasma
from plasma import plasma2040
import time

height = 20
width = 20

led_map = {}  # led_map holds the LED number for each (x, y) location
NUM_LEDS = width * 40

for x in range(width):
    for y in range(height):
        led_map[(x, y)] = x * 40 + y + 1

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT, color_order=plasma.COLOR_ORDER_BGR)

led_strip.start()
offset = 0.0

while True:

    offset += float(10) / 2000.0

    for i in range(NUM_LEDS):
        hue = float(i) / NUM_LEDS
        led_strip.set_hsv(i, hue+offset, 1.0, 1.0)

    time.sleep(1.0 / 60)
