# get the files
git clone https://github.com/eliabruni/hadoop-tutorial

cd word-count
mkdir out

# run it locally
cat mobydick.txt | ./mapper.py | ./reducer.py | sort -nrk 2 > out/mobydick_count_local.txt

# put the data in hdfs
hadoop fs -mkdir count_example
hadoop fs -put mobydick.txt count_example

# run it on hadoop
hadoop jar $HADOOP_HOME/hadoop-streaming.jar $PARAMS -mapper mapper.py -reducer reducer.py -input count_example/mobydick.txt -output count_example/hamlet_out -file mapper.py -file reducer.py 

# view the output 
mkdir out
hadoop fs -ls count_example/hamlet_out/
hadoop fs -cat count_example/hamlet_out/part-* | sort -nrk 2 > out/mobydick_count.txt
head | out/mobydick_count.txt

# test that hadoop worked
diff  out/mobydick_count.txt out/mobydick_count_local.txt

# cleanup
hadoop fs -rmr count_example


