## 安装Flume docker image

Starting the Docker daemon  
当 Docker 安装完成之后，你需要启动 docker 进程。  

  > $ sudo service docker start  
如果我们希望 Docker 默认开机启动，如下操作：  

  > $ sudo chkconfig docker on  
现在，我们来验证 Docker 是否正常工作。第一步，我们需要下载最新的 centos 镜像。  

  > $ sudo docker pull hello-world  

下一步，我们运行下边的命令来查看镜像，确认镜像是否存在：  

  > $ sudo docker images hello-world  

### pull flume image and build new image   
1.pull flume image from docker hub  
  > $ sudo docker pull probablyfine/flume  

2.edit flume conf   
  > view flume-http.conf  
  

3.build new flume image from Dockerfile  
  > $ cd /data/work/app/docker/flume  
  > $ sudo docker build -t zhiguoguo/flume-http .  

3.check builded flume image   
  > $ sudo docker images|grep flume-http  

4.
