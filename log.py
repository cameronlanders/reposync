import sys
# --------------------------------------------------------------
#                      ||| log.py |||
# --------------------------------------------------------------
# Developed by: Cameron Landers
# --------------------------------------------------------------
# This python script is a companion to reposync.py. It logs the 
# message passed to a file named by the current date. 
# If the file exists, the message is appended. 
# If the file does not exist, it is created and the message 
# is appended.
# --------------------------------------------------------------
# Get the message
# --------------------------------------------------------------
msg = sys.argv[1]
from datetime import datetime
# --------------------------------------------------------------
# Date and time stamp
# --------------------------------------------------------------
datestamp = datetime.today().strftime('%Y-%m-%d')
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# --------------------------------------------------------------
# Open the file, log the datetim and tnhe message.
# --------------------------------------------------------------
with open('./' + datestamp + '-reposync.log', 'a') as f:
	f.write(timestamp + ' ' + msg)
	f.write('\n')