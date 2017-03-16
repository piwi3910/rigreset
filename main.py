#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import config

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


RelayList = [config.Relay_1, config.Relay_2, config.Relay_3, config.Relay_4]


# check how many relays are defined and add them to the list (to fix code, not working)

# i = 1
# for i in range(1, 99):
#    myTempRelayName = 'Relay_' + str(i)
#    if myTempRelayName in globals():
#        print('Relay_' + str(i))
#    else:
#        break

# add gpio pins to relay list and initialize gpio pins

def initialize_gpio():
    GPIO.setup(RelayList, GPIO.OUT, initial=GPIO.HIGH)
    #time.sleep(2)


def shutdown_rig(input_relay_number):
    GPIO.output(input_relay_number, GPIO.LOW)
    time.sleep(10)
    GPIO.output(input_relay_number, GPIO.HIGH)
    time.sleep(2)


def startup_rig(input_relay_number):
    GPIO.output(input_relay_number, GPIO.LOW)
    time.sleep(2)
    GPIO.output(input_relay_number, GPIO.HIGH)
    time.sleep(2)


# Main Loop
try:
    print('Initializing GPIOs')
    initialize_gpio()
    print('shutdown rig')
    shutdown_rig(27)
    print('startup rig')
    startup_rig(27)



except KeyboardInterrupt:
    # here you put any code you want to run before the program
    # exits when you press CTRL+C
    print("Quit!")

except:
    # this catches ALL other exceptions including errors.
    # You won't get any error messages for debugging
    # so only use it once your code is working
    print("Other error or exception occurred!")

finally:
    GPIO.cleanup()  # this ensures a clean exit
