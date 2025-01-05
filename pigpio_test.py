limport pigpio
import time

# Pin configuration
SERVO_PIN = 3  # GPIO pin connected to the servo

# Servo pulse width range (in microseconds)
MIN_PULSE_WIDTH = 500   # Approx. 0 degrees
MID_PULSE_WIDTH = 1500  # Approx. 90 degrees
MAX_PULSE_WIDTH = 2500  # Approx. 180 degrees

# Initialize pigpio and set up the servo pin
pi = pigpio.pi()
if not pi.connected:
    print("Failed to connect to pigpio daemon")
    exit()
    
try:
    while True:
        # Move servo to 0 degrees
        print("Moving to 0 degrees")
        pi.set_servo_pulsewidth(SERVO_PIN, MIN_PULSE_WIDTH)
        time.sleep(1)

        # Move servo to 90 degrees
        print("Moving to 90 degrees")
        pi.set_servo_pulsewidth(SERVO_PIN, MID_PULSE_WIDTH)
        time.sleep(1)

        # Move servo to 180 degrees
        print("Moving to 180 degrees")
        pi.set_servo_pulsewidth(SERVO_PIN, MAX_PULSE_WIDTH)
        time.sleep(1)
        

except KeyboardInterrupt:
    print("Stopping servo control")
finally:
    # Turn off the servo signal
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    pi.stop()
