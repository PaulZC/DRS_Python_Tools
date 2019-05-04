# Simple Python script to enable the DRS relay via the GPIO pins
# The code also then sets the serial Tx pin (GPIO14) back to alt5 mode
# (Raspberry Pi 3 uses alt5 instead of alt0)

# GPIO9 needs to be high to provide power to the 74LVC2G02
# GPIO10 needs to be high
# GPIO2 needs to be low

import time
import subprocess

try:
	import RPi.GPIO as GPIO
except:
	raise ValueError('Could not import RPi.GPIO. You might need to sudo?')

GPIO.setmode(GPIO.BCM) # Use GPIO numners not pin numbers
GPIO.setup(9, GPIO.OUT) # Make GPIO9 an output (provides power to the 74LVC2G02
GPIO.output(9, True) # Set GPIO9 high
GPIO.setup(10, GPIO.OUT) # Make GPIO10 an output (needs to be high to enable relay)
GPIO.output(10, True) # Set GPIO10 high
GPIO.setup(2, GPIO.OUT) # Make GPIO2 and output (needs to be low to enable relay)
GPIO.output(2, False) # Set GPIO2 low

time.sleep(2) # Wait 2 seconds

GPIO.output(2, True) # Disable the relay coil - set GPIO2 high
GPIO.output(10, False) # Ensure coil is disabled - set GPIO10 low

GPIO.cleanup() # Cleanup

# Now re-enable the Pi serial Tx pin
subprocess.check_call("gpio -g mode 14 alt5", shell=True)



