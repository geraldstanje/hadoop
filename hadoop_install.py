#!/usr/bin/python

#
# this is a hadoop 2.3.0 install script for mac osx
# make sure that brew installs hadoop 2.3.0
# i use java version: 1.8.0
# IMPORTANT: Make sure that you turn on remote login under system preferences then file sharing
# tutorial: http://www.linkedin.com/groups/How-learn-hadoop-762547.S.5845829474339282945?qid=cd795b39-0ceb-4083-a525-6992bf49f89b&trk=groups_guest_most_popular-0-b-cmr&goback=.gmp_762547
#

import os
import re
import sys
import commands
    
hdfs_path = "/Users/geraldstanje/Documents/" # dont forget the / at the end
hdfs_dir = "hdfstmp"
hadoop_version = "2.3.0" # TODO: we should extract that somehow from brew install...

#
# install hadoop
#
os.system("install hadoop...")
os.system("sleep 2")

#
# install hadoop using brew
#
os.system("brew install hadoop")

#
# set env vars for hadoop
#
hadoop_env_set = 0
status, home_dir = commands.getstatusoutput("echo ~")

# read env vars
fh = open(home_dir + "/.profile","r")
for line in fh:
    found = line.find("HADOOP_HOME")
        
    if found != -1:
        hadoop_env_set = 1
            
fh.close()

# set env_variables array
env_variables = [["JAVA_HOME", "/Library/Java/JavaVirtualMachines/jdk1.8.0.jdk/Contents/Home"],
                 ["HADOOP_HOME", "/usr/local/Cellar/hadoop/" + hadoop_version]
                ]

#
# write env vars and replace hadoop paths
#
if hadoop_env_set == 0:
    fh = open(home_dir + "/.profile","a")    
    for env in env_variables:
        fh.write("export " + env[0] + "=" + env[1] + "\n")
        print 'export %s="%s"' % (env[0], env[1])
    fh.close()

#
# create hdfs dir
#
os.system("mkdir -p" + hdfs_path + hdfs_dir)

#
# copy the property files (stored in config) to /usr/local/Cellar/hadoop/2.3.0/libexec/etc/hadoop
#
HADOOP_HOME_DIR = "/usr/local/Cellar/hadoop/" + hadoop_version
os.system("cp ./config/core-site.xml " + HADOOP_HOME_DIR + "/libexec/etc/hadoop") # copy core-site.xml from config folder to hadoop path
os.system("cp ./config/yarn-site.xml " + HADOOP_HOME_DIR + "/libexec/etc/hadoop") # copy yarn-site.xml from config folder to hadoop path
os.system("cp ./config/mapred-site.xml " + HADOOP_HOME_DIR + "/libexec/etc/hadoop") # copy mapred-site.xml from config folder to hadoop path
os.system("cp ./config/hdfs-site.xml " + HADOOP_HOME_DIR + "/libexec/etc/hadoop") # copy hdfs-site.xml from config folder to hadoop path

#
# modify the namenode and data node path in the hdfs-site.xml file
#
array = []
fh = open(HADOOP_HOME_DIR + "/libexec/etc/hadoop/hdfs-site.xml","r")
for line in fh:
    found1 = line.find("<value>file:/Users/geraldstanje/Documents/hdfstmp/namenode</value>")
    found2 = line.find("<value>file:/Users/geraldstanje/Documents/hdfstmp/datanode</value>")
    
    if found1 != -1:
        array.append("\t\t<value>file:" + hdfs_path + hdfs_dir + "/nnamenode</value>" + "\n")
    elif found2 != -1:
        array.append("\t\t<value>file:" + hdfs_path + hdfs_dir + "/ddatanode</value>" + "\n")
    else:
        array.append(line)    
fh.close()

fh = open(HADOOP_HOME_DIR + "/libexec/etc/hadoop/hdfs-site.xml","w")    
for line in array:
    fh.write(line)
fh.close()

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
# start hadoop service
#
os.system("$HADOOP_HOME/sbin/start-dfs.sh")
os.system("$HADOOP_HOME/sbin/start-yarn.sh")

#
# show functional instance of Hadoop running on your VPS
#
os.system("jps")
#If everything is sucessful, you should see following services running
#2583 DataNode
#2970 ResourceManager
#3461 Jps
#3177 NodeManager
#2361 NameNode
#2840 SecondaryNameNode