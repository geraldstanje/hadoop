#!/usr/bin/python

import os

#
# test the wordcount example
#
os.system("echo 'start wordcount example...'")
os.system("sleep 2")

#
# delete files in directory in
#
os.system("hdfs dfs -rm -r in")

#
# create the in directory in the hdfs path
#
os.system("hdfs dfs -mkdir in")

#
# download words file and unzip it
#
os.system("wget http://www.gutenberg.org/files/4300/4300.zip")
os.system("unzip 4300.zip")
os.system("rm 4300.zip")
os.system("hdfs dfs -copyFromLocal /Users/geraldstanje/Downloads/4300.txt in") # copy file to the in directory

#
# compile WordCount.java with the javac compiler
#
os.system("javac -classpath $HADOOP_HOME/libexec/share/hadoop/common/hadoop-common-2.3.0.jar:$HADOOP_HOME/libexec/share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.3.0.jar:$HADOOP_HOME/libexec/share/hadoop/common/lib/commons-cli-1.2.jar -d wordcount_classes WordCount.java")

#
# create a jar file
#
os.system("jar -cvf wordcount.jar -C wordcount_classes/ .")

#
# delete all files in output dir
#
os.system("hdfs dfs -rm -r output")

#
# run the hadoop mapreduce job with wordcount.jar
#
os.system("hadoop jar wordcount.jar org/apache/hadoop/mapred/WordCount in output")

#
# print the mapreduce results, should show a table with word/counts
#
os.system("hdfs dfs -cat output/part-00000")

#
# open hadoop monitoring system
#
os.system("sleep 2")
os.system("open -a \"Google Chrome\" http://localhost:8088 http://localhost:50070")