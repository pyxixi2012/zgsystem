# 安装flume zookeeper  kafka python 环境 基于docker image

### 目录

* [1. install and config docker ](#1)

  * [1.1 check cent os 7 kernel version](#1.1)

  * [1.2 config docker env](#1.2)

  * [1.3 Starting and config the Docker daemon](#1.3)

* [2. create flume docker image ](#2)

* [3. create kafka docker image ](#3)

  * [3.1 install kafka without docker ](#3.1)

  * [3.2 install kafka with docker ](#3.2)
* [13. dockerfile for flume http agent ](#13)

* [14. config file for flume http agent ](#14)

<h2 id = "1"> 1. about docker </h2>

<h5 id = "1.1">1.1 check cent os 7 kernel version </h5>

1. check cent os 7 kernel version
> uname -r

2. upgrade cent os 7
> $sudo yum -r update

3. mondify net config (aliyun)
  > $sudo brctl addbr docker0

  > $sudo brctl addif docker0 eth0

  > $sudo ip link set dev docker0 up

  > $sudo ifconfig docker0 172.17.42.1

4. install docker

  > usefull link:

  > http://www.widuu.com/chinese_docker/docker-hub/builds.html

  > http://probablyfine.co.uk/2014/05/05/using-docker-with-apache-flume-1/

  Install with the script

  Log into your machine as a user with sudo or root privileges.

  Make sure your existing yum packages are up-to-date.

  > $ sudo yum update

  Run the Docker installation script.

  > $ curl -sSL https://get.docker.com/ | sh

  This script adds the docker.repo repository and installs Docker.

  Start the Docker daemon.

  > $ sudo service docker start

  Verify docker is installed correctly by running a test image in a container.

  > $ sudo docker run hello-world

  Display docker version

  > $ sudo docker version

  > Client:

  > Version:      1.9.1  
  > API version:  1.21  
  > Go version:   go1.4.2  
  > Git commit:   a34a1d5  
  > Built:        Fri Nov 20 13:25:01 UTC 2015  
  > OS/Arch:      linux/amd64  

  > Server:  
  >  Version:      1.9.1  
  > API version:  1.21  
  > Go version:   go1.4.2  
  > Git commit:   a34a1d5   
  > Built:        Fri Nov 20 13:25:01 UTC 2015  
  > OS/Arch:      linux/amd64

  Create a docker group

  To create the docker group and add your user:

  Log into Centos as a user with sudo privileges.

  Create the docker group and add your user.

  > $sudo usermod -aG docker yang

  Log out and log back in.

  This ensures your user is running with the correct permissions.

  Verify your work by running docker without sudo.

  > $ sudo docker run hello-world

  > $ sudo docker  pull centos

  > $sudo docker run -it centos /bin/bash

  Start the docker daemon at boot

  To ensure Docker starts when you boot your system, do the following:

  > $ sudo chkconfig docker on


5. uninstal docker

  You can uninstall the Docker software with yum.

  - List the package you have installed.

    > $ yum list installed | grep docker  

    >docker-engine.x86_64   1.7.1-1.el7 @/docker-engine-1.7.1-1.el7.x86_64.rpm

  - Remove the package.

    > $ sudo yum -y remove docker-engine.x86_64

    > This command does not remove images, containers, volumes, or user-created configuration files on your host.

  - To delete all images, containers, and volumes, run the following command:

    > $ rm -rf /var/lib/docker

    > Locate and delete any user-created configuration files.

[1.2]: #1.2

## 1.2 config docker env

1. 配置Docker开机自启动：
> $systemctl enable docker.service

  If you need to add an HTTP Proxy, set a different directory or partition for the Docker runtime files, or make other customizations, read our Systemd article to learn how to customize your Systemd Docker daemon options.
2. 卸载,使用yum卸载Docker。

  列出安装的软件包

  > $yum list installed | grep docker

  > $yum list installed | grep docker

  > docker-engine.x86_64             1.8.1-1.el7.centos             
  > dockerrepo docker-selinux.x86_64            1.7.1-108.el7.centos   

  移除软件包

  >$ sudo yum -y remove docker-engine.x86_64

  上面的命令不会删除镜像，容器，卷组和用户自配置文件。

  删除所有镜像，容器和卷组

  >$ rm -rf /var/lib/docker

  删除用户自配置文件


<h5 id = "1.3"> 1.3 Starting and config the Docker daemon </h5>

1. 当 Docker 安装完成之后，你需要启动 docker 进程。
>  $sudo systemctl start docker.service

2. 如果我们希望 Docker 默认开机启动，如下操作：
> $sudo chkconfig docker on

3. 现在，我们来验证 Docker 是否正常工作。第一步，我们需要下载最新的 centos 镜像。
> $sudo docker pull centos

4. 下一步，我们运行下边的命令来查看镜像，确认镜像是否存在：
> $ sudo docker images centos

<h2 id = '2'>2. create flume docker image </h2>

  ```
  usefull link :

  #Using Docker with Apache Flume - Part 1
  http://segmentfault.com/a/1190000000504942

  #config kafk sink with Zookeeper
  http://www.cloudera.com/content/www/en-us/documentation/kafka/latest/topics/kafka_flume.html
  ```

1. mkdir flume work dir
> $mkdir /data/work/app/docker/flume

2. create Dockerfile

  > FROM probablyfine/flume

  > ADD ./flume-http.conf /var/tmp/flume-http.conf

  > EXPOSE 50004

  > ENTRYPOINT [ "flume-ng", "agent", "-c", "/opt/flume/conf", "-f", "/var/tmp/flume-http.conf", "-n", "a1", "-Dflume.root.logger=INFO,console" ]
3. make flume-http.conf

  > $cp /home/yang/app/apache-flume-1.6.0-bin/conf/flume-http ./flume-http.conf

4. build docker-flume images

  > $sudo docker build -t zhiguoguo/flume-http .

5. display flume-http images

  > $docker images |grep flume-http

  > zhiguoguo/flume-http     latest              d14cf0b3723b        6 minutes ago       418.9 MB

  > probablyfine/flume       latest              030613242e61        3 months ago        418.9 MB

6. push flume-http to private repository
  > mark

7. run flume-http image
  > $sudo docker run -p 444:50004 -t zhiguoguo/flume-http  
  > Q&A :  not yet config mongodb and kafka sink ,so run with error

8. view container running logs
  > $sudo docker ps|grep flume-http  
  > $sudo docker logs  be7a4c50e159

9. stop running container
  > $ sudo docker stop

10. remove images
  > $ docker rm test_sshd  
  > $ docker rmi eg_sshd

<h2 id = "3">3. create kafka docker image </h2>

<h5 id = "3.1">3.1 install kafka without docker </h5>

  1). start zookeeper server at localhost  
  > $zookeeper-3.4.6/bin/zkServer.sh start

  2). start kafka broker 1  
  >$bin/kafka-server-start.sh config/server.properties     

  3). create a topic 'email'  
  > $bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic email   

  4). list all kafka topic
  > $bin/kafka-topics.sh --list --zookeeper localhost:2181

  5). view topic's properties   
  > $ bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic email

  6). begin test kafka cluster broker  ,producers and consumer

  Created topic "email", "sms".  
  > $ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic email

  > $ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sms

  view all created topics
  > $ bin/kafka-topics.sh --list --zookeeper localhost:2181  
      sms  
      email  
      test  

  view email topics properties
  > $ bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic email  
  Topic:email  PartitionCount:1    ReplicationFactor:1 Configs:  
      Topic: email Partition: 0    Leader: 0   Replicas: 0 Isr: 0  

  producer connect Kafka Broker  to send a test messages
  > $bin/kafka-console-producer.sh --broker-list 192.168.1.215:9092 --topic email
      SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".  
      SLF4J: Defaulting to no-operation (NOP) logger implementation  
      SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.  
      Hello World  

  consumer connect Zookeeper to get messages
  > $bin/kafka-console-consumer.sh --zookeeper 192.168.1.215:2181 --topic email --from-beginning  

      SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".  
      SLF4J: Defaulting to no-operation (NOP) logger implementation  
      SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.  
      Hello World

  delete all message in a topic in a kafka cluster env

  > Tested in Kafka 0.8.2, for the quick-start example: First, Add one line to server.properties file under config folder:

  >> delete.topic.enable=true
  then, you can run this command:

  > bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic test

<h5 id = '3.2'>3.2 install kafka with docker </h5>

```
usefull link:

#
http://blog.jaceklaskowski.pl/2015/07/14/apache-kafka-on-docker.html?mkt_tok=3RkMMJWWfF9wsRonuqTMZKXonjHpfsX57ukoWaC0lMI%2F0ER3fOvrPUfGjI4ATctmI%2BSLDwEYGJlv6SgFQ7LMMaZq1rgMXBk%3D

```



<h2 id = '13'>13. dockerfile for flume http agent</h2>

      FROM probablyfine/flume

      RUN apt-get update -q
      RUN apt-get install -y telnet
      RUN apt-get install -y curl

      ADD ./flume-http.conf /var/tmp/flume-http.conf
      ADD ./flume-ng-mongodb-sink-1.0.0.jar /opt/flume/lib/.
      ADD ./mongo-java-driver-2.13.0.jar /opt/flume/lib/.

      EXPOSE 50004

      ENTRYPOINT [ "flume-ng", "agent", "-c", "/opt/flume/conf", "-f", "/var/tmp/flume-http.conf", "-n", "a1", "-Dflume.root.logger=INFO,console" ]

<h2 id = '14'>14. config file for flume http agent </h2>

```
a1.sources = r1
a1.sinks = k1 k2 k3
a1.channels = c1 c2 c3

#Describe/configure the source
a1.sources.r1.type= http
a1.sources.r1.host = 0.0.0.0
a1.sources.r1.port= 50004
a1.sources.r1.channels= c1 c2 c3
#alex
a1.sources.r1.selector.type = multiplexing
a1.sources.r1.selector.header = type
#映射允许每个值通道可以重叠。默认值可以包含任意数量的通道。
a1.sources.r1.selector.mapping.applog = c1
a1.sources.r1.selector.mapping.sms = c2
a1.sources.r1.selector.mapping.email = c3
a1.sources.r1.selector.default = c1

#Describe the mongodb sink 1
a1.sinks.k1.type = org.riderzen.flume.sink.MongoSink
a1.sinks.k1.host = 192.168.1.215
a1.sinks.k1.port = 50000
a1.sinks.k1.model = single
a1.sinks.k1.db = logdb
a1.sinks.k1.collection = logtable
a1.sinks.k1.batch = 100
a1.sinks.k1.channel = c1

#sink for kafka sms consumer
a1.sinks.k2.type = org.apache.flume.sink.kafka.KafkaSink
a1.sinks.k2.topic = sms
a1.sinks.k2.brokerList = 192.168.1.215:9092
a1.sinks.k2.requiredAcks = 1
a1.sinks.k2.batchSize = 20
a1.sinks.k2.channel = c2

#sink for kafka email consumer
a1.sinks.k3.type = org.apache.flume.sink.kafka.KafkaSink
a1.sinks.k3.topic = email
#config kafka sink to kafka broker directly
a1.sinks.k3.brokerList = 192.168.1.215:9092
#config kafka sink to zookeeper cluster
a1.sinks.k3.zookeeperConnect = 192.168.1.215:2181
a1.sinks.k3.requiredAcks = 1
a1.sinks.k3.batchSize = 20
a1.sinks.k3.channel = c3

#Describe the mongodb sink 2
#a1.sinks.k2.type = org.riderzen.flume.sink.MongoSink
#a1.sinks.k2.host = 192.168.1.215
#a1.sinks.k2.port = 50000
#a1.sinks.k2.model = single
#a1.sinks.k2.db = logdb
#a1.sinks.k2.collection = logtable_1
#a1.sinks.k2.batch = 100
#a1.sinks.k2.channel = c2
##Use a channel which buffers events in memory
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
a1.channels.c2.type = memory
a1.channels.c2.capacity = 1000
a1.channels.c2.transactionCapacity = 100
a1.channels.c3.type = memory
a1.channels.c3.capacity = 1000
a1.channels.c3.transactionCapacity = 100

#a1.sinks.k2.type = file_roll
#a1.sinks.k2.sink.directory = /data/work/app/logprog/logs
#a1.sinks.k2.type = logger
#a1.sinks.k2.channel = c2
```
