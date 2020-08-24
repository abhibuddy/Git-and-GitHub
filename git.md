## Working with GIT - git commands

> To check git installed and it's version
```
$ git --version
```
> Configure name and mail
```
$ git config --global user.name "your name"
$ git config --global user.email "your@email.com"
```
> Initializing a repository
```
$ git init
```
> Checking the status
```
$ git status
```
> Staging files
```
$ git add file.js
$ git add file1.js file2.js file3.js
$ git add .
```
> Making commits
```
$ git commit -m "commit message" 
```
> Commit history
```
$ git log
```
> Go back to Previous state
```
$ git checkout <commit-hash>
```
> To go back to latest code 
```
$ git checkout master
```
> Ignoring files
```
$ touch .gitignore
```
>Creating new Branch
```
$ git branch <new-branch-name>
```
> Changing Branches
```
$ git checkout <branch-name>
[# switch to different branch]
$ git checkout -b <new-branch-name>
[# To create branch name and switch to that at same time]
$ git checkout master 
[# To go back to master]

```
> Merging Branches
```
$ git merge <branch-name>
```
> Deleting a Branch
```
$ git branch -d <branch-name>
```