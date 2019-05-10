import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT) # blue
GPIO.setup(20, GPIO.OUT) # green
GPIO.setup(21, GPIO.OUT) # red
GPIO.setup(26, GPIO.OUT) # contrast

GPIO.output(26, GPIO.LOW) # lowest contrast

GPIO.output(16, GPIO.HIGH)
GPIO.output(20, GPIO.LOW) # green
GPIO.output(21, GPIO.HIGH)

time.sleep(1)

# off
GPIO.output(16, GPIO.HIGH)
GPIO.output(20, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)

time.sleep(1)

GPIO.output(16, GPIO.LOW) # blue
GPIO.output(20, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)

time.sleep(1)

GPIO.output(16, GPIO.HIGH)
GPIO.output(20, GPIO.HIGH)
GPIO.output(21, GPIO.LOW) # red

time.sleep(1)

GPIO.cleanup()
