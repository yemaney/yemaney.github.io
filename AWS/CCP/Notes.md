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
  - [AWS Direct Connect](#aws-direct-connect)
  - [Local Zones](#local-zones)
  - [Wavelength Zones](#wavelength-zones)
  - [Data Residency](#data-residency)
  - [Gov Cloud](#gov-cloud)
  - [AWS China](#aws-china)
  - [AWS Ground Station](#aws-ground-station)
- [Cloud Architecture](#cloud-architecture)
  - [Cloud Architecture Terminologies](#cloud-architecture-terminologies)
  - [High Availability](#high-availability)
  - [High Scalability](#high-scalability)
  - [High Elasticity](#high-elasticity)
  - [Fault Tolerance](#fault-tolerance-1)
  - [High Durability](#high-durability)
  - [Business Continuity Plan (BCP)](#business-continuity-plan-bcp)
  - [Disaster Recovery Options](#disaster-recovery-options)
- [Management and Development Tools](#management-and-development-tools)
  - [AWS API](#aws-api)
  - [AWS Management Console](#aws-management-console)
  - [AWS Tools for PowerShell](#aws-tools-for-powershell)
  - [Amazon Resource Name (ARN)](#amazon-resource-name-arn)
  - [AWS Command Line Interface (CLI)](#aws-command-line-interface-cli)
  - [AWS Software Development Kit (SDK)](#aws-software-development-kit-sdk)
  - [AWS CLoudShell](#aws-cloudshell)
  - [Infrastructure as Code (IaC)](#infrastructure-as-code-iac)
  - [AWS CloudFormation](#aws-cloudformation)
  - [AWS Cloud Development Kit](#aws-cloud-development-kit)
  - [AWS Toolkit for VSCode](#aws-toolkit-for-vscode)
  - [Access Keys](#access-keys)
- [Shared Responsibility Model](#shared-responsibility-model)
  - [AWS Shared Responsibility Model](#aws-shared-responsibility-model)
- [Compute](#compute)
  - [VM's, Container, and Serverless](#vms-container-and-serverless)
  - [High PErformance Computing (HPC)](#high-performance-computing-hpc)
  - [Edge and Hybrid Computing](#edge-and-hybrid-computing)
  - [Cost and Capacity Management](#cost-and-capacity-management)

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

- `Tier 1 network`: is a network that can reach every other network on the internet without purchasing IP transit or paying for peering
  - aws availability zones are all redundantly connected to multiple tier-1 transit providers

## AWS Direct Connect
AWS Direct Connect is a private/dedicated connection between an on-prem data center and AWS.
- Two very-fast network connection options
  - lower 50-500MBps,  higher 1-10GBps
- Helps reduce network costs and increase bandwidth throughput
- Direct Connect Locations are trusted third party data centers that establish the connection

## Local Zones
Data centers located close to densely populated areas to provide single-digit millisecond low latency performance
- used to support highly-demanding applications sensitive to latency

## Wavelength Zones
- Allow for edge-computing on 5G networks, by partnering with telecoms
- ultra low latency, as close as possible to user
- create subnets tied to a wavelength zone, to be able to launch virtual machines to the edge of the targeted networks

## Data Residency
The physical or geographical location of where an organization or cloud resources reside.

- `Compliance Boundaries`: A regulatory compliance that describes where data and cloud resources area allowed to reside
- `Data Sovereignty`: Legal authority that can be asserted over data because its physical location is within the jurisdictional boundaries

For workloads that need to meet compliance boundaries strictly.
- `AWS Config`: 
  - policy as code service
  - create rules to continuously check aws resource configuration
- `IAM Polices`:
  - can be written to explicitly deny access to specific aws regions
- `AWS Outposts`:
  - physical rack of servers that you can put your data in

## Gov Cloud
Regions that allow customers to host sensitive and regulated workloads
- currently only in the US

## AWS China
AWS cloud offering in mainland china. Intentionally isolated from AWS global.

## AWS Ground Station
Fully managed service that lets you control satellite communications

# Cloud Architecture

## Cloud Architecture Terminologies
- `Availability`: Ability to ensure service remains available
- `Scalability`: Ability to grow and unimpeded
- `Elasticity`: Ability automatically to shrink and grow to meet the demand
- `Fault Tolerance`: Ability to prevent a failure
- `Disaster Recovery`: Ability to recover from a failure

## High Availability
Ensure service remains available
- no single point of failure

Can be achieved by running workloads across multiple availability zones.

`Elastic Load Balancer`:
- A load balancer allows you to evenly distribute traffic to multiple servers in one or more data center.
- routes traffic towards health data centers and servers

## High Scalability
Ability to increase your capacity based on the increasing demand of traffic, memory and computing power

- `Vertical Scaling` (Scaling Up): Upgrading to bigger server
- `Horizontal Scaling` (Scaling Out): Add more servers of the same size

## High Elasticity
Ability to `automatically` increase your capacity based on the increasing demand of traffic, memory and computing power

- relies on horizontal scaling
- Scaling out (add more servers of same size)
- Scaling In (remove servers of same size)

`Auto Scaling Groups` (ASG)
- AWS feature that will automatically add or remove servers based on scaling rules you define

## Fault Tolerance
Ability for your service to ensure there is no single point of failure.

- `Fail-over`: plans to shift traffic to a redundant system in case the primary system fails

`RDS Multi-AZ`:
- run duplicate standby database in another availability zone in case the primary one fails

## High Durability
Ability to recover from a disaster and to prevent data loss during recovery

`CloudEndure Disaster Recovery`:
- Continuously replicates your machines into a low-cost staging area in your target aws account and preferred region enabling fast and reliable recovery.

## Business Continuity Plan (BCP)
A document that outlines how a business will continue to operate during an unplanned disruption in services.

- `Recover Point Objective` (RPO)
  - maximum acceptable amount of data loss after an unplanned data-loss incident
  - how much data are you willing to lose
- `Recovery Time Objective` (RTO)
  - maximum amount of time your business can tolerate without incurring a significant financial loss
  - how much time are you willing to go down

## Disaster Recovery Options
Coldest to Warmest

- `Backup & Restore`
  - rpo/rto hours
  - back up your data and restore it to new infrastructure
- `Pilot Light`
  - rpo/rto 10 mins
  - data is replicated to another region with minimal services running
- `Warm Standby`
  - rpo/rto
  - scaled down copy of your infrastructure running ready to scale up
- `Multi-site Active`
  - rpo/rto
  - scaled up copy of your infrastructure in another region

# Management and Development Tools

## AWS API
Each aws service has its own service endpoint which you can send a request to.
- The api endpoints are usually accessed through the cli, sdk, or console

## AWS Management Console
A web based unified console.
- build, manage, and monitor everything
- point and click (clickops)

## AWS Tools for PowerShell
Lets you interact with the aws api via powershell cmdlets
- Powershell is A task automation and configuration management framework.

## Amazon Resource Name (ARN)
Uniquely identify aws resources.

## AWS Command Line Interface (CLI)
Allows users to programmatically interact with the aws api via entering commands into a shell.

## AWS Software Development Kit (SDK)
Collection of software development tools in one installable package.
- used to programmatically create, modify, delete, or interact ith aws resources.

## AWS CLoudShell
Browser based shell built into the aws management console.
- free, scoped per region, same credentials as logged in user

## Infrastructure as Code (IaC)
Configuration script to automate creating, updating, or destroying cloud infrastructure.
- a blueprint of your cloud infrastructure

AWS CloudFormation - JSON or YAML

AWS Cloud Development Kit - Code

## AWS CloudFormation
Allows you to write IaC as either JSON or YAML.
- simple, but can lead to large files

## AWS Cloud Development Kit
Allows you to use a programming language to write IaC.
- generate CloudFormation templates as an output
- comes with its own cli
- cdk pipelines to quickly set up ci/cd
- has a testing framework

AWS SDK looks similar, but the key difference is CDK ensures Idempotent of your Infrastructure.
- cdk wont create new resources if it hasn't been updated

## AWS Toolkit for VSCode
Open source for VSCode to create, debug, deploy aws resources.
- explore aws resources and stacks
- helps create SAM applications

## Access Keys
A key and secret required to have programmatic access to aws resources when interacting with the aws api outside of the management console.

# Shared Responsibility Model
A cloud security framework that defines the security obligations of the customer versus the cloud service provider (csp).

## AWS Shared Responsibility Model
Customer is responsible for security in the cloud.
- data
- configuration

AWS is responsible for security of the cloud.
- hardware
- operation of managed services
- global infrastructure

# Compute

## VM's, Container, and Serverless

Virtual Machines
- `Elastic Compute Cloud (EC2)`
  - allows you to launch a virtual machine in the cloud.
  - a virtual machine is an emulation of a physical computer using software
  - `Amazon Machine Image (AMI)`
    - a predefined configuration for a virtual machine
- `Amazon LightSail`
  - managed virtual server services
  - friendlier version of EC2

Containers
- `Elastic Container Service (ECS)`
  - container orchestration service
  - when you need docker as a service
- `Elastic Container Registry (ECR)`
  - repository for container images
- `ECS Fargate`
  - serverless container orchestration service
  - same as ECS, but aws manages the server, pay on demand
- `Elastic Kubernetes Service (EKS)`
  - fully managed kubernetes service

Serverless
- `AWS Lambda`
  - serverless functions service
  - fully managed by aws, customer only uploads code and configurations
  - pay based on runtime

## High PErformance Computing (HPC)
USually for machine learning workloads


`AWS ParallelCluster`
- cluster management tool
- make it easier to deploy and manage high performance computing clusters on aws

## Edge and Hybrid Computing
`Edge Computing`
- pushing your computing workloads outside of your network to run closer to destination location

`Hybrid Computing`
- running workloads on both on-premise data center and aws virtual private cloud (VPC)

`AWS Outposts`
- physical rack of servers that can be put in your data centers
- allow to user aws api and service in your data center

`AWS Wavelength`
- build and launch application in a telecom data center
- ultra low latency
- closest as possible to end user

`VMWare Cloud on AWS`
- manage on-premise virtual machines using VMWare as EC2 instances

`AWS Local zones`
- edge data centers located outside of an aws region
- when you need faster computing, storage, and databases in populated areas outside of aws region

## Cost and Capacity Management

`EC2 Spot Instances, Reserved Instances, and Savings Plan`
- save on computing by paying upfront, committing to yearly contract or by being flexible about availability and interruption to computing service

`AWS Batch`
- plans, schedules, and executes batch computing workloads
- can utilize spot instances to save money

`AWS Compute Optimizer`
- uses machine learning to analyze usage
- suggests how to reduce costs and improve performance

`EC2 Autoscaling Groups (ASG)`
- automatically add or remove EC2 servers based on current traffic

`Elastic Load Balancer (ELB)`
- distribute traffic to multiple machines
- re-route traffic from unhealthy instances to healthy instances or different availability zones

`AWS Elastic Beanstalk (EB)`
- for easily deploying web applications
- PaaS