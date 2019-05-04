# Simple Python script to pull the serial Tx pin low
# to prevent it from powering the DRS SAMD processor

# Add "sudo python /home/pi/DRS_Python_Tools/DRS_tx_off.py" to /etc/profile
# to disable the pin on boot

import subprocess

subprocess.check_call("gpio -g mode 14 out", shell=True)
subprocess.check_call("gpio -g mode 14 down", shell=True)
