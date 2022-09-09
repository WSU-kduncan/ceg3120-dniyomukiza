# Project0 -Git Guide
  This document will take you through some basic commands you should know to useversion control with Github, but let's understand first the difference between Git and Github. **Git** is a version control system that lets you manage and keep track of your source code history while **Github** is a cloud-based hosting service that lets you manage Git repositories.

## Command line git
+ **clone**: The git clone command is used to create a copy of a specific repository or branch within a repository.
    + *options for git clone*:
      1. **git clone [url]**: Clone (download) a repository that already exists on GitHub, including all of the files, branches, and commits.
      2. **git clone --single-branch**: Clone only a single branch
      3. **git clone --sparse**: Instead of populating the working directory with all of the files in the current commit recursively, only populate the files present in the root directory. 
 + **add**: git add command adds a change in the working directory to the staging area. It tells Git that you want to include updates to a particular file in the next commit
 +     git add filename
 + **rm**: used to remove objects such as computer files, directories and symbolic links from file systems
     1.    rm file/folder will remove file locally
     2.    rm --cached file will remove file from being tracked by github
 
 + **commit**: saves a point in the project you can go back to if you find a bug, or want to make a change.
 +     commit -a: will automatically stage every changed, already tracked file
 +     commit -m: immediately creates a commit with a passed commit message
 + **push**: is used to upload local repository content to a remote repository
 +     git push
 + **fetch**: gets all the change history of a tracked branch/repo, tells the local repository that there are changes available in the remote repository without bringing the changes into the local repository.
 + **merge**: Incorporates changes from the named commits into the current branch.
 +  **pull**: does both merge and fetch together and brings the copy of the remote directory changes into the local repository
 + **branch**:we have moves current workspace from the master branch, to the new branch.
+    git branch:List all of the branches in your repository. 
+    git branch <branch>: creates a new branch.
+    git branch -D <branch>: Deletes branches even if they are unmarged things

 + **checkout**: is the command used to check out a branch. Moving us from the current branch, to the one specified at the end of the command:
**init**
**remote**
## git files & folders

## Github
## Resources
