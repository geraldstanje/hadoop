#!/usr/bin/python

import os

#
# test hadoop mapreduce pi example
#
os.system("echo 'start pi example...'")
os.system("sleep 2")

#
# run pi example
#
os.system("hadoop jar $HADOOP_HOME/libexec/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.3.0.jar pi 10 100")

#
# open hadoop monitoring system
#
os.system("sleep 2")
os.system("open -a \"Google Chrome\" http://localhost:8088 http://localhost:50070")