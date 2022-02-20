#!/usr/bin/env python3
# Imports
import pygame, sys
from pygame.locals import *

# Docs for ev3_dc:
# https://ev3-dc.readthedocs.io/en/latest/index.html
import ev3_dc as ev3

pygame.init()

# Connect to the EV3 brick. If it fails, an error is raised.
brick = ev3.EV3(protocol=ev3.BLUETOOTH, host='00:16:53:54:43:18')

print("Succesfully connected!")

# Create motor objects to interact and command with using the brick
motor_a = ev3.Motor(port=ev3.PORT_A, ev3_obj= brick)
motor_b = ev3.Motor(port=ev3.PORT_B, ev3_obj= brick)
motor_c = ev3.Motor(port=ev3.PORT_C, ev3_obj= brick)

# The pygame window is required to use the joystick class of pygame
WIN = pygame.display.set_mode((500, 500))

# Initialise the joystick
joystick = pygame.joystick.Joystick(0)

clock = pygame.time.Clock()
FPS = 60

def main():
    # Used for steering
    left = False
    right = False

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get all the joystick inputs for throttle, brakes, and steering
        # A formula is applied allowing variable speeds to be made depending on the axis value
        accelerate = (joystick.get_axis(5) + 1)/2
        brake = (joystick.get_axis(4) + 1)/2
        steering = joystick.get_axis(0)
        if accelerate > 0:
            if left:
                motor_b.start_move(speed=int(56*accelerate+1), direction=-1)
                motor_c.start_move(speed=int(84*accelerate+1), direction=-1)
            elif right:
                motor_b.start_move(speed=int(84*accelerate+1), direction=-1)
                motor_c.start_move(speed=int(56*accelerate+1), direction=-1)
            else:
                motor_b.start_move(speed=int(75*accelerate+1), direction=-1)
                motor_c.start_move(speed=int(75*accelerate+1), direction=-1)
        elif brake > 0:
            if left:
                motor_b.start_move(speed=int(56*brake+1), direction=1)
                motor_c.start_move(speed=int(84*brake+1), direction=1)
            elif right:
                motor_b.start_move(speed=int(84*brake+1), direction=1)
                motor_c.start_move(speed=int(56*brake+1), direction=1)
            else:
                motor_b.start_move(speed=int(75*brake+1), direction=1)
                motor_c.start_move(speed=int(75*brake+1), direction=1)
        else:
            motor_b.stop()
            motor_c.stop()
        if steering > 0.5:
            if not right:
                motor_a.move_by(-67, speed=75, brake=True).start(thread=False)
                right = True
                left = False
        elif steering < -0.5:
            if not left:
                motor_a.move_by(67, speed=75, brake=True).start(thread=False)
                left = True
                right = False
        else:
            if left:
                motor_a.move_by(-67, speed=75, brake=True).start(thread=False)
            elif right:
                motor_a.move_by(67, speed=75, brake=True).start(thread=False)
            left = False
            right = False
            motor_a.stop()

        clock.tick(FPS)

if __name__ == '__main__':
    main()