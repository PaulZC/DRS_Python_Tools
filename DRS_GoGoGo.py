# Simple Python script to release the DRS by sending "GoGoGo\n" to the serial port

import serial

try:
	yes_no = raw_input('Are you sure? (y/N) ')
except:
	yes_no = ''

if yes_no == '': yes_no = 'n'

if (yes_no == 'Y') or (yes_no == 'y'):
	try:
		ser = serial.Serial('/dev/ttyS0', 9600, timeout=1) # Try to open the serial port
	except:
		raise ValueError('Could not open serial port!')

	ser.write('GoGoGo\n') # Send the Go command

	try:
		ser.close()
	except:
		pass
