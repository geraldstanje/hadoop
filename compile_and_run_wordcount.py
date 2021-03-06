#!/usr/bin/python

import os

#
# test the wordcount example
#
os.system("echo 'start wordcount example...'")
os.system("sleep 2")

#
# delete in and out directory from hdfs
#
os.system("hdfs dfs -rm -r in")
os.system("hdfs dfs -rm -r out")

#
# create the in directory in the hdfs path
#
os.system("hdfs dfs -mkdir in")

#
# copy gutenberg text file to hadoop dir
#
os.system("unzip data/4300.zip -d data")
os.system("hdfs dfs -copyFromLocal data/4300.txt in") # copy file to the in directory, text file is from: http://www.gutenberg.org/files/4300/4300.zip

#
# compile WordCount.java with the javac compiler
#
os.system("mkdir src/wordcount_classes")
os.system("javac -classpath $HADOOP_HOME/libexec/share/hadoop/common/hadoop-common-2.3.0.jar:$HADOOP_HOME/libexec/share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.3.0.jar:$HADOOP_HOME/libexec/share/hadoop/common/lib/commons-cli-1.2.jar -d src/wordcount_classes src/WordCount.java")

#
# create a jar file
#
os.system("jar -cvf src/wordcount.jar -C src/wordcount_classes/ .")

#
# run the hadoop mapreduce job with wordcount.jar
#
os.system("hadoop jar src/wordcount.jar org/apache/hadoop/mapred/WordCount in out")

#
# print the mapreduce results, should show a table with word/counts
#
os.system("hdfs dfs -cat out/part-00000")

#
# open hadoop monitoring system
#
os.system("sleep 2")
os.system("open -a \"Google Chrome\" http://localhost:8088 http://localhost:50070")