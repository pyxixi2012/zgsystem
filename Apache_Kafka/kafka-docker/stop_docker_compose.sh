sudo docker-compose stop

sudo docker kill $(sudo docker ps -q) ; sudo docker rm $(sudo docker ps -a -q)

