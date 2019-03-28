## Brewery Example

This is a Flask app using a breweries API that does not require authentication.
It provides the user access to information about various breweries in the U.S.
It allows the user to enter the type of brewery (e.g. micro) as a parameter, returning information about breweries which fit the parameter type


## Building Your Own Image
You can use the images already pre-defined in the kubernetes manifest files or you can use the below to create your own images and use them:

Replace the realbtotharye with your Dockerhub repository

```
docker build -t gcr.io/${PROJECT_ID}/hello-app:v1 .
docker push gcr.io/${PROJECT_ID}/hello-app:v1

docker build -t realbtotharye/flask-kubernetes-redis flask-redis/
docker push realbtotharye/flask-kubernetes-redis
```

### Create Cluster

gcloud container clusters create hello-cluster --num-nodes=2
gcloud services enable container.googleapis.com

### Check cluster is created 
gcloud compute instances list

### Deploy app listening on port 8080
kubectl run hello-web --image=gcr.io/${PROJECT_ID}/hello-app:v1 --port 8080

### Delete Deployment
kubectl delete deployment hello-web






```console
$ kubectl delete -f .
```
