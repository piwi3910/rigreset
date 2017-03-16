#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [4, 17, 27, 22]

# loop through pins and set mode and state to 'high'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 1

# main loop

try:
  GPIO.output(4, GPIO.LOW)
  print("first")
  time.sleep(SleepTimeL);
  GPIO.output(17, GPIO.LOW)
  print("second")
  time.sleep(SleepTimeL);
  GPIO.output(27, GPIO.LOW)
  print("third")
  time.sleep(SleepTimeL);
  GPIO.output(22, GPIO.LOW)
  print("forth")
  time.sleep(SleepTimeL);
  GPIO.cleanup()


# End program cleanly with keyboard
except KeyboardInterrupt:

  # Reset GPIO settings
  GPIO.cleanup()
