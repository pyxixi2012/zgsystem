### git usage
```
$ git config --global credential.helper cache
# Set git to use the credential memory cache

$ git config --global credential.helper 'cache --timeout=3600'
# Set the cache to timeout after 1 hour (setting is in seconds)

# edit .git/config  change https to ssh
vi .git/config
url= git@github.com:username/projectname.git

$ git init

#make id_rsa.pub
$ cd ~/.ssh
cat id_rsa.pub ,add content to github SSH keys
```

### atom git usage
```
atom install git-plus package
press key "ctrl+shift+p" ,input  git commit all ,git commit and push
```

docker run -d \
-e MYID=1 \
-e SERVERS=192.168.1.208:2181 \
--name=zookeeper --net=host --restart=always mesoscloud/zookeeper:3.4.6-ubuntu-14.04
