FROM probablyfine/flume

RUN apt-get update -q
RUN apt-get install -y telnet
RUN apt-get install -y curl

ADD ./flume-http.conf /var/tmp/flume-http.conf
ADD ./flume-ng-mongodb-sink-1.0.0.jar /opt/flume/lib/.
ADD ./mongo-java-driver-2.13.0.jar /opt/flume/lib/.

EXPOSE 50004

ENTRYPOINT [ "flume-ng", "agent", "-c", "/opt/flume/conf", "-f", "/var/tmp/flume-http.conf", "-n", "a1", "-Dflume.root.logger=INFO,console" ]
