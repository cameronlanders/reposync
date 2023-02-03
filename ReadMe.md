
# Reposync  
## Auto-sync GitHub repositories  
  
--------------------------------------------------------------
Version 1.0.8 - June 16, 2022

Author: Cameron Landers

Developed using Python 3.7.1

__Cameron's LinkedIN profile:__ 

https://www.linkedin.com/in/cameronlandersexperience/
 
__Cameron's Web Site:__

https://conversiondynamics.com

### LICENSE:

This program is free to use, modify and include in your own programs, whether for personal or commercial use, provided that the above comments are included without modification.  

## Purpose:
Reposync is a small utility written in Python (3.7.1) that automates git commits to online repos from a Windows platform. Although you can run Reposync directly as a stand-alone utility, it's even more powerful when called directly from the Windows task scheduler utility (Schedule Tasks). You can specify reposync.exe as the program to run within a given scheduled task. 

The Python script is compiled to an executable using pyinstaller (explained below). 
The executable is then used in scheduled tasks to do periodic commits on any schedule you choose. 

Let's say you have several web sites or otehr applications, and you keep them all backed up periodically in GitHub repositories. You can setup scheduled tasks to update the repos nightly. This gives you fully-automated automated daily backups of all your repos, so your latest code changes are always in sync. 
 
## Calling Reposync From Windows Task Scheduler  
  
Use these steps to configure your scheduled tasks (in Windows) to call Resposync. 

From the Schedule Tasks utility:
- Choose _Start A Program_ and specify the full path and filename to reposync.exe as the program to be started. 
- Specify the path to your local copy of the target GitHub repository as a command line argument: this is the full path to the local repo root directory (where .git resides) where you initially cloned the repo. This path should be specified in the _Arguments_ field in the scheduled task __actions__ configuration.  

>Tip: Enclose the local repo path in double quotes "like this", regardless whether or not there are spaces in the path. This is necessary in order to successfully pass it as a command line argument to the Reposync executable.  
 
You can specify whatever schedule you want-- daily, weekly, hourly, etc. based upon how often you make changes to your repo contents. 

### What It Does:

When the scheduled task fires (or when you run it manually), Reposync will change to the local repo directory that you specified in the parameter list, and then it will run the following git commands to commit any changes to the online copy of your repo: 
 
    git add . 
    git commit -m "Updated by Reposync." 
    git push origin main 

Every time `reposync.exe` runs, the path argument in the parameters you passed is used to determine where your target repo resides on disk. The program will then sync your local repo with the online github repo branch (which you also specify in the parameter list). Again, by default this is the "_main_" branch. 
 
### Important Notes: 
>Reposync does **NOT** do a "git pull". It is assumed you have a local repo that was in sync at the time you setup the program and started scheduling commits. 
> 
>If you have multiple people updating your online repo branch, then you may need to add a command to the script to make it always do a "git pull" prior to the "git add ." command. Just use the other git commands in the script as a model to glean the correct syntax for the new line you want to add.  
>  
>Of course, any time you change the python script you need to recompile and redeploy the executable. Details on hiow to do that are privided below. 
 
>By default, the script updates a branch called "_main_". If your git repo master branch is not called "main" (or if you want to sync to a different branch) then you will need to update the script to target your desired branch. As mentioned above, you will then need to recompile the script and redeploy the executable to implement your changes. 

## To Recompile The Script  
If you need to make changes to the `reposync.py` script, you'll need to use pyinstaller to recompile the executable. From within the folder that contains your modified version of the script, run the following command:  

    pyinstaller --onefile reposync.py

This command will compile the python script to an executable (.exe) file. A folder called "_dist_" will be created, and the executable file will be placed there. 
 
If you plan to use Windows task scheduler to call your newly-compiled executable, you will need to copy the executable file to a permanent location where you want your scheduled tasks to find it.   

## log.py - The Logging Module

Along with Reposync, we have also included a logging module called log.py. This script is called from within Reposync to provide detailed log services. A new log is generated per day that shows what repo was called and what the GitHub commands returned. This is helpful to debug problems in your scheduled tasks configuration. 

If there were any errors returned in a given call to Reposync, in the Windows Schedule Tasks utility, select the task you want to check. task Scheduler will show the results from the last run of the task under the `history` tab. In the `action` segment of that information, you should see "successully completed" as the result of the action that calls reposync.exe. If you see something different, that's your cue to go off and examine the reposync log. It means the script likely did not complete successfully. The reposync log will then help you determine what may have gone wrong. 

Once you get your scheduled tasks all running without errors, (a return value of "completed successfully") you're good to go.

---
[eof]  

  