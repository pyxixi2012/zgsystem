### build zookeeper
  > $docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 jplock/zookeeper  
  > 注意： 需要修改防火墙，开放相关端口
### build apache kafka
  > pull kafak docker image from  docker hub digitalwonderland/kafka

  > $sudo docker run -d -e KAFKA_BROKER_ID=1 -e KAFKA_ADVERTISED_HOST_NAME=192.168.1.215 -e KAFKA_ZOOKEEPER_CONNECT=192.168.1.215 digitalwonderland/kafka
