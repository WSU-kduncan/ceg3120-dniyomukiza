## AUTHORIZING GITHUB
    SSH
To establish connection between your system and github  ***ssh-keygen -t ed25519 -C "your github email"***
     
     .SSH FOLDER
Folder configured for ssh as a program. Contains:

 __.ssh/  authorized_key__(stores public keys)

__.shh/known_hosts__
     (identity signatures provided during first log in)

__.shh config__
    (manages key and creates aliases)ghhgh

## GIT BASICS
__git clone__ Connects your repository to the system your using

__git add filename__ Adds file to be tracked(staging)

__git commit -m "your message"__ Saves changes made with a description message

__git push__ Syncs those committed messages with remote system(Github) 

__git status__ Gives a hint of the next steps

__.gitignore__ File holding files and folder you want to ignore(git status will no longer show the as need to be added)

__git config --global user.name "your name"__ This command saves your username

__git config --global user.email your email__ Saves your email


__git config --global core.editor vim__ Specifies editor you want to use

__git branch branchname__ Creates new branch

__git checkout branchname__ Switches to another branch

__git merge branchname__ Merge content of current branch to another branch you specified

__git rm filename__ Removes files from tracking and from disk

__git rm --cached filename__ Removes files from tracking but leaves it on the disk

__MERGE CONFLICT__: This error arises when local repositories does not have latest updates from remote repo or the other way around. Avid this by pulling from remote

       .GIT FOLDER

    
+ __hooks__ Folder containing scripts that are created before and after events like commit,etc
+ __objects__ Object database of Git
+ __config__ Local configuration file
+ __Refs__Stores information about tags and branches
+ __HEAD__ Stores reference to the current branch. Points to master branch by default
+ __index__ Binary file that stores staging information

## LINUX COMMON COMMANDS
* man command: manual pages for a command
* history: list all commands ever typed into terminal
* ls: lists all the files
* pwd: prints current directory
* cd: changes directories
* cat: prints file contents
* sudo: command after sudo has elevated priviledges
*  adduser username: creates new user
*  sudo su username: switches you to that user
*  /etc/password: stores essential information required during login
*  /etc/group:is a text file which defines the groups to which users belong
*  /etx/hostname: contains name of the machine, as known to applications that run locally
*  ls -lah: lists files and folder and permissions
*  chmod filename: changes file permissions:
     
        754 MEANS 7 for user, 5 for group and 4 for others
       
             4 - stands for read
             2 - stands for write
             1 - stands for execute
            
            In this example user is allowed to do everything, user can read and execute while other can just read
* chown username file/folder: changes owner of the file/folder
* addgroup groupname;creates new group
* chgrp groupname file/folder:changes the group of file/folder
* whoami: returns username you are using
* id: returns all the groups you are a member of
* sudo su: switches to root