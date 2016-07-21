
## build single zookeeper node and 3 kafka broker use wurstmeister/kafka

## compose to run all CONTAINER
  > edit /etc/hosts add zkserver1 to hosts in all zookeeper node,

  > $sudo vi /etc/hosts

  > 192.168.1.215   zkserver1

  > $sudo docker-compose up

  > or

  > $sudo docker-compose up -d

## scale kafka node
  > $sudo docker-compose scale kafka=1

## add a broker manual
  > $sudo docker run -d -e KAFKA_BROKER_ID=3 -e KAFKA_ADVERTISED_HOST_NAME=192.168.1.215 -e KAFKA_ZOOKEEPER_CONNECT=192.168.1.215:2181 -p 9092:9092 wurstmeister/kafka:0.8.2.0

  > $sudo docker run -e KAFKA_BROKER_ID=3 -e KAFKA_ADVERTISED_HOST_NAME=192.168.1.215 -e KAFKA_ZOOKEEPER_CONNECT=192.168.1.215:2181 -p 9092:9092 wurstmeister/kafka:0.8.2.0

## create a topic with 3 replication and 1 partition
  > $bin/kafka-topics.sh --create --zookeeper zkserver1:2181 --replication-factor 3 --partition 1 --topic  zgg.email

## to get a list of topics
  > $bin/kafka-topics.sh --list --zookeeper zkserver1:2181

## view topic's properties   
  > $bin/kafka-topics.sh --describe --zookeeper zkserver1:2181 --topic zgg.email

## Starting a producer - sending messages
  > $bin/kafka-console-producer.sh --broker-list zkserver1:11002 zkserver1:11003 zkserver1:11004 --topic zgg.email

## Starting a consumer - consuming messages
  > $bin/kafka-console-consumer.sh --zookeeper zkserver1:2181 --from-beginning --topic zgg.email
