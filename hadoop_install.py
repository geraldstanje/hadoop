#!/usr/bin/python

import os
import re
import sys
import commands

# run pi example
os.system("install hadoop...")
os.system("sleep 2")

# install hadoop using brew
os.system("brew install hadoop")

# set env vars for hadoop
array = []
env_vars_find = ["export JAVA_HOME", "export HADOOP_HOME", "export PATH=$PATH:$HADOOP_INSTALL/bin\n", "export PATH=$PATH:$HADOOP_INSTALL/sbin\n"]
env_vars_repl = ["export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0.jdk/Contents/Home\n", "export HADOOP_HOME=/usr/local/Cellar/hadoop/2.3.0\n", "export PATH=$PATH:$HADOOP_INSTALL/bin\n", "export PATH=$PATH:$HADOOP_INSTALL/sbin\n"]
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