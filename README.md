# DRS_Python_Tools


Simple Python tools to control the Data Recovery System:

- **DRS_tx_off.py** pulls the Pi's serial Tx pin low to prevent it from supplying parasitic power to the SAMD processor. This will run automatically on boot if added to /etc/profile.
- **DRS_on.py** will set the GPIO pins to enable the latching relay and provide power to the SAMD processor. The code also restores the serial Tx pin to alt5 mode.
- **DRS_log_serial.py** runs for 5 seconds and appends any incoming serial data to DRS_serial_log.txt. You can then tail the log file to see if the GNSS receiver has established a fix.
- **DRS_GoGoGo.py** sends the GoGoGo command to the SAMD processor. Confirm with y or Y.
