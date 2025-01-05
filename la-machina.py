import RPi.GPIO as GPIO
import time

# Pin configuration
mq3_in = 2  # GPIO 2 corresponds to pin 3 on the Raspberry Pi header
servo_control = 3

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(mq3_in, GPIO.IN)  # Set GPIO 2 as an input pin
GPIO.setup(servo_control, GPIO.OUT)

# PWM setup (pulse width modulation)
pwm = GPIO.PWM(servo_control, 50)  # 50 Hz (20 ms period)
pwm.start(0)  # Start with a duty cycle of 0

print("Monitoring GPIO 2 (pin 3). Press Ctrl+C to exit.")
pwm.ChangeDutyCycle(2.5)  # 2.5% duty cycle (approx. 0 degrees)

try:
    while True:
        # Read the pin state
        pin_state = GPIO.input(mq3_in)
        
        if pin_state == GPIO.HIGH:
            print("Alcohol not detected")
            
        else:
            print("Alcohol present")
            pwm.ChangeDutyCycle(7.5)  # 7.5% duty cycle (approx. 90 degrees)
            time.sleep(5)
            pwm.ChangeDutyCycle(2.5)  # 2.5% duty cycle (approx. 0 degrees)
        
        time.sleep(0.5)  # Add a small delay to avoid flooding the console

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    GPIO.cleanup()  # Reset GPIO settings on exit
