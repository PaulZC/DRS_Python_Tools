# Simple Python script to release the DRS by sending "GoGoGo\n" to the serial port
# then initiate a shutdown

import serial
import subprocess
import time

# Make sure the Pi serial Tx pin is enabled
subprocess.check_call("gpio -g mode 14 alt5", shell=True)
time.sleep(0.1)

try:
        ser = serial.Serial('/dev/ttyS0', 9600, timeout=1) # Try to open the serial port
except:
        raise ValueError('Could not open serial port!')

start_time = time.time()
print ('Logging serial data to DRS_serial_log.txt for 3 seconds...')

while (time.time() < (start_time + 3)): # Log data for three seconds
	fp = open('DRS_serial_log.txt','a') # Open log file for append
	serdat = ser.readline() # Try and read a line of serial data
	fp.write(serdat) # Write any serial data to the log file
	fp.close() # Close the log file so we can tail it from the console

# Display the tail of the log file
print subprocess.check_output("tail DRS_serial_log.txt", stderr=subprocess.STDOUT, shell=True)

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
