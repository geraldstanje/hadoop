#!/usr/bin/python

import os

#
# test hadoop mapreduce purchase example
# tutorial: http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
#
os.system("echo 'start purchase example...'")
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
# copy purchases text file to hadoop dir
#
os.system("gzip -d -k data/purchases.txt.gz")
os.system("hdfs dfs -copyFromLocal data/purchases.txt in") # copy file to the in directory, text file is from: http://content.udacity-data.com/courses/ud617/purchases.txt.gz

#
# run purchase example
#
os.system("hadoop jar $HADOOP_HOME/libexec/share/hadoop/tools/lib/hadoop-streaming-2.3.0.jar -file src/mapper_purchases.py -mapper src/mapper_purchases.py -file src/reducer_purchases.py -reducer src/reducer_purchases.py -input in -output output")

#
# print the mapreduce results, should show a table with word/counts
#
os.system("hdfs dfs -cat output/part-00000 | tail -10")

#
# open hadoop monitoring system
#
os.system("sleep 2")
os.system("open -a \"Google Chrome\" http://localhost:8088 http://localhost:50070")