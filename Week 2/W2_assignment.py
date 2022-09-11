# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

#record start time
startTime = time.monotonic()

#seconds for breathing
breathingTime = 5

#set default brightness, for future changes
bright = 0

#set increment of brightness
brightInc = 0.0005

#set default rgb value
r = 0
g = 0
b = 0

#code copied from "CircuitPython Internal RGB LED"
if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

#set the while loop according to loop within the assigned breathingTime
while (time.monotonic()-startTime) < breathingTime:
    #change the color so that the color changes within the PURPLE hue and become more sacturated
    r += 0.15
    b += 0.15
    #assign the led with the changing color
    led[0] =(r, g, b)
    #change the brightness of the led light
    bright += brightInc
    #assign the led with the changing brightness
    led.brightness = bright

#set the while loop to iterate a second time, lenghth the same as before
while (time.monotonic()-breathingTime-startTime) < breathingTime:
    #decrease the color's sacturation
    r -= 0.15
    b -= 0.15
    led[0] = (r, g, b)
    bright -= brightInc*2
    led.brightness = bright

#below there are two repetition of the "breathing process" with little changes in color
#reset all the changed variables to restart a new round of "breathing"
bright = 0
r = 0
g = 0
b = 0
while (time.monotonic()-breathingTime*2-startTime) < breathingTime:
    #change the color so that the color changes within the BLUE hue
    r += 0.05
    b += 0.15
    led[0] =(r, g, b)
    bright += brightInc
    led.brightness = bright

while (time.monotonic()-breathingTime*3-startTime) < breathingTime:
    r -= 0.05
    b -= 0.15
    led[0] = (r, g, b)
    bright -= brightInc*2
    led.brightness = bright

bright = 0
r = 0
g = 0
b = 0
while (time.monotonic()-breathingTime*4-startTime) < breathingTime:
    #change the color so that the color changes within the GREEN hue
    r += 0.05
    g += 0.15
    led[0] =(r, g, b)
    bright += brightInc
    led.brightness = bright

while (time.monotonic()-breathingTime*5-startTime) < breathingTime:
    r -= 0.05
    g -= 0.15
    led[0] = (r, g, b)
    bright -= brightInc*2
    led.brightness = bright
