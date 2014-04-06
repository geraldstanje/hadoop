#!/usr/bin/python

#
# this is a hadoop 2.3.0 install script for mac osx
# make sure that brew installs hadoop 2.3.0
# i use java version: 1.8.0
# IMPORTANT: Make sure that you turn on remote login under system preferences then file sharing
#

import os
import re
import sys
import commands

hdfs_path = "/Users/geraldstanje/Documents/" # dont forget the / at the end
hdfs_dir = "hdfstmp"

#
# install hadoop
#
os.system("install hadoop...")
os.system("sleep 2")

# install hadoop using brew
os.system("brew install hadoop")

#
# set env vars for hadoop
#
array = []
env_vars_find = ["export JAVA_HOME", "export HADOOP_HOME", "export PATH=$PATH:$HADOOP_HOME/bin\n", "export PATH=$PATH:$HADOOP_HOME/sbin\n"]
env_vars_repl = ["export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0.jdk/Contents/Home\n", "export HADOOP_HOME=/usr/local/Cellar/hadoop/2.3.0\n", "export PATH=$PATH:$HADOOP_HOME/bin\n", "export PATH=$PATH:$HADOOP_INSTALL/sbin\n"]
env_vars_found = [0, 0, 0, 0]

status, home_dir = commands.getstatusoutput("echo ~")

# read env vars
with open(home_dir + "/.profile", "r") as f:
    for line in f:
        count = 0
        env_var_lookup = 0
        
        for env in env_vars_find:
            found = line.find(env)
            
            if found != -1:
                env_vars_found[count] = 1
                env_var_lookup = 1
                array.append(env_vars_repl[count])
            
            count = count + 1
        
        if env_var_lookup == 0:
            array.append(line)
            
    f.close()

# write env vars and replace hadoop paths
fh = open(home_dir + "/.profile","w")   
for item in array:
    fh.write(item)

count = 0
for env in env_vars_found:
    if env == 0:
        fh.write(env_vars_repl[count])
    count = count + 1

fh.close()

# refresh env vars in current shell
os.system("source " + home_dir + "/.profile")

#
# create hdfs dir
#
os.system("mkdir -p" + hdfs_path + hdfs_dir)

#
# copy the property files (stored in config) to /usr/local/Cellar/hadoop/2.3.0/libexec/etc/hadoop
#
os.system("cp ./config/core-site.xml $HADOOP_HOME/libexec/etc/hadoop") # copy core-site.xml from config folder to hadoop path
os.system("cp ./config/yarn-site.xml $HADOOP_HOME/libexec/etc/hadoop") # copy yarn-site.xml from config folder to hadoop path
os.system("cp ./config/mapred-site.xml $HADOOP_HOME/libexec/etc/hadoop") # copy mapred-site.xml from config folder to hadoop path
os.system("cp ./config/hdfs-site.xml $HADOOP_HOME/libexec/etc/hadoop") # copy hdfs-site.xml from config folder to hadoop path

#
# create two directories which will contain the namenode and the datanode for this hadoop installation
#
os.system("mkdir -p " + hdfs_path + hdfs_dir + "/namenode")
os.system("mkdir -p " + hdfs_path + hdfs_dir + "/datanode")

#
# format the new hadoop filesystem
#
os.system("hdfs namenode -format")

#
# start hadoop
#
os.system("$HADOOP_HOME/sbin/start-dfs.sh")

#
# show functional instance of Hadoop running on your VPS
#
os.system("jps")