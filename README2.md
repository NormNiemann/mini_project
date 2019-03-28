## Guestbook Example

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



### Quick Start

This section shows the simplest way to get the example work. If you want to know the details, you should skip this and read [the rest of the example](#step-one-start-up-the-redis-master).

Start the guestbook with one command:

Ensure you are in the working dir

```
cd kubernetes-flask-example
```

```console
$ kubectl create -f .
service "redis-master" created
deployment "redis-master" created
service "redis-slave" created
deployment "redis-slave" created
service "frontend" created
deployment "frontend" created
```

Then, list all your Services:

```console
$ kubectl get services
NAME           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
frontend       NodePort    10.99.150.67    <none>        80:32515/TCP   34s
kubernetes     ClusterIP   10.96.0.1       <none>        443/TCP        48m
redis-master   ClusterIP   10.104.124.32   <none>        6379/TCP       34s
redis-slave    ClusterIP   10.104.43.119   <none>        6379/TCP       34s
```

Now with using minikube we can run the following to get the url for the service and access our app:

```
minikube service frontend --url
```

Use the URL given to us here and we can access it.  If you are not using minikube then you can access this via the ClusterIP or setup a load balancer or proxy to access the application.

Clean up the guestbook:

```console
$ kubectl delete -f .
```
