https://docs.docker.com/get-started/part2/#apppy


Step one: build the image

   ~$ docker build -t tutorial-example .

   ensure that it is there

   ~$ docker image ls

Step two: run the container

   ~$ docker run -p 4000:80 tutorial-example

   then go to http://localhost:4000/
   You can also ping the service with curl

   ~$ curl http://localhost:4000

Step three: run the container in detached mode

   ~$ docker run -d -p 4000:80 tutorial-example

   then check its status

   ~$ docker container ls

   Then to stop the service use where you imput the container id from the previous command

   ~$ docker container stop [CONTAINER ID]
