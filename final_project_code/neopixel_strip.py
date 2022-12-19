#Tutorial: https://learn.adafruit.com/circuitpython-led-animations/colors

import board
import neopixel
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.color import WHITE

#get board
pixel_pin = board.D5
pixel_num = 4

#set neopixel values
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.1, auto_write=False)

#speed: bigger --> slower (how fast the light moves)
#size: how many neopixel lights up at a time
#spacing: how many neopixels not lit up in between
chase = Chase(pixels, speed=0.1, size=3, spacing=6, color=WHITE)

while True:
    chase.animate()
