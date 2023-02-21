# Elastic Container Service (ECS)

## Introduction to Containers

Virtual machines virtualize operating systems.
- os consume a lot of the resources (bloat)

Container engine runs as a process within host os.
- containers run on top of container engine
- `doesn't create full new os` for each instance
- much `lighter` than virtual machines

`Docker Image`
- created using a `docker file`
- created from base image or scratch
- images contain read only layers, `(file system layers)`
- each set of changes adds another layer to the docker image
  - changes are layered onto the image using a differential architecture
- used to create a `docker container`

`Docker Container`
- running copy of a docker image
- has an addition `read write file system layer`
  - allows containers to run
- multiple containers can be created from the same docker image
  - the difference between containers created from the same docker image is only the final read write layer
  - similar `layers are reused` across containers
- portable, self contained, always run as expected
- ports are `exposed` to the host and beyond
- applications stacks can be multi-container

`Container Registry (dockerhub)`
- registry of container images
- where images are uploaded and downloaded from
  - download centos base image from here for example

## ECS Concepts

Allows you o use containers running on infrastructure managed by aws

- `ec2 mode`:  hosted on ec2 instances
- `fargate` : serverless way of running docker containers
- `container definition` : tells ecs which image to use and which ports are exposed
- `task definition`: represents an `application` as a whole
  - can be made of `one or more containers`
  - store the: 
    - `resources` used by task (cpu and memory)
    - `networking` mode that task use
    - `compatibility` (ex2 or fargate)
    - `task role` : iam role that a task can assume to gain temporary credentials to interact with aws
- `ecs service`
  - service definition : define how we want a task to `scale`
    - used to create HA along with a load balancer
    - how many copies, restarts
- `ecs cluster` : where containers run from
  - upload task or service here

## Cluster Modes

Main difference is Admin overhead involved and costs.

- ecs management components : handle scheduling, orchestration, cluster management, placement engine (where to run containers)

`EC2 Mode`
- ecs cluster created within a vpc
  - benefits from `multiple AZ` available in the vpc
- instances run the containers
- specify an initial size which controls the number of container instances
  - handled by an autoscaling group (`ASG`)
- tasks and services
  - get images from registry
  - uses task and service definition to deploy container images onto container hosts as containers
- `user manages the cluster`
- `pay for instance even if they aren't running containers`

`Fargate Mode`
- still define task an service definitions, cluster, and vpc
- runs  on `shared AWS infrastructure`
- each task or service gets injected into vpc
  - given an elastic network interface ENI (ip address within the vpc)
- only pay for the resources that running containers consume

Scenarios and Choices
`EC2`
- large workload
- price conscious
`ECS(EC2 mode)`
- if you use containers
`Fargate`
- large workload
- overhead conscious
- small or burst workloads
- batch or periodic workloads

## Kubernetes

- open-source system for automating deployment, scaling, and management of containerized applications.
- `cluster`
  - deployment of kubernetes, management, orchestration
- `cluster control plane`
  - manages the cluster, scheduling, applications, scaling and deploying
  - `kube-apiserver`
    - front end for kubernetes control plane
    - what nodes interact with
    - can horizontally scale for HA
  - `etcd`q
    - highly available key value storage within cluster
  - `kube-scheduler`
    - assigns node to pods based on needs and constraints
  - `cloud-controller-manager`
    - provide cloud specific control logic
  - `kube-controller-manager`
    - `node controller` : monitoring and responding to node outages
    - `job controller` : run pods to execute jobs
    - `endpoint controller` : populates endpoints in cluster
    - `service account & token` : accounts/api token creation
  - `kube-proxy`
    - runs on each node
    - coordinates networking
- `cluster nodes`
  - vm or physical server on which pods are placed in
  - `containerd` or `Docker` software for handling container operations
  - `kubelet` agent to interact with cluster control plane
- `pods`
  - 1+ containers, often one container per pod
  - smallest units of computing
  - pods are non-permanent
- `service`
  - abstraction, running on one or more pod
- `ingress`
  - exposes way into a service
  - `ingress controller`
    -  used to provide ingress
-  `persistent storage`
   -  lifecycle lives beyond any 1 pod

## Elastic Kubernetes Service (EKS)

- aws managed kubernetes
- control plane scales and runs on multiple AZs
- integrates with AWS services
  - ECR, RLB, IAM, VPC, EBS, EFS
- EKS cluster
  - eks control plan & eks nodes
- etcd distributed across multiple AZs
- nodes
  - self managed on ec2
  - managed node groups : eks handles provisioning and lifecycle management
  - fargate
