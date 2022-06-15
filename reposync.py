import subprocess
import os
import sys
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#                      ||| reposync |||
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Developed by: Cameron Landers
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# This is a python script that calls git to synchronize a local 
# github repository with it's remote origin on Github. 
#
# This script runs only on Windows. 
# A port for Unix/Linux is TBD.
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Setup:
# --------------------------------------------------------------
# 1. Compile this script to an executable (reposync.exe).
# 2. Compile the log.py script to an executable (log.exe).
# 3. Create a scheduled task for each repository you want to 
# sycnronize. 
# 
# Configure your scheduled tasks to call reposync.exe and pass 
# the path to the given repository. 
# 
# Obviously if you want to create scheduled tasks for multiple 
# repositories, you will need to schedule them each at 
# different times.
#
# This will automate synchronization of any local Github 
# repository to it's remote origin with full logging of the 
# Github output to a log file on each run.
#
# This script calls the log executable (log.exe) directly.
#
# Both reposync.exe and log.exe must reside in the same 
# directory, but that directory can be anmywhere you wish.
# --------------------------------------------------------------
# Example command for calling reposync from a schecduled task: 
# --------------------------------------------------------------
# C:\reposync\reposync.exe repopath
#
# where "repopath" is the path to your local Git repository.    
# --------------------------------------------------------------
def convertTuple(tup):
	# ----------------------------------------------------------
	# This function is called from the script below. It 
	# processes the tuple output from the subprocess 
	# communicate() command. It's purpose is to decode the value 
	# at index 0 of the tuple to a UTF8 string and return it. 
	# ----------------------------------------------------------
	str = tup[0].decode('utf-8')
	str=str.replace('\n',' ')
	str=str.replace('\r',' ')
	if ('Your branch is up to date' in str):
		str = "Local branch is already in sync with upstream."
	return str

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# MAIN SCRIPT:
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# --------------------------------------------------------------
# The target repository path is passeed on the command line.
# --------------------------------------------------------------
# The log executable (log.exe) is expected to be in the same 
# directory from which reposync.exe runs. 
# --------------------------------------------------------------
repopath = sys.argv[1]
repodrive = repopath[0:2]
logdir = os.getcwd()
logpath = logdir + "\\log.exe"
logdrive = logdir[0:2]
# --------------------------------------------------------------
# Begin a log entry for this run.
# --------------------------------------------------------------
subprocess.call([logpath, "----------------------------------------------"])
subprocess.call([logpath, "[log:] Reposync session start."])
subprocess.call([logpath, "----------------------------------------------"])
msg="[inf:] RepoPath: " + repopath
subprocess.call([logpath, msg])
# --------------------------------------------------------------
# Only run if the specified repo path exists. 
# --------------------------------------------------------------
if (os.path.isdir(repopath)):
	os.chdir(repodrive)
	os.chdir(repopath)
	# ----------------------------------------------------------
	# Run the git command.
	# ----------------------------------------------------------
	p=subprocess.Popen(["git", "add", "."], stdout=subprocess.PIPE)
	tup=p.communicate()
	# ----------------------------------------------------------
	# Pass the output from each git command (a tuple) to the 
	# convertTuple function to extract the return message. 
	# ----------------------------------------------------------
	msg=convertTuple(tup)
	# ----------------------------------------------------------
	# Pass the message to the Log executable.
	# ----------------------------------------------------------
	os.chdir(logdrive)
	os.chdir(logdir)
	if (msg):
		subprocess.call([logpath, "[git:] " + msg])
	# ----------------------------------------------------------
	# Continue with the next git command...
	# ----------------------------------------------------------
	os.chdir(repodrive)
	os.chdir(repopath)
	p=subprocess.Popen(["git", "commit", "-m", "Updated by Reposync."], stdout=subprocess.PIPE)
	tup=p.communicate()
	msg=convertTuple(tup)
	os.chdir(logdrive)
	os.chdir(logdir)
	# ----------------------------------------------------------
	# Log each Git command's output.
	# ----------------------------------------------------------
	if (msg):
		subprocess.call([logpath, "[git:] " + msg])
	os.chdir(repodrive)
	os.chdir(repopath)
	# ----------------------------------------------------------
	# Etc.
	# ----------------------------------------------------------
	p=subprocess.Popen(["git", "push"], stdout=subprocess.PIPE)
	tup=p.communicate()
	msg=convertTuple(tup)
	os.chdir(logdrive)
	os.chdir(logdir)
	if (msg):
		subprocess.call([logpath, "[git:] " + msg])
# --------------------------------------------------------------
# Final log entry for this run. 
# --------------------------------------------------------------
msg="[log:] Reposync session end."
subprocess.call([logpath, msg])
sys.exit(0)