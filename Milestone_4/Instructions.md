### How to get things working

1. Start the Docker app on your computer.

2. Build the Docker image for our web application using the command below, replacing <image_name> with the name you choose to give our Docker image:

```  docker build -t <image_name> .```

Make sure the docker image has been successfully created by running `docker images` and checking the `<image_name>` is in that list, and has been recently created.

2. Create a Docker container by running the Docker image with internal and external ports both 9999:

`docker run -p 9999:9999 <image_name>`

The output you see should look like:

``` 
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9999 (Press CTRL+C to quit)
```

3. Open your brower and type `localhost:9999` in the URL. 

4. You should see our webpage displayed.

