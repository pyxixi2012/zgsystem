# 安装flume zookeeper kafka python 环境 基于docker image

## 建立zgsystem的消息系统

## Docker Usage
### links :  
#### About Docker Command
  - Docker image and container via docker commands (search, pull, run, ps, restart, attach, and rm)
  http://www.bogotobogo.com/DevOps/Docker/Docker_Commands_for_Images_Container.php

  - More on Docker Run command
  http://www.bogotobogo.com/DevOps/Docker/Docker_Run_Command.php

  - Linking containers and volume for datastore
  http://www.bogotobogo.com/DevOps/Docker/Docker_Container_Linking_Connect_with_linking_system_Communication_across_links_Environment_variables.php

#### About Dockerfile
  - Dockerfiles : building Docker images automatically - FROM, MAINTAINER, and build context
  http://www.bogotobogo.com/DevOps/Docker/Docker_Dockerfile_to_build_images_automatically.php

  - Dockerfiles : building Docker images automatically II - revisiting FROM, MAINTAINER, build context, and caching
  http://www.bogotobogo.com/DevOps/Docker/Docker_Dockerfile_to_build_images_automatically_2.php

  - Dockerfiles : building Docker images automatically III - RUN
    http://www.bogotobogo.com/DevOps/Docker/Docker_Dockerfile_to_build_images_automatically_3.php

  - Dockerfile - Build Docker images automatically IV - CMD
    http://www.bogotobogo.com/DevOps/Docker/Docker_Dockerfile_to_build_images_automatically_4_CMD.php



## Apache Flume

  > 使用Apache Flume 作为消息收集的通道 ，为不同消息来源定义不同的message type ，如email ，sms ，applog等

  > 路由到不同的Sink 如Mongodb, Log File ,Apache Kafka etc..

  > 所有消息都默认sink为mongodb ，记录所有消息和日志信息

  > 目前使用Sink有，Mongodb ，Kafka ，Log

## Zookeeper

  > version : 3.4.6

## Apache Kafka

  > version : 2.9.1-0.8.2.2

  > 建立一个Zookeeper ，3个Kafka broker 结构的消息处理系统

  > 用Python实现Kafka Consumer ，处理email 和 sms Topic

## Python

  > 基于Python 2.7

## 注意事项
  > 需要修改防火墙，开放相关端口
