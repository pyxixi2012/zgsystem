sudo docker kill $(sudo docker ps -q) ; sudo docker rm $(sudo docker ps -a -q)

sudo docker-compose up -d
