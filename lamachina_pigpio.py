import RPi.GPIO as GPIO # built-in GPIO library for MQ-3 input handling
import pigpio # external pigpio library (daemon required) for servo handling
import time

# Pin configuration
mq3_in = 2  # GPIO 2 corresponds to pin 3 on the Raspberry Pi header
servo_control = 3

# Servo pulse width range (in microseconds)
servo_0 = 500   # Approx. 0 degrees
servo_45 = 1000 # Approx. 45 degrees - LOCKED
servo_90 = 1500  # Approx. 90 degrees
servo_180 = 2500  # Approx. 180 degrees

# Set up GPIO mode for MQ-3
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(mq3_in, GPIO.IN)  # Set GPIO 2 as an input pin

# Initialize pigpio and set up the servo pin
pi = pigpio.pi()
if not pi.connected:
    print("Failed to connect to pigpio daemon")
    exit()

# Initial lock
pi.set_servo_pulsewidth(servo_control, servo_45)

# Main
try:
    while True:
        # Read the pin state
        pin_state = GPIO.input(mq3_in)
        
        if pin_state == GPIO.HIGH:
            print("LOCKED - Alcohol not detected")
            pi.set_servo_pulsewidth(servo_control, servo_45)
            
        else:
            print("UNLOCKED - Alcohol present")
            pi.set_servo_pulsewidth(servo_control, servo_90)
        
        time.sleep(0.5)  # Add a small delay to avoid flooding the console

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    GPIO.cleanup()  # Reset GPIO settings on exit
