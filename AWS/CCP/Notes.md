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
- [Storage](#storage)
  - [Types of Storage](#types-of-storage)
  - [S3 Storage  Classes](#s3-storage--classes)
  - [AWS Snow Family](#aws-snow-family)
  - [Storage Services](#storage-services)
- [Networking](#networking)
  - [Cloud-Native Networking Services](#cloud-native-networking-services)
  - [Enterprise/Hybrid Networking Services](#enterprisehybrid-networking-services)
- [Databases](#databases)
  - [Data Warehouse](#data-warehouse)
  - [NoSQL Database Services](#nosql-database-services)
  - [Relational Database Services](#relational-database-services)
  - [Other Database Services](#other-database-services)
- [Elastic Compute Cloud (EC2)](#elastic-compute-cloud-ec2)
  - [Introduction to EC2](#introduction-to-ec2)
  - [Instance Families](#instance-families)
  - [Instance Type](#instance-type)
  - [Dedicated Host vs Dedicated Instance](#dedicated-host-vs-dedicated-instance)
  - [Elastic IP](#elastic-ip)
- [EC2 Pricing Model](#ec2-pricing-model)
  - [Reserved Instances](#reserved-instances)
  - [Reserved Instances (RI)](#reserved-instances-ri)
  - [REgional and Zonal RI](#regional-and-zonal-ri)
  - [RI Limits](#ri-limits)
  - [Capacity Reservations](#capacity-reservations)
  - [Standard vs Convertible RI](#standard-vs-convertible-ri)
  - [Savings Plan](#savings-plan)
- [Identity](#identity)
  - [Zero-Trust Model](#zero-trust-model)
  - [Zero-Trust Model on AWS](#zero-trust-model-on-aws)
  - [Directory Service](#directory-service)
  - [Identity Providers (IdP)](#identity-providers-idp)
  - [Single Sign On](#single-sign-on)
  - [Lightweight Directory Access Protocol (LDAP)](#lightweight-directory-access-protocol-ldap)
  - [Multi-Factor Authentication](#multi-factor-authentication)
  - [Security Keys](#security-keys)
  - [AWS Identity and Access Management (IAM)](#aws-identity-and-access-management-iam)
  - [Anatomy of an IAM Policy](#anatomy-of-an-iam-policy)
  - [Principle of Least Privilege (PoLP)](#principle-of-least-privilege-polp)
  - [AWS Account Root User](#aws-account-root-user)
  - [AWS SSO](#aws-sso)
- [Application Integration](#application-integration)
  - [Queueing and Simple Queue Service (SQS)](#queueing-and-simple-queue-service-sqs)
  - [Streaming and Kinesis](#streaming-and-kinesis)
  - [Pub-Sub and SNS](#pub-sub-and-sns)
  - [API Gateway](#api-gateway)
  - [State Machines](#state-machines)
  - [Event Bus](#event-bus)
  - [Other Application Integration Services](#other-application-integration-services)
- [Containers](#containers)
  - [VM's vs Containers](#vms-vs-containers)
  - [Micro-services](#micro-services)
  - [Kubernetes (K8's)](#kubernetes-k8s)
  - [Docker](#docker)
  - [Container Services](#container-services)
- [Governance](#governance)
  - [Organizations and Accounts](#organizations-and-accounts)
  - [AWS Control Tower](#aws-control-tower)
  - [AWS Config](#aws-config)
  - [AWS Quick Starts](#aws-quick-starts)
  - [Tagging](#tagging)
  - [Resource Groups](#resource-groups)
  - [Business Centric Services](#business-centric-services)
- [Provisioning](#provisioning)
  - [Provisioning Services](#provisioning-services)
  - [AWS Elastic Beanstalk](#aws-elastic-beanstalk)
- [Serverless Services](#serverless-services)
- [Windows on AWS](#windows-on-aws)
- [Logging](#logging)
  - [Anatomy of an Alarm](#anatomy-of-an-alarm)
  - [CloudWatch Logs — Log Streams](#cloudwatch-logs--log-streams)
  - [Log Insights](#log-insights)

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

# Storage

## Types of Storage
`Elastic Block Storage (EBS)`
- when you need a virtual hard drive attached to a vm
- only a single write volume

`Elastic File Storage (EFS)`
- when you need a file-share where multiple vms need to access the same drive
- multiple connections via network share

`Simple Storage Service (S3)`
- multiple reads and writes
- max object size 5TB, unlimited numbe rof objects

## S3 Storage  Classes

`S3 Standard`
- fast
- highly available and durable
- replicated across 3 AZ's

`S3 Intelligent Tier`
- use ML to analyze object usage and determine the appropriate storage class

`S3 Standard-IA (Infrequent Access)`
- Cheaper if you access files less than once a month

`S3 One-Zone-IA`
- objects only exist in one AZ

`S3 Glacier`
- for long term cold storage
- retrieval can take minutes to hours
- very cheap

`S3 Glacier Deep Archive`
- lowest cost storage class
- data retrieval 12 hours

## AWS Snow Family
Storage and compute devices used to physically move data in or out the cloud when moving data over the internet is to slow, difficult, or costly.

`Snowcone`
- comes in two sizes: 8TB, 14TB

`Snowball Edge`
- comes in two types
  - storage optimized
    - 80TB
  - compute optimized
    - 39.5 TB

`Snowmobile`
- 100PB

## Storage Services

- `S3 (Simple Storage service)`
  - object storage service
  - industry-leading scalability, data availability, security, and performance
- `S3 Glacier`
  - low cost storage fir archiving and long-term backup
  - longer data retrieval wait time
- `Elastic Block Storage (EBS)`
  - virtual hard drive you attach to EC2 instances
- Elastic File Storage (EFS)
  - file storage mountable ot multiple EC2 instances at the same time
- `Storage Gateway`
  - hybrid cloud storage with local caching
  - expand in-premise storage capacity into the cloud
- `File Gateway`
  - extend local storage to S3
- `Volume Gateway`
  - caches local drives to S3, so you have a continuous back up of local files in the cloud
- `Tape Gateway`
  - stores files onto virtual tapes for backing up on very cost effective long term storage
- `AWS Snowfamily`
  - storage devices used to physically migrate large amounts of data to the cloud
- `AWS Backup`
  - fully managed backup service
- `CloudEndure Disaster Recovery`
  - continuously replicates your machines into a low-cost staging area in your target aws account and preferred region
  - enabling ast and reliable recovery in case of failures

# Networking

## Cloud-Native Networking Services

- `Region`
  - geographical location of your network
- `Availability Zone (AZ)`
  - data center containing aws resources
- `Virtual Private Cloud (VPC)`
  - isolated section of aws cloud where you can launch aws resources
- `Internet Gateway`
  - enables access to the internet for you VPC
- `Route Tables`
  - determines where network traffic from your subnets are directed
- `Network Access Control List (NACL)`
  - act as a firewall at the subnet level
  - create Allow and Deny rules.
- `Security Groups`
  - act as a firewall at the instance level
  - only Allow rules.
- `Subnets`
  - partition of an IP network intro multiple, smaller network segments
  - Public subnets are generally used for placing resources which are accessible on the internet
  - Private subnets are used when you need resources to be more secured and only accessible through tightly filtered traffic into the subnet

## Enterprise/Hybrid Networking Services
- `Direct Connect`
  - dedicated gigabit network connection from you premises location to aws
- `AWS Virtual Private Network (VPN)`
  - establish secure connection to aws network
  - site-to-site: on-prem to aws
  - client vpn: user laptop to aws
- `PrivateLinks (VPC Interface Endpoints)`
  - keeps traffic within the aws network and not traverse the internet to keep traffic secure

# Databases

## Data Warehouse
A relational database designed for `analytic workloads`.
- generally perform aggregation, such as grouping
- optimized around columns since they need to aggregate column data
- designed to be HOT, return results from queries very fast
- infrequently accessed
- consume data from a relational database on a regular basis

## NoSQL Database Services
- `DynamoDB`
  - serverless, NoSQL, key/value, and document database
  - designed to scale to billions of records
  - guaranteed consistent data returns within a second
- `DocumentDB`
  - NosQL document database that is MongoDB compatible
- `Amazon Keyspaces`
  - fully managed apache cassandra database

## Relational Database Services

- `Relational Database Service (RDS)`
  - supports common sql engines
    - mysql, mariadb, postgres, oracle, microsoft sql server
- `Aurora`
  - fully managed, of either MySQL or PostgreSQL
- `Aurora Serverless`
  - serverless on demand version of aurora
  - when you want most of aurora functionality but can trade to have cold starts
- `RDS on VMWare`
  - deploy rds managed databases to on premise data center

## Other Database Services

- `Redshift`
  - petabyte size data warehouse
- `ElastiCache`
  - managed database of in memory and caching open-source
  - when you need to improve the performance of applications by adding a caching layer in front of the web server or database
- `Neptune`
  - graph database
  - when you need to understand the connections between data
- `Amazon Timestreams`
  - fully managed time series database
  - when you need to measure how things change over time
- `Amazon Quantum Ledger`
  - fully managed ledger database that provides transparent, immutable, and cryptographically variable transaction logs
- `Database Migration Service (DMS)`
  - on-premise database to aws
  - from two databases using different sql engines
  - from sql to nosql

# Elastic Compute Cloud (EC2)

## Introduction to EC2
A highly configurable virtual machine.

Steps
- choose os
- choose instance type
- add storage (EBS, EFS)
- configure instance
  - Security Groups, Key Pairs, UserData, IAM Roles, Placement Groups

## Instance Families
Different combinations of cpu, memory, storage, and network capacity.
- allows you to choose the appropriate combination of capacity to meet your applications unique requirements


Family Names
- `General Purpose`
  - balance of compute, memory, and network resources
  - web servers and code repositories
- `Compute optimized`
  - high performance processor
  - scientific modeling, gaming servers
- `Memory Optimized`
  - fast performance for workloads that process large data sets in memory
  - real time big data analytics, in-memory caches
- `Accelerated Optimized`
  - hardware accelerators or co-processors
  - machine learning, computational finance
- `Storage Optimized`
  - high sequential read and write access to very large data sets on local storage
  - NoSQL, data warehousing

## Instance Type
A particular instance size and instance family

- EC2 Instance Sizes generally double in price and key attributes

## Dedicated Host vs Dedicated Instance
- `Dedicated Host`
  - physical server isolation
  - socket, cores, host ID visibility
  - more expensive
- `Dedicated Instance`
  - instance isolation via virtualization
  - virtual server always lives on the same part of the physical server
- `Default`
  - vm instance lives in a specific part of physical server until a reboot

## Elastic IP
A way to configure static IP address for virtual machines.

# EC2 Pricing Model

- `on-Demand`
  - least commitment
  - low cost and flexible
  - pay per hour
  - short term, unpredictable workloads
  - cannot be interrupted
- `Reserved`
  - best long term saving, upt to 75%
  - commit to 1 or 3 years
  - can resell unused reserved instances
  - the greater upfront the great the savings
- `Spot`
  - biggest savings, up to 90%
  - request spare computing capacity
  - flexible, can handle interruptions
- `Dedicated`
  - most costly
  - can be on demand or reserved (up to 75%)

## Reserved Instances
Designed for applications that have a steady-state, predictable usage, or require reserved capacity.

`Class` : the less flexible the greater the savings
- Standard
  - up 75% reduced pricing compared to on-demand
  - can modify ri attributes
- Convertible
  - up to 54% reduced pricing compared to on-demand
  - can exchange ri attributes

`Payment Options`:The greater upfront the greater the savings
- All upfront
- Partial upfront
- No upfront

## Reserved Instances (RI)
Also known as instance attributes. 

- `instance type`
  - instance family + instance size
- `region`
- `tenancy`
  - whether your instance runs on shared or single tenant hardware
- `platform`
  - the operating system of the machine

## REgional and Zonal RI
When you purchase a RI, you determine the scope of the reserved instance. The scope does not affect price.

`Regional RI`: Purchase for a region
- does no reserve capacity
- discount applies to instances in any AZ in the region
- discount can apply to instance within the instance family
- can purchase regional ri

`Zonal RI`: Purchase fo an availability zone
- reserves capacity in the specified availability zone
- discount only applies to instance in the selected AZ
- no instance size instance size flexibility
- can't purchase zonal ri

## RI Limits
Per-month you can purchase
- 20 regional reserved instances per region
  - cannot be used to exceed on-demand instance limit (20)
- 20 zonal reserved instances per AZ
  - can exceed on-demand instance limit

## Capacity Reservations
Request a reservation of a specific EC2 instance type or family.

## Standard vs Convertible RI
- `Standard` 
  - can be modified
  - changed az within same region, scope from zonal to regional, instance size, network
- `Convertible`
    - can be exchanged for another convertible ri with new ri attributes including
      - instance family, instance type, platform, scope, tenancy

## Savings Plan
Offers similar discounts as reserved instances but simplifies the purchasing process.
- two different terms ( 1 year or 3 years)
- `payment options`
  - all upfront
  - partial upfront
  - no upfront
- `Types`
  - `compute`
    - most flexibility, reduce cost by up to 66%
    - automatically applies to EC2, fargate, and lambda services regardless of instance family, size, AZ, region, OS, or tenancy.
  - `EC2 Instances`
    - lowest prices, 72% savings
    - commitment to usage of instance families in a region
    - automatically reduces your cost on the selected instance family in that region regardless of AZ, size, OS or tenancy
  - `SageMaker`
    - helps reduce sagemaker costs by up to 64%

# Identity

## Zero-Trust Model
`trust no one, verify everything`

In the zero trust model, identity becomes the primary security perimeter.
- first line of defense

Network Centric - focused on VPN's and firewalls
Identity Centric - persons scope of access limited by there identity

## Zero-Trust Model on AWS
Identity and Access Management (IAM)
- `IAM Polices`: set of permissions detailing a users access to services
- `Permission Boundaries`: what permission someone should not have
- `Service Control Polices`: Organization-wide permissions
- `IAM Policy Conditions`: more fine grain control of policy

AWS does not have ready-to-use identity controls that are intelligent, which is why AWS is considered to not have a true Zero Trust offering for customers, and third-party services need to be used.

A collection of AWS Services can be setup to intelligent-ish detection of identity concerns but requires expert knowledge
- `AWS CloudTrail`: track all API Calls
- `Amazon GuardDuty`: detect suspicious activity based on CloudTrail and other logs
- `Amazon Detective`: investigate and quickly identify security issues, an ingest data from GuardDuty

Third Party Services:
- Azure Active Directory (Azure AD)
- Google BeyondCorp
- JumpCloud

## Directory Service
A directory service maps the names of network resources to their network addresses.
- shared information infrastructure for locating, managing, administering, and organizing resources
  - volumes, folders, files, users, groups...

A directory server is a server that provides a directory service.
- each resource on the network is considered an object by the directory server
- information about a particular resource is stored as a collection of attributes associated with that resource or object

## Identity Providers (IdP)
A system that creates, maintains, and manages information for principals and also provides authentication services to applications within a federated or distributed network.
- A trusted provider of your user identity that lets you use to authenticate to access other services
- Federated identity is a method of linking a user's identity across multiple separate identity management systems​

- `OpenID`
  - open standard and decentralized `authentication` protocol
  - allows you to login into different social media platforms using a google or facebook account
  - *who you are*
- `OAuth2.0`
  - uses `authorization` tokens to prove an identity between consumers and a service provider
  - *grant access to functionality*
- `Security Assertion Markup Language (SAML)`
  - open standard for authentication and authorization between an identity provider and a service provider
  - *single-sign-on*

## Single Sign On
An authentication scheme that allows a user to log in with a single ID and password to different systems and software

## Lightweight Directory Access Protocol (LDAP)
An open, vender-neutral, industry standard application protocol for accessing and maintaining distributed directory information services over an internet protocol (IP)
- provide a central place to store usernames and passwords
- enables same-sign-on
  - allows the same userID and password to be used for multiple applications, but they have to enter it in every time they want to login.​

Why use LDAP when SSO is more convenient?​
- Most SSO systems are using LDAP.​
- LDAP was not designed natively to work with web applications.​
- Some systems only support integration with LDAP and not SSO​

## Multi-Factor Authentication
A security control where after you fill in your username and password, you have to use a second device such as a phone to confirm that it's you logging in.

## Security Keys
A secondary device that can be used during multi-factor authentication. Resembling a memory stick with a button, that when pressed will autofill a security token.

## AWS Identity and Access Management (IAM)
Allows you to create and manages AWS users and groups, and use permissions to allow and deny their access to AWS resources.

- `IAM policies`
  - document that grant permissions for a specific user, group, or role to access services
  - attached to IAM identities
- `IAM Permission`
  - the API actions that can or cannot be performed
  - represented in the IAM policy document
- `IAM Users`
  - End users who interact with aws resources
- `IAM Groups`
  - Group of users that share same permissions
- `IAM Roles`
  - grant aws resources permissions to specific aws API actions
  - associate policies to a role and the assign it to an aws resource

## Anatomy of an IAM Policy
IAM Policies are written in JSON, and contain the permissions which determine what API actions are allowed or denied.

- `Version of policy language`
  - 2012-10-17 is the latest version
- `Statement Container`
  - for policy element, allowed to have multiple
- `Sid`
  - a way to label your statements
- `Effect`
  - whether the policy will Allow or Deny
- `Action`
  - list of actions that the policy allows or denies
- `Principal`
  - account, user, or role which would like to allow or deny access
- `resource`
  - the resource to which the actions apply
- `condition`
  - circumstances under which the policy grants permission

## Principle of Least Privilege (PoLP)
Computer security concept of providing a usr, role, or application the least amount of permissions to perform an operation or action

- `Just-Enough-Access (JEA)`
  - permitting only the exact actions for the identity to perform its task
- `Just-In-Time (JIT)`
  - permitting smallest length of duration an identity can  use permissions

## AWS Account Root User
- `AWS Account`
  - the account which holds all your aws resources
- `Root User`
  - special account that cannot be deleted
- `User`
  - a user for common tasks that are assigned permissions

Root Users can:
- change account settings
- close aws account
- change or cancel aws support plan

## AWS SSO
AWS Single Sign-On (AWS SSO) is where you create or connect, your workforce identities in AWS once and manage access centrally across your AWS organization.

Choose your Identity Source
- AWS SSO, Active Directory, SAML 2.0 IdP
Managed User Permissions Centrally
- AWS Account, AWS Applications, SAML Applications

Uses get Single Click Access

# Application Integration
The process of letting two independent applications to communicate and work with each other.
- commonly facilitated by an intermediate system

## Queueing and Simple Queue Service (SQS)

- Simple Queue Service (SQS)
  - Used to provide asynchronous communication and decouple processes via messages/events.
  - delete messages once they are consumed
  - not real time
  - have to pull
  - simple communication
  - fully managed queuing service that enables you to decouple and scale microservice's, distributed systems, and serverless applications

## Streaming and Kinesis

- Amazon Kinesis
  - events live in the stream for long periods of time, so complex operations can be applied
  - real time
  - fully managed solution for collecting, processing, and analyzing streaming data in the cloud

## Pub-Sub and SNS
Publish-Subscribe pattern commonly implemented in messaging systems.

- Simple Notification Service (SNS)
- Publishers send their messages to an event bus
- event bus categorizes the messages into groups
- receivers subscribe to the groups
- messages are sent to subscribers

## API Gateway

- Amazon API Gateway is a solution for creating secure APIs in your cloud environment at any scale.
  - A program that sits between a single-entry point and multiple backends.
  - Allows for throttling, logging, routing logic or formatting of the request and responses
  - Create APIs that act as a front door for applications to access data, business logic, or functionality from back-end services.

## State Machines
An abstract model which decides how one state moves to another based on a series of conditions.

- AWS Step Functions
  - coordinate multiple aws services into a serverless workflow
  - a graphical console to visualize the components of your application as a series of steps
  - automatically triggers and tracks each step, and retries when there are errors, so your application executes in order and as expected
  - logs the state of each step, so when things go wrong you can diagnose and debug problem quickly

## Event Bus
Receives events from a source and routes events to a target based on rules.

- EventBridge
  - serverless event bus service that is used for application integration by streaming real-time data to you applications
  - types
    - default event bus for every account
    - custom event bus, scoped to multiple accounts or other aws accounts
    - SaaS event bus, scoped to third party SaaS providers
  - producers: aws services that emit events
  - partner sources: third party apps that can emit events
  - rules: define what event to capture and pass to targets
  - targets: aws services that consume events
  - events: data emitted by services, JSON objects

## Other Application Integration Services
- Amazon MQ
  -  is a managed message broker service that uses Apache ActiveMQ
-  Managed Kafka Service (MSK) 
   -  fully managed Apache Kafka service
   -  for building real-time streaming data pipelines and applications. Similar to Kinesis but more robust
-  AppSync 
   -  fully managed GraphQL service

# Containers

## VM's vs Containers
VMS do not make the best use of space. 
- apps are not isolated which could cause config conflicts, security problems, or resource hogging

Containers allow you to run multiple apps which are virtually isolated from each other
- configure os and dependencies per container

## Micro-services
- `Monolithic architecture`
  - one app which is responsible for everything
  - functionality is tightly coupled
- `Micro-services architecture`
  - multiple apps, each responsible for one thing
  - functionality is isolated and stateless

## Kubernetes (K8's)
Open source container orchestration system for automating deployment, scaling, and management of containers.
- advantage of kubernetes over docker is the ability to run containers distributed across multiple VM's
- ideally for micro-service architectures where a company has `tens to hundreds of services` they need to manage
- a unique component of kuberneetes are `pods`
  - a pod is a group of one or more containers with shared storage, network resources, and other shared settings

## Docker
PaaS product that use OS-level virtualization to deliver software in packages called containers.
- `dokcer cli`: cli commands to download, upload, build, run, and debug containers
- `dockerfile`: a configuration file on how to provision a container
- `docker compose`: tool and configuration file when working with multiple containers
- `docker swarm`: orchestration tool for managing deployed multi-container architectures
- `dockerhub`: public online repository for containers published by the community for download
- `The Open Container Initiative (OCI)`:  an open governance structure for creating open industry standards around container formats and runtime.

Podman, Buildah and Skopeo
- `podman`: is a container engine that is OCI-compliant and is a deopin replacement for docker
  - daemon-less, allows you to create pods like K8
- `buildah`: is a tool used to build OCI images
- `Skopeo`: tool for moving container images between different types of container storages

## Container Services

Primary Services:
- `Elastic Container Service (ECS)`
  - no cold starts
  - self managed EC2
- `AWS Fargate`
  - more robust than lambda
  - scale to zero cost
  - aws managed EC2
- `Elastic Kubernetes Service (EKS)`
  - open source, avoid vendor lock-in
- `AWS Lambda`
  - only think about code
  - short running tasks
  - can deploy custom containers

Provisioning and Deployment
- `Elastic Beanstalk (EB)`
  - ECS on training wheels, PaaS
- `App Runner`
  - PaaS specifically for containers
- `AWS Copilot CLI`
  - build, release, and operate production ready containerized applications on aws app runner, ECS, and aws Fargate

Supporting Services
- `Elastic Container Registry (ECR)`
  - repos for your docer images
- `X-Ray`
  - analyze and debug between micro-services
- `Step Functions`
  - stitch together lambdas and ECS tasks

# Governance

## Organizations and Accounts

- `Organizations`
  - allow the creation of new aws accounts, centrally managed billing, control access, compliance, security, and shared resources across your aws accounts
- `Root Account User`
  - a single sign-in identity that has complete access to all aws services and resources in an account
- `Organization Units`
  - a group of aws accounts within an organization which can also contain other organization units, creating a hierarchy
- `Service Control Policy`
  - control over the allowed permission for all accounts within an organization


Key Points
- more than one account managed through a single account using Organizations
- setup consolidated billing where 1 account pays the AWS bill for all
- create isolated AWS accounts for different teams under the payer account - and place them inside Organizational Units (OU)
  - allows you to set customized permission boundaries on the accounts using Service Control Policies (SCPs)

## AWS Control Tower
Helps enterprises quickly set-up a secure, aws multi-account.

- `Landing Zones`
  - baseline environment following best practice to quickly start production ready workloads
- `Account Factory`
  - automates provisioning of new accounts in your organization
  - standardize the provisioning of new accounts with pre-approved account configurations
- `Guardrails`
  - pre-packaged governance rules for security, operations, and compliance that can be applied to enter-prise wide or to specific groups

## AWS Config
Compliance as Code (CaC) framework that allows us to manage change in aws accounts on a per region basis
- change management is a formal process to
  - monitor changes
  - enforce changes
  - remediate changes

`AWS Config`
- ensure a resource is configured a certain way
- keep track of configuration changes
- list of all resources in a region

## AWS Quick Starts
Prebuilt templates by aws and aws partners to help deploy stacks
- reference architecture for deployment
- aws cloudformation templates that automate and configure the deployment
- a deployment and implementation guide

## Tagging
A key and value pair that you can assign to aws resources. Can be used to organize resources:
- resource management
- cost management
- operations management
- security
- governance and regulatory compliance

## Resource Groups
A collection of resources that share one or more tags
- Helps you organize and consolidate information based on your project and the resources that you use.
- Resource Groups can display details about a group of resource based on
  - Metrics
  - Alarms 
  - Configuration Settings

Resource Groups appears in the Global Console Header and Under Systems Manager

## Business Centric Services
-` Amazon Connect`
  - virtual call center
- `WorkSpaces`
  - virtual remote desktop service
- `WorkDocs`
  - shared collaboration service
- `Chime`
  - platform for online meetings
- `WorkMail` 
  - - Managed business email, contacts, and calendar service with support for existing desktop and mobile email client applications
- `Pinpoint`
  - Marketing campaign management system you can use for sending targeted email, SMS, push notifications, and voice messages.
- `Simple Email Service`
  - email sending service designed fro marketers and application developers to send marketing, notifications, and emails.
- `QuickSight`
  -  A Business Intelligence (BI) service. Connect multiple datasource and quickly visualize data in the form of graphs

# Provisioning
The allocation or creation of resources and services to a customer.

## Provisioning Services
- `Elastic Beanstalk `
  -  an easy-to-use service for deploying and scaling web applications
- `OpWorks` 
  - configuration management service that provides managed instances of Chef and Puppet
- `CloudFormation` 
  - lets you deploy your cloud resources using infrastructure-as-code with JSON and YAML templates
- `AWS QuickStarts `
  - pre-made packages that can launch and configure your AWS compute, network, storage, and other services
- `AWS Marketplace `
  - a digital catalogue containing thousands of software listings
- `AWS Amplify `
  - is a mobile and web application framework, that will provision multiple AWS services as your backend.​
- `AWS App Runner `
  - a fully managed service that makes it easy for developers to quickly deploy containerized web applications and APIs
- `AWS Copilot` 
  - AWS Copilot is a command-line interface (CLI) that enables customers to quickly launch and easily manage containerized applications on AWS
- `AWS CodeStar` 
  - provides a unified user interface, enabling you to easily manage your software development activities in one place
- `AWS Cloud Development Kit (CDK)`
  - an Infrastructure as Code (IaC) tool.

## AWS Elastic Beanstalk
PaaS allowing customer to develop, run, and manage applications without the complexity of building and maintaining the infrastructure
-  powered by a `CloudFormation` template and setups
  - Elastic Load Balancer
  - Autoscaling Groups
  - RDS Database
  - EC2 Instance preconfigured (or custom ) platforms
  - Monitoring (CloudWatch, SNS)
  - In-Place and Blue/Green deployment methodologies
  - Security (Rotates passwords)
  - Can run Dockerized environments

# Serverless Services
Serverless architecture generally describes fully managed cloud services.

A serverless service could have all or most of the following characteristics:
- Highly elastic and scalable
- Highly available
- Highly durable
- Secure by default

Abstracts away the underlying infrastructure and are billed based on the execution of your business task.

Serverless can Scale-to-Zero meaning when not in use the serverless resources cost nothing.

- `DynamoDB` 
  - is a serverless NoSQL key/value and document database
- `Simple Storage Service (S3) `
  - is a serverless object storage service.
- `ECS Fargate `
  - is serverless orchestration container service.
- `AWS Lambda`
  - is a serverless functions service. 
- `Step Functions `
  - is a state machine service
- `Aurora Serverless`
  - is the serverless on-demand version of Aurora.

# Windows on AWS

- `Windows Servers on EC2`
- `SQL Server on RDS`
- `AWS Directory Service `
  - lets you run Microsoft Active Directory (AD) as a managed service​
- `AWS License Manager `
  - makes it easier to manage your software licenses from software vendors such as Microsoft.​
- `Amazon FSx for Windows File Server `
  - is a fully managed scalable storage built for Windows.​
- `AWS Software Development Kit (SDK)`
  - has .NET support
- `Amazon WorkSpaces `
  - allows you to run a Windows virtual desktop
- `AWS Migration Acceleration Program (MAP)`
  - migration methodology from moving large enterprise

# Logging
- `CloudTrail`
  - logs all api calls between various aws services
  - used to answer questions of who created/launched/configured a 
    - `Where` : Source IP Address
    - `When` : EventTime
    - `Who` : User, UserAgent
    - `What` : Region, Resource, Actionresources
  - Trails are output to S3 and do not have GUI like Event History. To analyze a Trail you’d have to use Amazon Athena.
- `CloudWatch`
  - a collection of multiple resources
  - `logs`: performance data about aws services
  - `metrics`: time-ordered set of data points for monitoring purposes
    - It's a variable that is monitored over time.
  - `events`: trigger an event based ona  condition
  - `alarms`: trigger notifications based on metrics
    - Metric Alarm States
    - `OK` The metric or expression is within the defined threshold
    - `ALARM` The metric or expression is outside of the defined threshold
    - `INSUFFICIENT_DATA`
  - `dashboard`: visualize metrics
- `AWS X-Ray`
  - distributed tracing system
  - see how data moves from one app to another, how long it takes to moves, and if failed to move forward

## Anatomy of an Alarm
- `threshold condition` : defines when a data point is breached
- `evaluation periods` : number of previous periods
- `data point` : metrics measurement at a given time period
- `metric` : data that is being measured
- `period` : how often alarm is evaluated
- `networkin` : volume of incoming network traffic
- `datapoints` to alarm : "1 data point is breached in an evaluation period going back 4 periods."

## CloudWatch Logs — Log Streams
- `log stream` :  represents a sequence of events from an application or instance being monitored.

- `log Events` : a single event in a log file. Log events can be seen within a Log Stream.

## Log Insights
Enables you interactively search and analyze cloudwatch data
- more robust filtering than log streams
- less burdensome than having to export logs to s3 an analyze them with athena
- has it's own language `Query Syntax`