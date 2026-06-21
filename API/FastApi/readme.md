##Run a contianer
##1.Create an image
run this command to build the docker image  for the application along with its dependencies.
'''
docker build -t my-api .
'''
##2.Run an image
run this command to run the docker container for the available image given
'''
docker run -p 3000:3000 my-api
'''
