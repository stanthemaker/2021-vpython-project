git reset HEAD^ --hard
git rebase "your new base"
cancel rebase: use git reflog to find the previous commit before the rebase,
git reset ....... --hard or  git reset ORIG_HEAD --hard