## Working with GitHUb :octocat:
>make directory and intialize Git

```
$ mkdir folder
$ cd folder
$ git init
```

###### (add file in folder)

```
$ echo "# Hello World" >> README.md
$ git add README.md
$ git add . [ #for all files in one go ]
```

>commit -> checking status and -> Push to remote

```
$ git commit -m " Initial commit "
$ git status
$ git remote add origin url_dir.git
$ git push -u origin master
```
> Making change to git repository
```
[# make the changes]
$ git add .   [#add all files in one go]
$ git add <file-name>   
$ git commit -m "change greeting" 
$ git push origin master
```
> Cloning a exiting repository
```
$ git clone <github-repo-link> 
```
> Branching and merging
```
$ git checkout -b new-feature-branch
[# make chnages]
$ git add . 
$ git commit -m "Adding new feature"
$ git push origin new-feature-branch
```
> Pull changes from github
```
$ git pull origin master
```