
# Reposync  
## Auto-sync github repositories  
  
Reposync is a python program that synchronizes a local github repository to it's origin on Github.  

* Reposync is intended to be called from scheduled tasks to do autmated commits and pushes to keep any repository in sync with it's online origin.
* Both the `reposync.py` and `log.py` scripts are compiled to executables for use in the scheduled tasks. 
* The program includes full logging of the output returned from each git command. The logging feature is implemented in the included log.py script.
* This program only runs on Windows. A Unix/Linux port is TBD at the time of this writing.
 
### Important:   
* It is critical that the location of **git.exe** is already included in your PATH environment variable so that git commands can be run from any directory on your machine. If not, you will need to add it. 
* By default, the script pushes commits to a branch called "_main_" which is the latest GitHub-recommended standard name for the master branch, replacing the older standard name, "_master_".  
    * If your git repo master branch is not called "main" (or if you want to sync to a different branch) then you will need to update the script to target your desired branch. You will then need to recompile the script and redeploy the executable. 

### What if you have different branch names in different repositories?  

As you can see, the script is currently designed to push commits to the same branch name in every repository. If you modify the script to target a different branch name, it will target that branch name in every repository.  

It's always a good idea to standardize your branch names across all your repositories. Most organizations use something like "dev" as their development branch and either "master" or "main" for the main branch. Regardless what name they use, it's typically the same across all their repositories. 

If the branches you want to target are actually different across different repositories, this script will not work for you as-is. You will need to modify the script to address this. 

In this case, you will need modify the script to accept an additional command line parameter for the branch name. Obviously you will also need to modify the code to utilize the passed-in parameter as the target branch name instead of having it hard-coded as it is now. This should be pretty straightforward for those familiar with Python. 

### If you need to recompile the scripts:  
If you need to make changes to the python script, you'll need to use pyinstaller to recompile the executable. From within the folder that contains the original reposync.py script, run the following commands to compile both the reposync.py script and the log.py script:  

    pyinstaller --onefile reposync.py
    pyinstaller --onefile log.py

These commands will compile the reposync script to an executable file (reposync.exe) and the log script to an executable file (log.exe). A folder called "_dist_" will be created, and the executable files will be placed there. 

> The scripts have already been compiled to executables in the dist folder within this repository. If you do not need to make any git command changes, the executables should be ready to use as they are.
 
## Deploying and Operating Reposync:  

If you do your local repository commits from a single location, the existing compiled executables are ready to use as-is. At a high level, once you have cloned the repo to your local machine, the following two steps are all you need to do in order to deploy Reposync in your environment. Details for creating the scheduled tasks are explained below.  

1. Copy the executable files to a permanent location which you will specify as the path to reposync.exe in each scheduled task.
2. Create a scheduled task for each repository you wish to automate, using the steps described below.  

### Creating Your Scheduled tasks  
  
**Use these steps to configure a scheduled task for each repository you wish to automate:**  

* Open a new scheduled task. 
* Choose _Start A Program_ and specify the full path and filename to reposync.exe as the program to be started. 
* Specify the path to the local repository from which you wish to push commits as a command line argument: this is the full drive and path to the local repo root directory (where .git resides) where you initially cloned the repo. Example: "D:\MyRepo" 
    * The local repository path must be placed in the `Arguments` field in the scheduled task's `Actions` section.  
    * The local repository path must be enclosed in quotes, regardless whether or not there are spaces in the path. This is necessary in order to successfully pass the path as a command line argument to the python executable.  
 
* Specify whatever schedule you want: daily, weekly, hourly, etc. based upon how often you expect to make changes to the local repository.  

When the scheduled task fires, Reposync will change to the specified local repository directory. It will then execute the following git commands to push a new commit to the online github repo: 
 
    git add . 
    git commit -m "Updated by Reposync." 
    git push origin main 

The output returned by git for each of these commands will be logged to a file, whose name is the current date, located in the same directory where the executables reside. So each day you'll have a new log file. It's up to you to remove old log files periodically.

---
Copyright ©2022 Cameron Landers  
This open source work is released under the <a href='https://opensource.org/licenses/MIT'>MIT License</a>:  

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
>

[eof]    