## Run a contianer

## Note :
<pre style="line-height: .10; margin: 0; padding: 0;">
 • Use <b>0Dockerfile</b> for Simple pip to install packages.<br>
 • Use <b>1Dockerfile</b> when installation is complex, but this is large image due to usage of windows image for installation.<br>
 • Use <b>2Dockerfile</b> uses multistage build of docker where : <br>
                                                       1.UV to install libararies
                                                       2.creating runtime with python and no UV </pre> 
(remember to rename to Dockerfile to actually work for building.docker uses file with the same name)<br> 


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
