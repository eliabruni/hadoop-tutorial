# make a new directory
mkdir count_example
cd count_example

# get the files
git clone https://github.com/eliabruni/hadoop-tutorial

# run it locally
cat mobydick.txt | ./mapper.py | ./reducer.py | sort -k 2 -r -n | head
cat mobydick.txt | ./mapper.py | sort | ./reducer.py | sort -k 2 -r -n | head


