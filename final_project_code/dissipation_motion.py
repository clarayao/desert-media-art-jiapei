# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# resistor in series to the pin to visualize duty cycle changes and its impact on brightness.

import board
import busio
import time
import adafruit_lis3dh
import digitalio
from adafruit_motor import servo
from adafruit_simplemath import map_range

## Import the PCA9685 module.
import adafruit_pca9685
# Create the I2C bus interface.
i2c = busio.I2C(board.SCL, board.SDA)

#Set up servo driver
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, i2c=i2c, address=0x45)
# Set up accelerometor
int1 = digitalio.DigitalInOut(board.D6)
accel = adafruit_lis3dh.LIS3DH_I2C(int1=int1, i2c=i2c, address=0x18)
accel.range = adafruit_lis3dh.RANGE_4_G

#Initializing acceleration values
px, py, pz = accel.acceleration

# Set variable for servo rotation angle
# Variable to be influenced by input value of the accelerometer
angle_range = 60
# The larger angle_speed is, the faster the servo rotates
angle_speed = 5

while True:
    x, y, z = accel.acceleration
    dx = abs(px - x)
    dy = abs(py - y)
    sum_d = int(dx + dy)
#     print("Difference value: ", sum_d)
#     print("Difference values: ", dx, dy)
#     print("Current values: ", x)
    if sum_d > 20:
        sum_d = 20
    angle_range = int(map_range(sum_d, 0, 21, 10, 70))
    angle_speed = int(map_range(sum_d, 0, 21, 1, 10))
#     print("ANGLE RANGE IS", angle_range)
#     print("SPEED RANGE IS", angle_speed)

    #Adjust movement
    if angle_range < 20:
        angle_range = 20

    kit.servo[0].angle = 90
    kit.servo[1].angle = 90
    kit.servo[3].angle = 90
    kit.servo[2].angle = 90
    kit.servo[4].angle = 90
    kit.servo[5].angle = 90
    kit.servo[12].angle = 90
    kit.servo[13].angle = 90
    kit.servo[14].angle = 90
    kit.servo[15].angle = 90
    for angle in range(0, angle_range, angle_speed):
#         Bone 1
        kit.servo[0].angle = 90-angle
        kit.servo[1].angle = 90+angle

#         Bone 2
        kit.servo[3].angle = 90-angle
        kit.servo[2].angle = 90+angle

#         Bone 3
        kit.servo[5].angle = 90-angle
        kit.servo[4].angle = 90+angle

#         Bone 4
        kit.servo[13].angle = 90-angle
        kit.servo[12].angle = 90+angle

#         Bone 5
        kit.servo[15].angle = 90-angle
        kit.servo[14].angle = 90+angle

        time.sleep(0.05)
#     print("servo angle: ", kit.servo[0].angle)
#     print("ANGLE RANGE IS", angle_range)
    for angle in range(0, 2*angle_range, angle_speed):
#         Bone 1
        kit.servo[0].angle = 90-angle_range+angle
        kit.servo[1].angle = 90+angle_range-angle

#         Bone 2
        kit.servo[3].angle = 90-angle_range+angle
        kit.servo[2].angle = 90+angle_range-angle

#         Bone 3
        kit.servo[5].angle = 90-angle_range+angle
        kit.servo[4].angle = 90+angle_range-angle

#         Bone 4
        kit.servo[13].angle = 90-angle_range+angle
        kit.servo[12].angle = 90+angle_range-angle

#         Bone 5
        kit.servo[15].angle = 90-angle_range+angle
        kit.servo[14].angle = 90+angle_range-angle

        time.sleep(0.05)
#         print(kit.servo[0].angle)
    for angle in range(0, angle_range, angle_speed):
#         Bone 1
        kit.servo[0].angle = 90+angle_range-angle
        kit.servo[1].angle = 90-angle_range+angle

#         Bone 2
        kit.servo[3].angle = 90+angle_range-angle
        kit.servo[2].angle = 90-angle_range+angle

#         Bone 3
        kit.servo[5].angle = 90+angle_range-angle
        kit.servo[4].angle = 90-angle_range+angle

#         Bone 4
        kit.servo[13].angle = 90+angle_range-angle
        kit.servo[12].angle = 90-angle_range+angle

#         Bone 5
        kit.servo[15].angle = 90+angle_range-angle
        kit.servo[14].angle = 90-angle_range+angle
        time.sleep(0.05)

    px, py, pz = x, y, z
    #kit.servo[0].angle = 0
    #break
