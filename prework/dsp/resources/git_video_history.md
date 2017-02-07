###List of Commands Used in Video

```bash
# print present working directory
pwd
/Users/reshamashaikh/ds/metis/metisgh
# create new directory
mkdir prework
# list files
ls
# change directory, go into prework directory
cd prework
# clone the repo
git clone https://github.com/reshama/dsp.git
ls
# change directory, go into dsp
cd dsp
ls
# see what the remotes are
git remote -v
# use editor to view and edit file
emacs 00-fork_repo.md

# check if any changes have been made to local repo; changed files will be in red
git status
# add a file, also means 'staging file'
git add 00-fork_repo.md
# check that file is staged, staged file will be in green
git status
# commit a file; adding message to commit to track changes made
git commit -m 'added emoji'
# check that file has been committed
git status
# push file to forked repo
git push

# clear screen
clear
ls

# open up file and see if any changes have been made to file
emacs 00-fork_repo.md

# check remotes
git remote -v
# pull updates from forked repo on broswer
git pull
ls
# check file and see that the updated changes from browser file are now in local file
emacs 00-fork_repo.md

# clear screen
clear
# print history of commands used
history
  
  
  
