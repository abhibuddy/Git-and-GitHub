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
[# switch to different branch]
$ git checkout <branch-name>

[# To create branch name and switch to that at same time]
$ git checkout -b <new-branch-name>

[# To go back to master]
$ git checkout master 
```
> Merging Branches
```
$ git merge <branch-name>
```
> Deleting a Branch
```
$ git branch -d <branch-name>
```
> cherry-pick the changes from commit to other branch
```
$ git cherry-pick <commit-hash>

[# in case of merge conflict resolve the conflict ]
$ git cherry-pick --continue 
$ git cherry-pick --abort

[# take the changes from start to end commit]
$ git cherry-pick <start-commit-hash>^..<end-commit-hash>

```

#### Undo the changes
> restore : 
```
[# remove the file from staged area]
git restore --staged <file>

[# Reverts the file or directory to the state it was in a specific commit or branch]
git restore --source <commit> <file>
```
> reset
```
[# Keeps your changes in the staging area, but removes the last commit]
git reset --soft HEAD~1

[# move the HEAD pointer to another commit without modifying the working directory or the staging area]
git reset --soft <commit>

[# Completely wipes out changes in your working directory, staging area, and commit history]
git reset --hard HEAD~1
```
> show
```
[#show the commit details]
git show <commit-hash>

[#show the files in specific commit]
git show <commit-hash> -- <file>

[#show the changes in that tag]
git show v1.0

[# show that file in head]
git show HEAD:file.txt

[# show the names of all the files changed in that commit]
git show --name-only <commit-hash>

[# show the names and status like delete/modified of all the files changed in that commit]
git show --name-status <commit-hash>
```
#### rebase 
> rebase interactive
```
git rebase -i HEAD~n

Pick: Keep the commit as is.
Reword: Modify the commit message.
Edit: Stop at that commit to make changes.
Squash: Combine the commit with the previous commit.
Fixup: Like squash, but discards the commit message.
Drop: Remove the commit from the history.
```
> rebase the branch
```
[# on main/master branch ]
git pull && git fetch
git checkout feature-branch 
git rebase main

[# in case of conflict]
git rebase --continue
git rebase --abort
```

> stash the changes and later apply it
```
git stash

[# opens the stash list]
git stash list

[# apply the stashed changes]
git stash apply

[# apply the specific commit]
git stash apply stash@{2}

[# drop the specific commit]
git stash drop stash@{2}

[# clear all the stashed changes]
git stash clear
```


