
# Reposync  
## Auto-Update GitHub Repositories  
  
--------------------------------------------------------------
Version 1.0.8 - Released June 16, 2022

Developed using Python 3.7.1

Author: **Cameron Landers**

__Cameron's LinkedIN profile:__ 

https://www.linkedin.com/in/cameronlandersexperience/
 
__Cameron's Web Site:__

https://conversiondynamics.com

--------------------------------------------------------------
## LICENSE:

--------------------------------------------------------------
All files within this distribution, hereinafter referenced as "the program" are free to use, modify and include in your own programs, whether for personal or commercial use. The only restrictions are as follows: 
- Everything above and including this license section must be included in every copy you distribute that contains the program in whole or in part, even if you modify the accompanying code modules or the contents below. 
- Any such modification must be accompanied by a statement indicating it has been modified from this original version. 

--------------------------------------------------------------
  
## What is Reposync?
Reposync is a small utility written in Python (3.7.1) that automates git commits to online repos from a Windows platform. Although you can run Reposync directly as a stand-alone utility, it's even more powerful when called directly from the Windows task scheduler utility (Schedule Tasks). You can specify reposync.exe as the program to run within a given scheduled task. 

The Python script is compiled to an executable using pyinstaller (explained below). Note that the source script (reposync.py) is NOT intended to be run directly. The program is intended to be run from the compiled executable only. If you want to modify the reposync.py script, you will need to recompile it. More on that below.
The executable program is designed to be called from scheduled tasks to do periodic GitHub commits for any repository on any schedule you choose. 

Let's say you have developed several applications or web sites and you are using GitHub repositories for source control. You can setup scheduled tasks for each repository and call reposync from these tasks to automatically update the repos nightly. You get fully-automated daily backups of all your repos, so your latest code changes always stay in sync - you don't even have to think about it! 

## Files in the distribution 
- `reposync.exe ` - The compiled Windows executable 
- `log.exe` - The logging module (called by reposync.exe to implement the logging feature)
- `reposync.py` - The main program source code, written in Python
- `log.py` - The logging module source code, written in Python
- `Readme.md` - This file
 
## How To Use Reposync
Reposync (reposync.exe) is a Windows command-line utility. You can run it manually and specify the required parameters, or you can build a command line into a Windows Scheduled Task to update a given Github repository in a scheduled, automated fashion as mentioned above. Reposync was created for the purpose of automation.

The command line consists of the program name (reposync.exe) followed by two paramweters:
- The full local path to the target Github repository (the root folder where `.git` resides).
- The name of the target branch on GitHub where you want to commit your changes.

## Example:
`reposync.exe "c:\myapp" "main"`

Make sure to include the quotes around each parameter as shown. The above command would execute reposync.exe and pass in `c:\myapp` as the path to the target repository folder, and `main` would be used as the name of the target branch for the commit in the online GitHub repository. 

## Calling Reposync From A Windows Scheduled Task  
  
The real power of Reposync is when you call it from Scheduled Tasks for a fully automated solution. Use these steps to configure your scheduled tasks (in Windows) to call Resosync. 

>This documentation assumes some familiarity with creating Scheduled Tasks. If you've never created a Scheduled Task before, consult the Microsoft documentation first, before completing the steps below.

Open the Schedule Tasks utility, then follow these steps to create and configure a Scheduled Task to call Reposync:
- Choose _Start A Program_ and specify the full path and filename to reposync.exe as the program to be started. 
- Specify the path to your local copy of the target GitHub repository as a command line argument: this is the full path to the local repo root directory (where .git resides) where you initially cloned the repo. This path should be specified in the _Arguments_ field in the scheduled task __actions__ configuration.  

>Tip: Enclose the local repo path in double quotes "like this", regardless whether or not there are spaces in the path. This is necessary in order to successfully pass it as a command line argument to the Reposync executable.  
 
Specify whatever schedule you want-- daily, weekly, hourly, etc. based upon how often you make changes to your repo contents. 

### What It Does:

When the scheduled task fires (or when you run it manually), Reposync will change to the local repo directory that you specified in the parameter list, and then it will run the following git commands to commit any changes to the online copy of your repo: 
 
    git add . 
    git commit -m "Updated by Reposync." 
    git push origin main 

Every time `reposync.exe` runs, the path argument in the parameters you passed is used to determine where your target repo resides on disk. The program will then sync your local repo with the online github repo branch (which you also specify in the parameter list). In our example, this is the "_main_" branch. 
 
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

Along with Reposync, I have also included a logging module called **log.exe**. This module is called from within reposync.exe to provide detailed log services. A new log is generated per day that shows whn each repo was updated and what the GitHub commands returned. If changes were committed, the log will include them, the same as you would see if you ran the git commands yourself. The log is particularly helpful when debugging problems in your scheduled tasks configuration. 
 
If there were any errors returned in a given call to Reposync, in the Windows Schedule Tasks utility, select the task you want to check. Task Scheduler will show the results from the last run of the task under the `history` tab. In the `action` segment of that information, you should see "successully completed" as the result of the action that calls reposync.exe. If you see something different, that's your cue to go off and examine the reposync log. It means the script likely did not complete successfully. The reposync log will then help you determine what may have gone wrong. 

Once you get your scheduled tasks all running without errors, (a return value of "completed successfully") you're good to go.

---
[eof]  

  