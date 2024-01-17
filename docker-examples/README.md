## Docker Examples Guide

The example folder contains the Docker usages examples, the main focus is to use Docker for the AI Models Development and Deployment.

There are there three examples:
1. 🔰 Simple Docker Example: How to use simple container using Dockerfile and manipulate the image (Picture)
2. 🏹 Intermediate Example: How to run the OpenCV inference using Live camera feed and detect the face, then show the Live feed on web browser using Python Flask.
3. 🔱 Advanced Example: Comming Soon ! 

### 1. Simple Docker Example


This is the given file tree for the simple Docker example:
```bash
simple/
├── Dockerfile
├── image_processing.py
├── requirements.txt
└── sample.jpg
```

The purpose of this example is to load a image using OpenCV and convert into gray scale then write the converted image into output folder.
This is the content of the `Dockerfile`
```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run Python script when the container launches
CMD ["python", "./image_processing.py"]
```
The given instructions in `Dockerfile` can be breakdown into following.
1. Prepare or install the OpenCV in docker image - for that we are using the `python:3.8-slim` docker image and then installing the OpenCV using [requirements.txt](docker-examples/simple/requirements.txt), that can be found in the [Dockerfile](docker-examples/simple/Dockerfile) 
2. Copy all the data to the docker image by using the `COPY` command in `Dockerfile`. 
2. To read, converting and writing the image, the `image_processing.py` is being used.
3. The last step is to build the Docker Image using Dockerfile (It will get all the instructions from the `Dockerfile` and create the Docker Image by setting the `image_processing.py` as startup script.)
4. Lastly we need to run the docker container by using the same docker image we created.

#### 1.1 Build Docker Image and run the Docker Container 
By these two commands, the docker image is being created with name `my-computer-vision-app` and we can run the docker container by using `docker run`. 
```bash
# change the dir to simple folder
cd docker-examples/simple

# to build the docker image from the Dockerfile, that will install the opencv as requirment.
docker build -t my-computer-vision-app .
```
After successful execution of the `docker build` you can check the docker builded a local `docker image` you can check the by `docker images`
```console
(base) usman@saikhu:~/docker-tutorial/docker-examples/simple$ docker images
REPOSITORY               TAG       IMAGE ID       CREATED         SIZE
my-computer-vision-app   latest    0bab9d7512b1   3 minutes ago   344MB
hello-world              latest    d2c94e258dcb   8 months ago    13.3kB
```
Now, we just create a docker image using all the instructions from the Dockerfile, now we can run the docker container from this image that we just created, by following command.
```bash
# to run the docker image that we create with previous command.
# the output will be saved in output folder.
docker run --rm -v $(pwd)/output:/usr/src/app/output my-computer-vision-app
```

After  successful execution of `docker run` command, there will be new folder created in the same dir with name of output, inside of this folder you should see the gray image converted by the container that we just run.




### 2. Intermediate Example: Live Face Detection using OpenCV and Flask

Live Face Detection using OpenCV and Flask
This application demonstrates an intermediate-level example of using OpenCV for live face detection, with the feed displayed in a web browser using a Flask server. The application captures video from a camera, applies face detection in real-time, and streams the processed video to a Flask web app.

#### 2.1 Features
- Live video capture using OpenCV.
- Real-time face detection using Haar Cascades.
- Video streaming to a web browser through Flask.
- Containerized setup using Docker.

#### 2.2 Prerequisites
- Python 3.8 or later.
- Docker.
- Access to a webcam.
#### 2.3 Installation and Setup

##### 2.3.1 Change the working dir
```bash
cd docker-examples/intermediate
```
##### 2.3.2 Build the Docker Image
```bash
docker build -t my-cv-flask-app .
```
##### 2.3.3 Run the Docker Container
```bash
docker run --rm --device /dev/video0:/dev/video0 -p 5000:5000 my-cv-flask-app
```


#### 2.4 Usage
Once the Docker container is running, navigate to `http://localhost:5000` or check the output from terminal like below in your web browser to view the live face detection feed.

```console
(base) usman@saikhu:~/docker-tutorial/docker-examples/intermediate$ docker run --rm --device /dev/video0:/dev/video0 -p 5000:5000 my-cv-flask-app
 * Serving Flask app 'app.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
```
The output should be like this.

![Alt text](/assets/output.gif)

#### 2.5 File Structure
```console
intermediate/
├── app.py # Flask application script with OpenCV for face detection.
├── Dockerfile # Docker configuration file.
├── requirements.txt # List of Python dependencies.
└── templates # Directory containing Flask HTML templates.
    └── index.html
```
You can modify the app.py script to change the face detection algorithm or apply other image processing techniques using OpenCV.

