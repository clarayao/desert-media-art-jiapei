print("Let's blink!")

#import existing library on the board
import board
import digitalio
import time

#variable "led" gives access to the hardware pin
#digitalio is the library in circuit python
#board.LED --> give us pin LED on the board so that we could give it in/output
led = digitalio.DigitalInOut(board.LED)

#print("The basic LED is attached to pin" + board.LED)

#set the led pin as an output so we can turn it on/off
led.direction = digitalio.Direction.OUTPUT

"""
#led blinks forever
while True: #loop that keeps going
    led.value = True #light on
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5) #light off
    time.sleep(0.5) #light off
    #print("time - %f" % time.monotonic())
"""

#led blinks for 5 seconds
startTime = time.monotonic()
secondsToBlink = 5

print("start blinking")
while (time.monotonic() - startTime) < secondsToBlink:
    led.value = True #light on
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5) #light off
    time.sleep(0.5) #light off
    print("time - %.1f" % time.monotonic())
print("All done")
