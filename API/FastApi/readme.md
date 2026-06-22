## Run a contianer

## Note :
-use 0Dockerfile for Simple pip to install packages.
-use 1Dockerfile when installation is complex, but this is lkarge image due to usage of windows image for installation..
-use 2Dockerfile uses multistage build of docker where 1.UV to install libararies and \
                                                       2.creating runtime with python and no UV \
(remember to rename to Dockerfile to actually work for building.docker uses file with the same name)\


## 1.Create an image
run this command to build the docker image  for the application along with its dependencies.
```
docker build -t my-api .
```
## 2.Run an image
run this command to run the docker container for the available image given
```
docker run -p 3000:3000 my-api
```
