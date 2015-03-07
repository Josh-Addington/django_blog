git add -A
read -p "Commit Description: " desc
git commit -m "$desc"
git push origin staging
git push staging master
