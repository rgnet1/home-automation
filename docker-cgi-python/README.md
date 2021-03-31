# tidal-dl Docker Wrapper

This is a simple python web server that allows you to run tidal-dl from a web
page.  

## How to use

```bash
# build image
docker build -t rgnet1/tidal-dl .
# run image
docker run -p 8885:80 --name tidal-dl -d rgnet1/tidal-dl
```

## First time use
First time use requires you to enter the container, and link tidal to your account:

```bash
docker exec -it  /bin/bash

```

You can Access from the below URL after run docker container.  

* http://localhost:8885](http://localhost:8885)


### References

* [Usage of docker with apache2 and python](https://github.com/pyohei/docker-cgi-python)
* [Tidal-dl] (https://github.com/yaronzz/Tidal-Media-Downloader)
