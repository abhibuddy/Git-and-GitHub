import streamlit as st

st.header(":red[git] commands")
st.caption("30 most commanly used commands")
st.divider()

st.subheader("setup and config")
st.markdown("*[1]* ***initializing git in any exiting repo***")
st.code("git init")
st.markdown("*[2]* ***clone a remote repo in pc***")
st.code("git clone <url>")
st.markdown("*[3]* ***setting and fetching config***")
st.code('''git config --global user.name 'name'
git config --global user.email 'email'
git config user.name #fetching user name''')

st.subheader("stagging and commiting")
st.markdown("*[4]* ***to stage file that are modified***")
st.code("""git add <file>
git add . #for all files""")
st.markdown("*[5]* ***commit the files in staging***")
st.code("git commit -m 'some commit message'")
st.code('git commit --amend #amends the last commit')
st.code("git commit -v #show changes being committed")
st.markdown("*[6]* ***show which file is staged/untraked or modified***")
st.code("git status")

st.subheader("branching and merging")
st.markdown("*[7]* ***List all branch***")
st.code("git branch")
st.markdown("*[8]* ***create a new branch***")
st.code("git branch <branch-name>")
st.markdown("*[9]* ***deleting branch***")
st.code("git branch -d <branch-name>")
st.code("git branch -D <branch-name> #force deleting")
st.markdown("*[10]* ***switch to an exiting branch***")
st.code("git checkout <branch-name>")
st.markdown("*[11]* ***create a new branch and switch to it***")
st.code("git checkout -b <branch-name>")
st.markdown("*[12]* ***move to specific commit***")
st.code("git checkout <commit-hash>")
st.markdown("*[13]* ***switch to previous branch***")
st.code("git checkout -")

st.subheader("undoing changes")
st.markdown("*[14]* ***discard the changes from file***")
st.code('''git checkout --<file>
git checkout . #for all files''')

st.subheader("viewing changes and diffs")
st.markdown("*[15]* ***check the differences***")
st.code('''git diff''')
st.code('''git diff <commit>''')
st.code('''git diff <branch>''')
st.markdown("*[16]* ***get the commit history***")
st.code('''git log''')
st.code('''git log --graph #get the graphical view''')
st.code("""git log --author=<author_name> #filtering by author""")
st.markdown("*[17]* ***detailed information about a specific commit***")
st.code('''git show <commit>''')
st.markdown("*[18]* ***who made the last modification***")
st.code('''git blame <file>''')

st.subheader("submodules")
st.markdown("*[19]* ***update submodule***")
st.code('''git submodule update --init''')

st.subheader("remote connection")
st.markdown("*[20]* ***forcefully making any change***")
st.code('''git push -force''')
st.markdown("*[21]* ***update local copy of the remote branches***")
st.code('''git fetch <remote>''')
st.markdown("*[22]* ***get the copy from remote***")
st.code('''git pull''')

st.subheader("Rebasing")
st.markdown("*[23]* ***Rebase you changes on  top of some other branch***")
st.code('''git checkout <master>''')
st.code('''git fetch && pull #if you don't mention anything it will take the current one''') 
st.code('''git checkout <branch>''')
st.code('''git rebase <master>''')
st.code('''git rebase --continue #Resolve Conflicts (If Any)''')
st.code('''git checkout <branch>''')
st.code('''git push origin <branch> --force''')

st.subheader("cherry-pick")
st.markdown("*[24]* ***taking individual commits from one branch and applying them to another***")
st.code("git cherry-pick <commit>")
st.code('''git cherry-pick --continue #resolve if any conflict is there''')

st.subheader("reset and revert")
st.markdown("*[25]* ***soft reset:  moves the branch pointer to a specific commit but leaves the changes in your working directory and staging area (index) intact***")
st.code("git reset --soft <commit>")
st.code("git reset --soft HEAD~1")
st.markdown("*[26]* ***hard reset: moves the branch pointer to a specific commit and forcefully discards all changes in your working directory and staging area.***")
st.code("git reset --hard <commit>")
st.code("git reset --hard HEAD~1")
st.markdown("*[27]* ***revert***")
st.code("git revert <commit>")

st.subheader("stashing")
st.markdown("*[28]* ***stash: temporary saves the changes***")
st.code("git stash #save")
st.code("git stash apply #apply the saved changes")
st.code("git stash drop     # Discard saved changes")

st.subheader("working with remote repo")
st.markdown("*[29]* ***remote repo i.e. on server directory***")
st.code("git remote add #add a remote repository")
st.code("git remote remove #remove a remote repository")
st.code("git remote -v #list remote repositories")
st.code("git remote show #show info about remote repositories")

st.subheader("resolving conflict using meld")
st.markdown("*[30]* ***configure meldtool***")
st.code("git config --global merge.tool meld")
st.code("git mergetool #when conflict occurs open this interactive tool")

st.divider()

