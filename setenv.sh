#!/bin/bash

# environment variables
echo "Setting environment variables ..."
export MY_GIT_ROOT="$(pwd)"

echo "Setting aliases ..."
# set bash aliases
alias g='git'
alias la='ls -a'
alias ll='ls -l'
alias test="python3 $MY_GIT_ROOT/tools/test.py"

echo "Configure git ..."
# set git config
git config --global push.default simple
git config --global alias.hist "log --graph --oneline --decorate"
git config --global alias.p push
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ft fetch
git config --global alias.rb rebase
git config --global alias.ll "log --decorate --oneline --graph --date=relative --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'"
git config --global alias.mt mergetool
git config --global alias.cp cherry-pick
git config --global alias.dt difftool
