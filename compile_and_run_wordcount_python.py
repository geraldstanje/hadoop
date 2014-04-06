#!/usr/bin/python

import os

#
# test hadoop mapreduce purchase example
# tutorial: http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
#
os.system("echo 'start wordcount python example...'")
os.system("sleep 2")

#
# delete directory in and output
#
os.system("hdfs dfs -rm -r in")
os.system("hdfs dfs -rm -r output")

#
# create the in directory in the hdfs path
#
os.system("hdfs dfs -mkdir in")

#
# copy gutenberg text file to hadoop dir
#
os.system("unzip data/4300.zip -d data")
os.system("hdfs dfs -copyFromLocal data/4300.txt in")
#
# run purchase example
#
os.system("hadoop jar $HADOOP_HOME/libexec/share/hadoop/tools/lib/hadoop-streaming-2.3.0.jar -file src/mapper_wordcount.py -mapper src/mapper_wordcount.py -file src/reducer_wordcount.py -reducer src/reducer_wordcount.py -input in -output output")

#
# print the mapreduce results, should show a table with word/counts
#
os.system("hdfs dfs -cat output/part-00000 | tail -10")

#
# open hadoop monitoring system
#
os.system("sleep 2")
os.system("open -a \"Google Chrome\" http://localhost:8088 http://localhost:50070")