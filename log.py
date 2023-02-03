import sys
# --------------------------------------------------------------
# log.py - version 1.0.8 - June 16, 2022
# --------------------------------------------------------------
# Developed using Python 3.7.1
# --------------------------------------------------------------
# Author: Cameron Landers
# --------------------------------------------------------------
# Cameron's LinkedIN profile: 
# https://www.linkedin.com/in/cameronlandersexperience/
# 
# Cameron's Web Site:
# https://conversiondynamics.com
# --------------------------------------------------------------
# LICENSE: 
# --------------------------------------------------------------
# This program is free to use, modify and include in your own 
# programs, whether for personal or commercial use, provided 
# that the above comments are included without modification.  
# --------------------------------------------------------------
# --------------------------------------------------------------
# Purpose:
# --------------------------------------------------------------
# Logs the message specified in argv[1] to a datestamped file in 
# the directory from which it was called. 
# Currently the script will append to an existing file. If 
# the file does not exist it is created. 
# --------------------------------------------------------------
# Note:
# --------------------------------------------------------------
# The filename will be in the format: [datestamp]-reposync.log
# The script therefore generates a new log for each day that it 
# runs. To change the filename logic, modify the script below.
# --------------------------------------------------------------
msg = sys.argv[1]
msg = msg.replace(".. .",'...')
from datetime import datetime
datestamp = datetime.today().strftime('%Y-%m-%d')
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('./' + datestamp + '-reposync.log', 'a') as f:
	f.write(timestamp + ' ' + msg)
	f.write('\n')
sys.exit(0)
