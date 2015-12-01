# install multi node zookeeper cluster
## pull zookeeper docker image from docker-hub using dao pull mesoscloud/zookeeper
```
#delete all container
sudo docker kill $(sudo docker ps -q) ; sudo docker rm $(sudo docker ps -a -q)

#delete all images
docker kill $(docker ps -q) ; docker rm $(docker ps -a -q) ; docker rmi $(docker images -q -a)
```

```
cluster 环境 ，有待测试

sudo docker run -d \
-e MYID=1 \
-e SERVERS=brand-server-215,brand-server-215,brand-server-215 \
--name=zookeeper --net=host --restart=always mesoscloud/zookeeper:3.4.6-centos-7
```
```
# 单点的zookeeper环境，测试可以用
docker hub image url : https://hub.docker.com/r/jplock/zookeeper/

sudo docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 jplock/zookeeper

# 查看zookeeper 运行日志
sudo docker logs -f 870acbb99046b656bdec2da9e8274c2557f419f8b1ba6a5068abdfdb1846dd30

```
