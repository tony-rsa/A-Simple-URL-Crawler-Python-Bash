git add --all
echo -en "Commit Msg: " && read CMTMSG

git commit -m "$CMTMSG"
git push
