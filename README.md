## Tutorial for python flask with mongo db integration running in docker containers. 

Create a learning python flask application which is build on docker and connects with mongo DB for showing basic profile information. 

app.py -> Is the primary application for python flask applicaion. 

** For running it locally without running the application in the docker container** 

1. Clone the repository from github

```
git clone https://github.com/gdgupta11/docker_learning.git
```

2. Install docker and docker-compose if not already on your machine. 

Create a docker test network
```
docker network create testnet
```

To Spawn a mongo DB latest container:
```
docker run -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=apollo13 --net testnet --name mongo mongo
```
Also, I have spawned up a mongo-express container to view the data in the mongo DB.

```
docker run -d -p 8081:8081 -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin -e ME_CONFIG_MONGODB_ADMINPASSWORD=apollo13 -e ME_CONFIG_MONGODB_SERVER=mongo --net testnet --name mongo-express mongo-express
```

Once the docker images for mongo and mongo DB are running 

4. Login to mongo-express using admin:pass credentials  --> http://localhost:8081

5. Create a DB named profile 

6. Create a user collection (table)

7. Run the test.py script to ingest the values for first time for testing or create schema of userid, name, address and company. 

8. Run the python application locally 
```
    python app.y --> The application will run on localhost:8080 port
```

** For Running the application and entire ecosystem in docker container**

Either you can change the required values in app.py as per your requirement and then build the application locally using docker build command. 

The DockerFile is present in the folder for helping you to build the application. 
```
docker build -t flaskapp:2.0 . 
```
One the image is build you can run it with following commands
```
docker run -d -p 8080:8080 -v d:/logs:/var/log --net testnet --name flaskapp flaskapp:2.0 
```
For anything issues you can check logs using
```
docker ps ( for listing all the running containers)
docker logs <container name>
```
** 3rd way of directly pulling the already created flaskapp image and running it**

1. I have build the image and pushed it into docker.io personal container registry, you can directly pull it. 

2. in this case also you need to have mongo and mongo-express running 

3. pull the image  
```
docker pull gg951x/learnings:2.0 
```
4. run the image
```
docker run -d -p 8080:8080 -v d:/logs:/var/log --net testnet --name flaskapp flaskapp:2.0 
```