FROM probablyfine/flume

RUN apt-get update -q
RUN apt-get install -y telnet
RUN apt-get install -y curl
RUN mkdir /opt/flume/logs
RUN chown -R root:root /opt/flume

ADD ./flume-http.conf /opt/flume/conf/flume-http.conf
ADD ./flume-env.sh /opt/flume/conf/flume-env.sh
ADD ./log4j.properties /opt/flume/conf/log4j.properties
ADD ./lib/flume-ng-mongodb-sink-1.0.0.jar /opt/flume/lib/.
ADD ./lib/mongo-java-driver-2.13.0.jar /opt/flume/lib/.

VOLUME ["/opt/flume/logs"]
VOLUME ["/opt/flume/conf"]


EXPOSE 50004

ENTRYPOINT [ "flume-ng", "agent", "-c" ,"/opt/flume/conf","-f", "/opt/flume/conf/flume-http.conf", "-n", "a1"]
