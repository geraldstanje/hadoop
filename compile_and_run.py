#!/usr/bin/python

#
# IMPORTANT: Make sure that you turn on Remote Login under System Preferences then File Sharing
#

import os

# run pi example
os.system("echo 'start pi example...'")
os.system("sleep 2")

# run pi example
os.system("hadoop jar $HADOOP_HOME/libexec/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.3.0.jar pi 10 100")


os.system("sleep 2")


# run wordcount example
os.system("echo 'start wordcount example...'")
os.system("sleep 2")

# delete files in in dir
os.system("hdfs dfs -rm -r in")
# create in dir in hdfs
os.system("hdfs dfs -mkdir in")

# download file and unzip it
os.system("wget http://www.gutenberg.org/files/4300/4300.zip")
os.system("unzip 4300.zip")
os.system("rm 4300.zip")
# copy file to in directory
os.system("hdfs dfs -copyFromLocal /Users/geraldstanje/Downloads/4300.txt in")

# compile java
os.system("javac -classpath $HADOOP_HOME/libexec/share/hadoop/common/hadoop-common-2.3.0.jar:$HADOOP_HOME/libexec/share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.3.0.jar:$HADOOP_HOME/libexec/share/hadoop/common/lib/commons-cli-1.2.jar -d wordcount_classes WordCount.java")

# create jar
os.system("jar -cvf wordcount.jar -C wordcount_classes/ .")

# delete files in output dir
os.system("hdfs dfs -rm -r output")

# run hadoop with wordcount.jar
os.system("hadoop jar wordcount.jar org/apache/hadoop/mapred/WordCount in output")

# mapreduce results
os.system("hdfs dfs -cat output/part-00000")


os.system("sleep 2")


os.system("open -a \"Google Chrome\" http://localhost:8088 http://localhost:50070")
