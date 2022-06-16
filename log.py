import sys
msg = sys.argv[1]
msg = msg.replace(".. .",'...')
from datetime import datetime
datestamp = datetime.today().strftime('%Y-%m-%d')
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('./' + datestamp + '-reposync.log', 'a') as f:
	f.write(timestamp + ' ' + msg)
	f.write('\n')
sys.exit(0)
