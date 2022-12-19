import board
import time
from analogio import AnalogIn

print("yes")
from adafruit_motorkit import MotorKit

potentiometer = AnalogIn(board.A1)
kit = MotorKit(i2c=board.I2C())

threshold = 32000
open = True

while True:

    brightness = potentiometer.value
    
    print((brightness,))      # Display value


    if (brightness > threshold and open == True):
        print('bright')
        open = False
        kit.motor2.throttle = 1.0  # drive motor M1 forward at a full speed 1.0
        kit.motor3.throttle = 1.0
        time.sleep(2)

    elif (brightness < threshold and open == False):
        print('dark')
        open = True
        kit.motor2.throttle = -1.0  # drive motor M1 forward at a full speed 1.0 
        kit.motor3.throttle = -1.0
        time.sleep(2)

    else:
        kit.motor2.throttle = 0
        
    time.sleep(0.25)