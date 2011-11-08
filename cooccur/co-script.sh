# get the files
git clone https://github.com/eliabruni/hadoop-tutorial

# enter cooccur and create out dir
cd cooccur
mkdir out

# run it locally
cat mobydick.txt | ./mapper.py | sort | ./reducer.py > out/mobydick_cooccur_local.txt
head | out/mobydick_cooccur_local.txt

# put the data in hdfs
hadoop fs -mkdir cooccur_example
hadoop fs -put mobydick.txt cooccur_example

# run it on hadoop
hadoop jar $HADOOP_HOME/hadoop-streaming.jar $PARAMS -mapper mapper.py -reducer reducer.py -input cooccur_example/mobydick.txt -output cooccur_example/mobydick_out -file mapper.py -file reducer.py 

# view the output 
mkdir out
hadoop fs -ls cooccur_example/mobydick_out/
hadoop fs -cat cooccur_example/mobydick_out/part-*  > out/mobydick_cooccur.txt
head | out/mobydick_cooccur.txt

# test that hadoop worked
diff  out/mobydick_cooccur.txt out/mobydick_cooccur_local.txt

# cleanup
hadoop fs -rmr cooccur_example


