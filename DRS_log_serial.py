# Simple script to append incomming GNSS data from the DRS to DRS_serial_log.txt

import time
import serial

try:
	ser = serial.Serial('/dev/ttyS0', 9600, timeout=1) # Try to open the serial port
except:
	raise ValueError('Could not open serial port!')

start_time = time.time()

while (time.time() < (start_time + 5)): # Log data for five seconds
	fp = open('DRS_serial_log.txt','a') # Open log file for append
	serdat = ser.readline() # Try and read a line of serial data
	fp.write(serdat) # Write any serial data to the log file
	fp.close() # Close the log file so we can tail it from the console

try:
	ser.close()
except:
	pass
try:
	fp.close()
except:
	pass

