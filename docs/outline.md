


Objective: demonstrate the fundamentals of 2 key methods of deployment (via cli or from manifest file) 

## Game Plan:
- capture the steps for deploying a dockerized flask app from the cli and with manifests

##Part 1: Create a python/flask development envrionment
- create a dockerfile as shown to use as a development envrionment
- build/test the container locally

##Part 2: create the flask app and test it
- start from the cli inside the running python container
- create a a file app.py for our flask app (using content as shown)
- run the app from inside the container, test it by using curl from the cli in the container

##Part 3: run the container locally and test the service
- run the container locally exposing the proper ports to validate the service works
- validate uri works via curl/browser calling from the host machine where the container's running

##Part 4: validate minikube is running
- start and validate minikube is operational

##Part 5: 
- push the container to dockerhub
- deploy the container to minikube from the cli
- validate access to the container running on minikube via curl and browser
- stop and destroy the running container

##Part 6:
- create a pod description (as shown) to more easily manage the deployment
- validate the pod has been deployed and is accesisble

##Part 7:
- create a replication controller description (as shown) to 

Notes:
- show the steps so users can follow along, but allow the vagrant envrionment to dynamically setup the envrionment

