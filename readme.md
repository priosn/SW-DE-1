# Python/DevOps Project

## Question 1 - *Coding*
**Implement a GET method to show all the connections store in the database.**

You can find the solved exercise in the file *app.py*.

## Question 2 -Productization
**Prepare the application to be deployed in production environment.**

### Build a docker image
To create a Docker image for the Flask app , we have created a Dockerfile in the app directory. A Dockerfile contains a set of instructions describing the image and allows its automatic build. In this case: 
 * Base the image on Python version 3.10.4
 * Expose port 5000 (for Flask)
 * Create a working directory to which requirements.txt and app.py will be copied
 * Update pip package and install needed packages specified in requirements.txt

After you've created the Dockerfile, you need to build the image. To do this, we run the following command:
```sh
docker build --tag app_flask app/
```
Now, you can run `docker images` command to see a list of your images
```sh
$ docker images
REPOSITORY                TAG       IMAGE ID       CREATED         SIZE
app_flask                 latest    ac7663ee71d7   5 minutes ago   969MB
```
After successfully building the image, the next step is to run an instance (container) of the image.
```sh
docker run -p 5000:5000 app_flask
```

> Open a browser and type in the URL `hhtp:/0.0.0.0:5000`

### Upload the Docker image to Docker hub
You can find the image in Docker hub in the following [link](https://hub.docker.com/repository/docker/rivers054/flask_docker)

To download the Docker image from Docker hub, you can use:
```sh
docker pull rivers054/flask_docker:latest
```
### Build a Docker Compose file to deploy the applications using an external SQL database.
Before deploying the applications using an external SQL database, you have to build the images with the following command:
```sh
docker-compose build
```
Then, to run the dockerized app, you run the following command:
```sh
docker-compose up
```
That should run the containers successfully and you should be able to access to the API on `hhtp:/0.0.0.0:5000`.

## Question 3. CI/CD
**Automatize the productization process in your favorite Git repository hosting services**

We have created CICD.yml workflow script to build and push Docker image with Github actions.

