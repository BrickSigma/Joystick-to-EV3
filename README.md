# Joystick-to-EV3
This program uses the power of EV3_DC and Pygame to connect your LEGO Mindstorms EV3 to any controller of joystick, including Xbox and PS.  
This was once very difficult but now it is possible.

## Libraries required
The libraries required are within the `requirements.txt` file.  
Once the libraries have installed, run the command `pip install --upgrade ev3_dc`. The reason for this is because the installed version will not work correctly with the motors.  
Along with those, if you want to connect the EV3 via USB, take a look at the [ev3_dc docs](https://ev3-dc.readthedocs.io/en/latest/examples_ev3.html#connect-with-the-ev3-device).  

## Notes  
This was built for a basic car, with steering, acceleration and brake features. It will require modification to work with your builds.  
The program will stop working when the EV3 brick is no longer in range of the computer. PLEASE BE WARNED that when it disconnects, the motors will continue to spin until you shut down the EV3 brick. The main program will also glitch and crash.
