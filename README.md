# 安装flume zookeeper kafka python 环境 基于docker image

## 建立zgsystem的消息系统

### Apache Flume

  > 使用Apache Flume 作为消息收集的通道 ，为不同消息来源定义不同的message type ，如email ，sms ，applog等

  > 路由到不同的Sink 如Mongodb, Log File ,Apache Kafka etc..

  > 所有消息都默认sink为mongodb ，记录所有消息和日志信息

  > 目前使用Sink有，Mongodb ，Kafka ，Log

### Zookeeper

  > version : 3.4.6

### Apache Kafka

  > version : 2.9.1-0.8.2.2

  > 建立一个Zookeeper ，2个Kafka broker 结构的消息处理系统

  > 用Python实现Kafka Consumer ，处理email 和 sms Topic

### Python

  > 基于Python 2.7
