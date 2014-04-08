#!/bin/sh

HDFS_PATH=/Users/geraldstanje/Documents/ # existing path
HDFS_DIR=hdfstmp # creates a new directory called $HDFS_DIR

echo "Install hadoop..."
echo "System sleep 2"

echo `brew install hadoop`
HADOOP=/usr/local/Cellar/hadoop/
HADOOP_VERSION=`ls $HADOOP`

sh -c export HADOOP_HOME=$HADOOP$HADOOP_VERSION
sh -c export JAVA_HOME=`/usr/libexec/java_home`

######TODO look for & replace vars in .profile
#sh -c 'echo export JAVA_HOME=$HADOOP_HOME >> ~/.profile'
#sh -c 'echo export HADOOP_HOME=$HADOOP_HOME >> ~/.profile'

#
# create hdfs dir
#
mkdir -p  $HDFS_PATH$HDFS_DIR

#
# copy the property files (stored in config) to /usr/local/Cellar/hadoop/2.3.0/libexec/etc/hadoop
#
cp ./config/core-site.xml $HADOOP_HOME/libexec/etc/hadoop/core-site.xml # copy core-site.xml from config folder to hadoop path
cp ./config/yarn-site.xml $HADOOP_HOME/libexec/etc/hadoop/yarn-site.xml # copy yarn-site.xml from config folder to hadoop path
cp ./config/mapred-site.xml $HADOOP_HOME/libexec/etc/hadoop/mapred-site.xml # copy mapred-site.xml from config folder to hadoop path
cp ./config/hdfs-site.xml $HADOOP_HOME/libexec/etc/hadoop/hdfs-site.xml # copy hdfs-site.xml from config folder to hadoop path

#
# modify the namenode and data node path in the hdfs-site.xml file
#
search="/Users/geraldstanje/Documents/hdfstmp"
replace=$HDFS_PATH$HDFS_DIR
file=$HADOOP_HOME/libexec/etc/hadoop/hdfs-site.xml
file_rpl="tmp.xml"

declare -a myarray

# Load file into array
let i=0
while IFS=$'\n' read -r line_data; do

    var="${line_data}"
    var=${var//"$search"/$replace}
    myarray[i]="${var}"
	((++i))
done < "$file"

# Write changes to file
rm "$file_rpl"
let i=0
while (( ${#myarray[@]} > i )); do

    echo "${myarray[i]}" >> "$file_rpl"
    ((++i))
done

mv tmp.xml $HADOOP_HOME/libexec/etc/hadoop/hdfs-site.xml

#
# create two directories which will contain the namenode and the datanode for this hadoop installation
#
mkdir -p $HDFS_PATH$HDFS_DIR/namenode
mkdir -p $HDFS_PATH$HDFS_DIR/datanode

#
# format the new hadoop filesystem
#
hdfs namenode -format

#
# start hadoop service
#
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

#
# show functional instance of Hadoop running on your VPS
#
jps
#If everything is sucessful, you should see following services running
#2583 DataNode
#2970 ResourceManager
#3461 Jps
#3177 NodeManager
#2361 NameNode
#2840 SecondaryNameNode
