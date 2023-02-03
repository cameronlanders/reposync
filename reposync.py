import subprocess
import os
import sys
# --------------------------------------------------------------
# reposync.py - version 1.0.12 - June 16, 2022
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
def cleanMessage(msg):
	# ----------------------------------------------------------
	# Convert to UTF8
	# ----------------------------------------------------------
	msg = msg.decode('utf-8')
	# ----------------------------------------------------------
	# Clean up confusing messages:
	# ----------------------------------------------------------
	strout=msg.replace('\n',' ')
	strout=strout.replace('\r','')
	strout=strout.replace("On branch main Your branch", "On branch main. Your branch")
	strout=strout.replace(".  nothing to commit", ". Nothing to commit")
	strout=strout.replace("working tree clean ", "working tree clean.")
	npos = strout.find("Your branch is up to date")
	if (npos > 7):
		strout=strout[0:npos]

	strout=strout.strip()
	if (strout=="On branch main."):
		strout = ""

	return strout

# --------------------------------------------------------------
# Configure repo, target branch and executable paths 
# --------------------------------------------------------------
repopath = sys.argv[1]
repodrive = repopath[0:2]
branch = sys.argv[2]
logdir = os.getcwd()
logpath = logdir + "\\log.exe"
logdrive = logdir[0:2]

# --------------------------------------------------------------
# Begin a log entry for this run.
# --------------------------------------------------------------
subprocess.call([logpath, "----------------------------------------------"])
subprocess.call([logpath, "[log:] Reposync session start."])
subprocess.call([logpath, "----------------------------------------------"])
msg="[inf:] RepoPath: " + repopath + ". Target branch: " + branch
subprocess.call([logpath, msg])

# --------------------------------------------------------------
# Only run if the specified repo path exists. 
# --------------------------------------------------------------
if (os.path.isdir(repopath)):
	os.chdir(repodrive)
	os.chdir(repopath)
	with subprocess.Popen(["git", "add", "."], stdout=subprocess.PIPE) as proc:
		msg=proc.stdout.read()
		# ------------------------------------------------------
		# The add output will usually be nothing. 
		# We don't want to even call cleanMessage in that case.
		# ------------------------------------------------------
		if (msg):
			msg=cleanMessage(msg)
			if (msg):
				os.chdir(logdrive)
				os.chdir(logdir)
				subprocess.call([logpath, "[git:] " + msg])
	os.chdir(repodrive)
	os.chdir(repopath)
	with subprocess.Popen(["git", "checkout", branch], stdout=subprocess.PIPE) as proc:
		msg=proc.stdout.read()
		msg=cleanMessage(msg)
		if (msg):
			os.chdir(logdrive)
			os.chdir(logdir)
			subprocess.call([logpath, "[git:] " + msg])
	os.chdir(repodrive)
	os.chdir(repopath)
	with subprocess.Popen(["git", "commit", "-m", "Updated by RepoSync."], stdout=subprocess.PIPE) as proc:
		msg=proc.stdout.read()
		msg=cleanMessage(msg)
		if (msg):
			os.chdir(logdrive)
			os.chdir(logdir)
			subprocess.call([logpath, "[git:] " + msg])
	os.chdir(repodrive)
	os.chdir(repopath)
	with subprocess.Popen(["git", "push"], stdout=subprocess.PIPE) as proc:
		msg=proc.stdout.read()
		msg=cleanMessage(msg)
		if (msg):
			os.chdir(logdrive)
			os.chdir(logdir)
			subprocess.call([logpath, "[git:] " + msg])

os.chdir(logdrive)
os.chdir(logdir)
msg="[log:] Reposync session end."
subprocess.call([logpath, msg])
sys.exit(0)
