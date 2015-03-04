git add -A
read -p "Commit Description: " desc
git commit -m "$desc"
git push origin master
git push live master
