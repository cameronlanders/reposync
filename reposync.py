import subprocess
import os
import sys

def convertTuple(tup):
	str = tup[0].decode('utf-8')
	str=str.replace('\n',' ')
	str=str.replace('\r',' ')
	if ('Your branch is up to date' in str):
		str = "Local branch is already in sync with upstream."
	return str

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
msg="[inf:] RepoPath: " + repopath + ". Target branch: " + branch + "."
subprocess.call([logpath, msg])

# --------------------------------------------------------------
# Only run if the specified repo path exists. 
# --------------------------------------------------------------

if (os.path.isdir(repopath)):
	os.chdir(repodrive)
	os.chdir(repopath)
	p=subprocess.Popen(["git", "add", "."], stdout=subprocess.PIPE)
	tup=p.communicate()
	msg=convertTuple(tup)
	os.chdir(logdrive)
	os.chdir(logdir)
	if (msg):
		subprocess.call([logpath, "[git:] " + msg])
	os.chdir(repodrive)
	os.chdir(repopath)
	p=subprocess.Popen(["git", "checkout " + branch], stdout=subprocess.PIPE)
	tup=p.communicate()
	msg=convertTuple(tup)
	os.chdir(logdrive)
	os.chdir(logdir)
	if (msg):
		subprocess.call([logpath, "[git:] " + msg])
	os.chdir(repodrive)
	os.chdir(repopath)
	p=subprocess.Popen(["git", "commit", "-m", "Updated by RepoAutoSync."], stdout=subprocess.PIPE)
	tup=p.communicate()
	msg=convertTuple(tup)
	os.chdir(logdrive)
	os.chdir(logdir)
	if (msg):
		subprocess.call([logpath, "[git:] " + msg])
	os.chdir(repodrive)
	os.chdir(repopath)
	p=subprocess.Popen(["git", "push"], stdout=subprocess.PIPE)
	tup=p.communicate()
	msg=convertTuple(tup)
	os.chdir(logdrive)
	os.chdir(logdir)
	if (msg):
		subprocess.call([logpath, "[git:] " + msg])

msg="[log:] Reposync session end."
subprocess.call([logpath, msg])
sys.exit(0)