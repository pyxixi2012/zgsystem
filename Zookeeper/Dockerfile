# Dockerfile for ZooKeeper
FROM quay.io/signalfuse/maestro-base:alp-3.2-jdk7
MAINTAINER Maxime Petazzoni <max@signalfx.com>
# Get latest stable release of ZooKeeper
ADD zookeeper-3.4.6 /opt/zookeeper-3.4.6
ADD run.py /opt/zookeeper-3.4.6/.docker/
ADD libnss_files.so.2 /opt/libnss_files.so.2
RUN cp /etc/hosts /tmp/hosts
RUN mkdir -p -- /lib-override && cp /opt/libnss_files.so.2 /lib-override
RUN sed -i 's:/etc/hosts:/tmp/hosts:g' /lib-override/libnss_files.so.2
ENV LD_LIBRARY_PATH /lib-override
RUN echo 192.168.1.215 zk-node-0 >> /tmp/hosts
RUN echo 192.168.1.208 zk-node-1 >> /tmp/hosts
RUN echo 192.168.1.138 zk-node-2 >> /tmp/hosts
RUN cat /tmp/hosts
WORKDIR /opt/zookeeper-3.4.6/
CMD ["python", "/opt/zookeeper-3.4.6/.docker/run.py"]
