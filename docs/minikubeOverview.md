
# Up and running with Minikube


---

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Getting an Environment Up and Running](#getting-an-environment-up-and-running)
- [What is Kubernetes?](#what-is-kubernetes)
- [Getting Minikube Installed](#getting-minikube-installed)
- [Looking around Minikube](#looking-around-minikube)
- [Running an application on minikube](#running-an-application-on-minikube)

<!-- /TOC -->

## Getting an Environment Up and Running
We'll use Vagrant as our working environment. This makes it easy to use, and to share via Git. We'll initialize the vm using the standard centos box.
https://atlas.hashicorp.com/centos/boxes/7

Initializing a new enviornment is easy enough. You can either create a new environment on your own, or you can download the vagrant file I've created to make life easy, and just get started by typing  'vagrant up' at the command line in the directory where the Vagrant file lives.

With a brand new centos 7 environment up and running you can do all the updates, and we can get started.

## What is Kubernetes?
Kubernetes is one of several choices for providing ... but if you ask the good folks at Kubernetes, they'll tell you that "Kubernetes is an open-source platform for automating deployment, scaling, and operations of application containers across clusters of hosts, providing container-centric infrastructure.". Which is a pretty official way of saying that you can run containers at scale in production. If you've spent enough time working with containers to start thinking of using them in production, you'll have considered 2 things... 1) that learning how containers work wasn't too painful. 2) Learning how to run containers at scale in production seems to be a separate discussion entirely that needs to be investigated further.  Kubernetes is a great option for managing containers in production.

When I first started looking at Kubernetes, my first thought was "gee,  looks like I might need get a new machine?... or two maybe?". Fortunately one of the 2016 projects from the K8s team has been to create a local development environment, which is also a great local environment to get to know Kubernetes a bit better.


## Getting Minikube Installed
Minikube expects that Virtualbox is installed. Which is pretty easy to get running on mac, linux or windows. [ //todo:  add a tutorial for installing both virtualbox and vagrant and put a pointer here ].
Let's start by getting Minikube donwloaded and installed

```bash
$ curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.14.0/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 82.7M  100 82.7M    0     0   893k      0  0:01:34  0:01:34 --:--:--  851k
```


We'll also need kubectl since that's the key admin tool.

```bash
$ curl -Lo kubectl https://storage.googleapis.com/kubernetes-release/release/v1.5.1/bin/linux/amd64/kubectl && chmod +x kubectl && sudo mv kubectl /usr/local/bin/
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 48.0M  100 48.0M    0     0   420k      0  0:01:56  0:01:56 --:--:--  753k
```


With Minikube installed we'll start it with 'Minikube start'.

```bash
$ minikube start
Starting local Kubernetes cluster...
Kubectl is now configured to use the cluster.
```

We can check the status with 'minikube status'.

```bash
$ minikube status
minikubeVM: Running
localkube: Running
```

Now that Minikube running and kubectl is configured... let's poke around a bit and see what's there!

---

## Looking around Minikube
Minikube has lots of capabilities, for spinning up containers in a way that's conducive to a production environment. Let's start by taking a look at


```bash
$ minikube status
minikubeVM: Running
localkube: Running
```


We can check to see what nodes are running

```bash
$ kubectl get nodes
NAME       STATUS    AGE
minikube   Ready     38d
```


We can also check to see what pods are running

```bash
$ kubectl get pods --all-namespaces
NAMESPACE     NAME                                    READY     STATUS    RESTARTS   AGE
default       hello-minikube-3015430129-h0d70         1/1       Running   5          38d
default       my-web-1068939808-sx7gk                 1/1       Running   3          38d
kube-system   kube-addon-manager-minikube             1/1       Running   3          1h
kube-system   kube-dns-v20-n19fd                      3/3       Running   15         38d
kube-system   kubernetes-dashboard-3203700628-9xm3t   1/1       Running   3          38d
kube-system   kubernetes-dashboard-x8gtq              1/1       Running   3          1h
kube-system   kubernetes-dashboard-zitr5              1/1       Running   6          38d
```



---

## Running an application on minikube
Now that we have our Minikube cluster up and running, lets run some stuff on it... we'll try the sample guestbook application. The application uss Redis and a PHP front end.

```bash

$ kubectl create -f https://raw.githubusercontent.com/kubernetes/kubernetes/master/examples/guestbook/all-in-one/guestbook-all-in-one.yaml
service "redis-master" created
deployment "redis-master" created
service "redis-slave" created
deployment "redis-slave" created
service "frontend" created
deployment "frontend" created
```

Now 3 deployments are available... we can also dig into more of the details.

Typing 'minikube dashboard' opens a browser based dashboard that gives us more insight.
[[todo: add a jpeg showing the dashboard ]]

Since the guestbook service won't be available outside the kubernetes development cluster, we'll need to add a proxy.

```bash
$ kubectl proxy

```


now we should be able to hit the guestbook

```bash
$ open localhost: http://localhost:8001/api/v1/proxy/namespaces/default/services/frontend

```


---

###### [irvingr2017|tutorial]
