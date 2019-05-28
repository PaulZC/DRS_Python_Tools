# Simple Python script to release the DRS by sending "GoGoGo\n" to the serial port
# then initiate a shutdown

import serial
import subprocess
import time

try:
	yes_no = raw_input('Are you sure? (y/N) ')
except:
	yes_no = ''

if yes_no == '': yes_no = 'n'

if (yes_no == 'Y') or (yes_no == 'y'):
	# Make sure the Pi serial Tx pin is enabled
	subprocess.check_call("gpio -g mode 14 alt5", shell=True)
	time.sleep(0.1)

	try:
		ser = serial.Serial('/dev/ttyS0', 9600, timeout=1) # Try to open the serial port
	except:
		raise ValueError('Could not open serial port!')

	ser.write('GoGoGo\n') # Send the Go command

	print('Dropping in 30 seconds!')

	time.sleep(5) # Wait five seconds

	try:
		ser.close() # Close the serial port
	except:
		pass

	print('Shutting down...')
	time.sleep(1) # Wait an extra second

	# Shutdown now
	subprocess.check_call("sudo shutdown now", shell=True)
