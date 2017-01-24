#!/bin/bash
python3 athena.py

echo "commiting.."
git add -A
git commit -m 'Update and Build'



echo "deploying.."
git push origin master

