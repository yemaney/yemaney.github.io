# Notes

## RDS

- can invoke a lambda function from an amazon `aurora` MySQL compatible edition db cluster with a `native function` or `stored procedure`
  - capture data changes
- rds events provide operation events such as
  - db instance events, db parameter group events, db security group events, and db snapshot events
- aurora serverless is an on-demand, auto-scaling configuration for amazon aurora
  - infrequent, intermittent, sporadic, or unpredictable workloads
- multi-az
  - synchronous replication
- enhanced monitoring
- can authenticate to db using IAM database authentication
  - MySQL and PostgreSQL

## CloudFront

- cf `signed-url` and `signed-cookies` allow you to control who can access your content
  - signed-urls
    - RTMP, restrict access to individual files, using a client that doesn't support cookies
  - signed cookies
    - provide access to multiple restricted files, don't wan to change urls

## Organization

- account management service

## ResourceAccessManager RAM

- enables you to easily and securely share aws resources with any aws account or within your organization


## ASG

- default termination policy
  - if multiple AZ, choose AZ with most instances
  - oldest launch configuration instance in AZ
  - closest to next billing hour
  - random

## EC2

- `cloudwatch agent`
  - install on ec2
  - memory, disk swap, disk space, page file utilization and log collection
  - view custom metrics in the cloudwatch console
- communicate across subnets
  - check network acl
  - check security group
- increase network availability
  - attach new eni to primary instance
  - if primary instance fails, attach new eni to secondary instance
- billing
  - charged when stopping to hibernate
  - charged when reserved instance is terminated
- stop and start : underlying host might change
- vCPU-based On-Demand Instance limit per region

# R53
- can route to EC2 using R53
- active-active
  - include all available resources
  - when you want maximum availability
- active-passive
  - primary, secondary resources


## ElastiCache

- authenticate users using redis auth
  - create new redis cluster with both `transit-encryption-enabled` and  `--auth-token` parameters enabled

## Lambda

- secure env variables
  - create new kms key and use it to enable encryption helpers

## S3

- versioning
  - prevent accidental deletes and overwriting
- object lock
  - write once read many
- access point
  - control who can access bucket
  - multi-region access point
    - use global accelerator
- Expedited retrievals allow you to quickly access your data when occasional urgent requests for a subset of archives are required
  - Provisioned capacity ensures that your retrieval capacity for expedited retrievals is available when you need it

## APIGW

- use throttling limits to protect backend systems and applications from traffic spikes
- can cache frequently accessed data

## ECS

- doesn't support resource based policy

## IAM

- can assign IAM role to users or groups from you AD once its integrated with your VPC via the aws directory service ad connector
- policy attached to roles/groups


## LB

- path-based routing, host-based routing, and bi-directional streaming using Remote Procedure Call (gRPC)
  - configure ALB with gRPC as protocol
- SNI
  - Upload all SSL certificates of the domains in the ALB using the console and bind multiple certificates to the same secure listener on your load balancer. ALB will automatically choose the optimal TLS certificate for each client using Server Name Indication (SNI).
  - host multiple TLS-secured applications, each with its own TLS certificate, behind a single load balancer.

## Config

- track all configuration changes

## DMS

- migrate databases, warehouses, nosql
- can replicate on going changes (change data capture CDC)
- supports SSL for security

## Proton

- deploy serverless or container-bases applications with increased efficiency
- can define infrastructure standards and cd pipelines
- can use components dev can add supplementary resources to applications before the standard template

## SNS

- use over SES for monitoring

## ASG

- default cooldown is 300sec

## GuardDuty

- used to find suspicious access patterns

## DataSync

- move large amounts of data online between on-premises storage and Amazon S3, Amazon Elastic File System (Amazon EFS), or Amazon FSx for Windows File Server

## KMS

- Unless the key policy explicitly allows it, you cannot use IAM policies to allow access to a KMS key

## AWS Backup

- centralized backup service that makes it easy and cost-effective for you to backup your application data across AWS services

## Fargate 

- 5GB ephemeral storage

## VPC

- ACL outbound connection use ephemeral port