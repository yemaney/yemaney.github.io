- [Cloud Concepts](#cloud-concepts)
  - [What is Cloud Computing](#what-is-cloud-computing)
  - [Types of Hosting](#types-of-hosting)
  - [What Is A Cloud Service Provider (CSP)](#what-is-a-cloud-service-provider-csp)
  - [Evolution of Computing](#evolution-of-computing)
  - [Types of Cloud Computing](#types-of-cloud-computing)
  - [Cloud Computing Deployment Models](#cloud-computing-deployment-models)
- [The Benefits Of The Cloud](#the-benefits-of-the-cloud)
  - [Seven Advantages to Cloud](#seven-advantages-to-cloud)
- [AWS Global Infrastructure](#aws-global-infrastructure)
  - [Regions](#regions)
  - [Availability Zones](#availability-zones)
  - [Fault Tolerance](#fault-tolerance)
  - [AWS Global Network](#aws-global-network)
  - [Points Of Presence (PoP)](#points-of-presence-pop)

# Cloud Concepts

## What is Cloud Computing
- The practice of using a network of remote servers hosted on the internet to store, manage, and process data, rather than a local server.
- Cloud providers own the servers, and manages the physical upkeep. 
- You are responsible for configuring only the services and code

## Types of Hosting
- `Dedicated servers`: One physical machine dedicated to a single application
- `Virtual Private Server (VPS`: One physical machine, virtualized into submachine to run multiple applications.
- `Shared Hosting`: One physical machine shared by hundred of businesses.
- `Cloud Hosting`: Multiple physical machines shared by thousands of businesses and services.

## What Is A Cloud Service Provider (CSP)
- Provides multiple cloud services which can be chained together to create cloud architectures
  - `compute`: a virtual computer to run applications
  - `networking`: to define internet connections or network isolation
  - `storage`: virtual hard-drive to store files
  - `databases`: virtual databases for storing and reporting data

## Evolution of Computing
- `Dedicated`:
  - a physical server wholly utilized by a single customer
  - guaranteed full utility of underlying resources
  - can't vertically scale, must migrate
  - will overpay for underutilized server
  - limited by host OS
  - multiple apps running can lead to resource sharing conflicts
- `Virtual Machine's`:
  - can run multiple virtual machines on one machine
  - physical server shared by multiple customers
  - pay a for a fraction of server
  - overpaying for underutilized server
  - limited by host OS
  - multiple apps running can lead to resource sharing conflicts
  - easy to export or import images for migration
  - easy to vertically or horizontally scale
  - `​Hypervisor​` is the software layer that lets you run the VMs​
- `Containers`:
  - Multiple applications can run side by side without OS conflicts
  - More efficient than virtual machines
  - ​`Docker Deamon​` is the name of the software layer that lets you run multiple conta## iners.​
- `Functions`:
  - managed VM's running managed containers
  - known as serverless compute
  - your only responsibility is code and data
  - very cost effective, only pay for time code is running
  - cold start side effect

## Types of Cloud Computing
- `SaaS`: Software as a service
  - Completed project managed by a service provider
  - Gmail
- `PaaS`: Platform as a service
  - provide platform to develop, run, and manage applications without the complications of maintaining infrastructure
  - AWS Elastic Beanstalk
- `Iaas`: Infrastructure as a service
  - Most basic building blocks of cloud IT infrastructure.
  - most flexibility and management control
  - AWS, Azure, GCP

## Cloud Computing Deployment Models
- Cloud: Everything built and runs on the CSP
- On Premise: Everything built on company's data centers
- Hybrid: Both on Cloud and On Premise being used
- Cross Cloud: Using more than one CSP

# The Benefits Of The Cloud

## Seven Advantages to Cloud
1. `Cost-Effective`: Pay as you go with thousands of customers sharing the cost of the resources
2. `Global`: Launch workloads anywhere in the world
3. `Secure`: Cloud provider takes care of physical security
4. `Reliable`: Data backup, disaster recovery, data replication, fault tolerance
5. `Scalable`: Increase or decrease resources based on demand
6. `Elastic`: Automate scaling during spikes and drop in demand
7. `Current`: Underlying hardware and software are managed without interruption to you

# AWS Global Infrastructure

## Regions
A geographically distinct location which has multiple data-centers (AZs).

- Each region has at least two availability zones
- not all services are available in all region

## Availability Zones
A physical location made up of one or more data centers.

The use of AZ's give customers the ability to operate production applications and databases that are more:
- Highly available
- Fault tolerant
- Scalable

A subnet is associated with an availability zone.
- Launch AWS resource into a specific subnet to launch the resource into a specific AZ

## Fault Tolerance
`Fault Domain`: A section of a network that is vulnerable to damage if critical device or system fails.
- if a failure occurs, it will not cascade outside that domain

`Fault Level`: A collection of fault domains

If an application is partitioned across AZs, companies are better protected from issues such as power outages, storms, etc.

## AWS Global Network
The AWS Global Network represents the interconnections between AWS Global Infrastructure.
- `Edge Locations` can act as on and off ramps to the AGN
  - `AWS Global Accelerator` and `AWS S3 Transfer Acceleration` use edge locations to quickly reach AWS resources in other regions by traversing the AGN
  - Amazon CloudFront (CDN) uses edge locations to provide edge storage and compute near the end user
  - `VPC Endpoints` ensure your resources stay within the AWS Network and do not traverse over the public cloud

## Points Of Presence (PoP)
Intermediate locations between AWS Region and the end user.
  - For AWS this is a data center utilized for content delivery or faster upload
  - `Edge locations` are data centers that hold caches of the most popular files, so that delivery of distance to the end users are reduced
  - `Regional Edge Cache` are data centers that hold much larger caches of less-popular files to reduce full round trip and cost of transfer fees
  - `AWS CloudFront` is a Content Delivery Network (CDN) service that:
    - routes requests to the nearest edge location cache
    - allows to choose an origin to be the source of cache
    - caches the contents of what origin would be returned to various edge locations