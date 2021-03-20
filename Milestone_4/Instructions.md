### How to get things working

1. Start the Docker app on your computer.

2. Build the Docker image for our web application using the command below, replacing `<image_name>` with the name you choose to give our Docker image (don't forget the '.' at the end!):

```  docker build -t <image_name> .```

Make sure the docker image has been successfully created by running `docker images` and checking the `<image_name>` is in that list, and has been recently created. It should look like this:

``` 
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
lang8_image         latest              b849065aed5a        About an hour ago   1.25GB
```

3. Create a Docker container by running the Docker image with internal and external ports both 9999:

`docker run -p 9999:9999 <image_name>`

The output you see should look like:

``` 
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9999 (Press CTRL+C to quit)
```

4. Open your brower and type `localhost:9999` in the URL. 

5. You should see our interface displayed in the window.

