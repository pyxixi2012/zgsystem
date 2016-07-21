### build zookeeper
  > $docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 jplock/zookeeper  
  > 注意： 需要修改防火墙，开放相关端口
### build apache kafka
  > pull kafak docker image from  docker hub digitalwonderland/kafka

  > $sudo docker run -d -e KAFKA_BROKER_ID=1 -e KAFKA_ADVERTISED_HOST_NAME=192.168.1.215 -e KAFKA_ZOOKEEPER_CONNECT=192.168.1.215 digitalwonderland/kafka

### test realmsg topic
  > create realmsg topic with 1 partition and 1 replication
  ```
  $bin/kafka-topics.sh --create --zookeeper 192.168.1.215:2181,192.168.1.208:2181,192.168.1.138:2181 --replication-factor 1 --partition 1 --topic  realmsg
  ```
  > list all exists topics
  ```
  $bin/kafka-topics.sh --list --zookeeper 192.168.1.215:2181 --replication-factor 1 --partition 1 --topic realmsg
  ```
  > view realmsg topic info
  ```
  $bin/kafka-topics.sh --describe --zookeeper 192.168.1.215:2181 --topic realmsg
  ```
  > create a consumer to test realmsg msg
  ```
  $bin/kafka-console-consumer.sh --zookeeper 192.168.1.215:2181 --from-beginning --topic realmsg
  ```
  > create a providor to test realmsg
  ```
  $bin/kafka-console-producer.sh --broker-list 192.168.1.215:11002 192.168.1.215:11003 --topic realmsg
  ```
