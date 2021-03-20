### How to get things working

1. Start the Docker app on your computer.

2. Download the image provided, and navigate to the directory with the image.

3. Load the docker image using this command: `docker load < colx_523_project_group_6.tar`

4. Create a Docker container by running the Docker image with internal and external ports both 9999:

`docker run -p 9999:9999 <image_name>`

The output you see should look like:

``` 
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9999 (Press CTRL+C to quit)
```

5. Open your brower and type `localhost:9999` in the URL. 

6. You should see our interface displayed in the window.

