
# Reposync  
## Auto-sync github repositories  
  
Reposync is a python script that synchronizes a local github repository to it's origin on Github.  

* The script is compiled to an executable using pyinstaller (explained below). 
* The executable is then used in scheduled tasks to do autmated commits and pushes to keep any repository in sync with it's online origin.
* This script calls a separate log script to provide full logging of the output returned from each git command. 
* This script only runs on Windows. A Unix/Linux port is TBD.
 
### Important:   
>By default, the script pushes commits to a branch called "_main_" which is the latest Github established standard name for the master branch. If your git repo master branch is not called "main" (or if you want to sync to a different branch) then you will need to update the script to target your desired branch. You will then need to recompile the script and redeploy the executable to implement your changes. 

## To compile the script to an executable file  
If you need to make changes to the python script, you'll need to use pyinstaller to recompile the executable. From within the folder that contains the original reposync.py script, run the following commands to compile both the reposync.py script and the log.py script:  

    pyinstaller --onefile reposync.py
    pyinstaller --onefile log.py

These commands will compile the reposync script to an executable file (reposync.exe) and the log script to an executable file (log.exe). A folder called "_dist_" will be created, and the executable files will be placed there. 
 
Copy the executable files to a permanent location which you will specify as the path to reposync.exe in each scheduled task.  

Every time the scheduled task fires, it will run _reposync.exe_, passing the path to the local target repository. The repo will then sync with the online github repo branch that you specify in the script (again, by default this is the "_main_" branch). 
 
### Note: 
Reposync does **NOT** do a "git pull". It is assumed you have a local repo that was in sync at the time you setup the program and started scheduling commits. 
 
If you have multiple people updating your repo branch, then you may need to add a "git pull" command to the script. Just use the other git commands in the script as a guide for the correct syntax when adding the new command to be called.  
  
Of course, any time you change the python script you need to test it manually, then recompile and redeploy the executable.  

## Creating Your Scheduled tasks  
  
Use these steps to configure scheduled tasks to call resposync for each repository you wish to automate:
* Open a new scheduled task. 
* Choose _Start A Program_ and specify the full path and filename to reposync.exe as the program to be started. 
* Specify your local repo path as a command line argument: this is the full path to the local repo root directory (where .git resides) where you initially cloned the repo. 
    * This path should be specified in the `Arguments` field in the scheduled task `Actions` section.  
    * Enclose the local repo path in quotes, regardless whether or not there are spaces in the path. This is necessary in order to successfully pass it as a command line argument to the python executable.  
 
* Specify whatever schedule you want: daily, weekly, hourly, etc. based upon how often you expect to make changes to the local repository.  

When the scheduled task fires, Reposync change to the local repo directory and run the following git commands to push a new commit to the online github repo: 
 
    git add . 
    git commit -m "Updated by Reposync." 
    git push origin main 

The output returned by git for each of these commands will be logged to a file named by the current date, in the same directory where the executables reside.

[eof]  

---
Copyright ©2022 Cameron Landers, All Rights Reserved.

  