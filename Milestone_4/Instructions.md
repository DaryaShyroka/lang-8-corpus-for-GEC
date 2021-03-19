### How to get things working

- start Docker app

- Navigate to src directory

1. Build the Docker image for our web application using the command, replacing <image_name> with the name you choose to give our Docker image:

```  docker build -t <image_name> .```

Make sure the docker image has been successfully created by running `docker images` and checking the `<image_name>` is in that list, and has been recently created.

2. Create a Docker container by running the Docker image with internal and external ports both 9999:

`docker run -p 9999:9999 <image_name>`

3. When inside the container, 

4. 
