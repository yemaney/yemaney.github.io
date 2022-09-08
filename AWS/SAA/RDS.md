# Relation Database Service (RDS)

## Database Refresher and  Models

- `Relational`
  - use Structured Query Language (SQL)
  - `rigid schema` : structure in and between tables of data
    - defined in advance
    - difficult to use for data that has rapidly changing relationships
  - table of rows, where each row has a unique primary key
  - relationship between tables
    - `composite key` : links to two tables which indirectly connects them



- `NoSQL`
  - not one single thing, many models
  - generally more relaxed schema
  - `Key-Value`
    - list of key value pairs
    - no real schema or tables
    - scalable since sections of the list can be split to different servers
    - really fast
    - in memory caching
  - `Wide Column Store (DynamoDB)`
    - two keys, partition and other key
    - can have multiple attributes, different items don't need to have the same attributes
  - `Document`
    - key : value, where the values are documents
    - documents usually json or xml format
    - ideal for interacting with whole documents or deep attribute interactions
  - `Column (Redshift)`
    - store data based on columns
    - really good at querying single columns for reporting and analytics
  - `Graph`
    - nodes and edges representing relationships
      - both can have key value pairs of data

## ACID v BASE

- database transaction models
- `cap theorem: (choose 2)`
  - `consistency` : every read to a database will get the most recent write or get an error
  - `availability` : every request will receive a non-error response, without the guarantee that you get the most recent write
  - `partition tolerant` : system can be made of multiple network partitions
- `acid : consistency`
  - transactions are : 
    - `atomic` : all or no components of a transaction succeeds or fails ex) banking transfers
    - `consistent` : transaction move database from one valid state to another, no in-between
    - `isolated` : concurrent transactions don't interfere with each other
    - `durable` : once committed, transactions are durable, stored on non-volatile memory
  - `RDS`
  - `limits scaling`
- `base : availability`
  - transactions are : 
    - `basically available` : read and write operations are available as much as possible without consistency guarantees
    - `soft state` : database doesn't enforce consistency, offloaded to application/user
    - `eventually` : if we wait long enough, reads from the system will be consistent
  - `highly scalable`
  - `nosql`

## Databases on EC2

- `usually a bad idea`
  - `admin overhead` : managing ec2 and dbhost
  - backup / DR management / replication
  - ec2 runs in a single AZ
  - missing features aws db products have, performance
  - on or off, not serverless, no easy scaling

- `putting database in an ec2 introduces dependency`
  - need reliable communication between application and database ec2
  - cost for data transferring across different AZ

`justifications`
- access to the db instance OS
- advanced db option tuning
- db or db version aws doesn't support
- specific os/db combination aws doesn't provide
- architecture aws doesn't provide

## Relational Database Service (RDS)

- Database-as-a-service (DBaas)
  - managed database instance (1 or more databases)
- multiple engines MySQL, MAriaDB, PostgreSQL, Oracle, Microsoft SQL Server
- Amazon Aurora

Architecture
- RDS Database Instance
  - use same tooling as engine to access
  - has one attached block storage in the same AZ as the instance
    - io1, gp2, magetic
  - billed for the instance (cpu/memory) and for the storage GB/month
  - access to to rds instance is controlled by its associated security group

- create a subnet group
  - inform which subnets to place rds instances into

## RDS Multi AZ

- secondary hardware is allocated in another AZ (standby replica)
- access database using cname, which points to primary rds
- `Synchronous Replication`
  - database writes directed at primary database cname
    - which writes changes to it's storage
  - changes immediately replicated across to standby replica
    - standby writes changes to it's storage
  - almost zero lag, as replication occurs as data is being written to primary database
- if error occurs with primary database
  - rds changes the database endpoint cname to the standby replica

- gives `high availability`, but not fault tolerance
- not available for free tier
- standby can't be directly used, doesn't increase performance
- `60-120` seconds failover
- `same region` only, work with other AZs in the VPC
- `backups are taken from standby`, (removes performance impact)
- failure reasons : az outage, primary failure, manual failure, instance type change, software patching

## RDS Backups and Restores


`Recovery Point Objective (RPO)`
- time between last backup and the point a failure occurred
  - maximum data loss possible
- influences technical solution and cost : 
  - lower rpo -> HIGHER COST

`Recovery Time Objective (RTO)`
- time between a failure and when system is return to service
- influenced by process, staff, tech, and documentation
- generally lower values cost more

RDS is capable of performing Manual Snapshots and Automatic backups
- both use aws managed s3 buckets that aren't visible to user
- gives region resilience
- first snapshot is full, then onwards incremental
- can affect performance of single instance, but if using multi-az used on standby
- `Manual Snapshots` : live forever
- `Automatic Backups` : configure how often it occurs
  - `every five minutes, database transactions logs are written to s3`
    - the actual data that changes in the database
    - database can be restored back in time within a 5 minute granularity
      - `RPO = 5 minutes`
    - database snapshot is restored, then the transaction logs are replayed over the top of the snapshot
  - are not retained indefinitely, automatically cleaned up
    - 0-35 day retention period
  - can retain automated backups after deleting rds instance, but they will still expire
    - must take manual snapshot

`RDS Restores`
- creates a `new rds instance with new address`
  - will have to update application that use the database endpoint address
- restoring using snapshots restores to single point in time

## RDS READ-Replicas

- RDS Read Replicas can be added to an RDS Instance - `5 direct per primary instance`.
  - each providing an additional instance of read performance
    - ie) make applications used replicas for read operations
- offers `low RTO recovery` for any instance failure issues
  - replicas can be promoted to a primary quickly
  - don't help with data corruption as the corruption will be replicated to the RR.
- like another RDS instance, has its `own address`
- asynchronous replication form primary to read replica
- can be in the `same region, or cross-region replicas`.
  - `global ` performance improvements
- read replicas can have read replicas, but lag start to be a problem

## RDS Data Security

- authentication : how users can log in to rds
  - can configure RDS to allow iam authentication
    - create RDS `local DB account` configured to use `aws authentication token`
    - policy attached to users or roles maps that iam identity onto the local RDS user
    - `generate-db-auth-token` for `15 mins`
- authorization : how access is controlled
- encryption in transit : between client and rds
  - SSL/TLS, can be `mandatory`
- encryption at rest : how data is protect when it is written to disk
  - default : EBS volume encryption with KMS
    - `handled by RDS HOST/EBS`
    - CMK generates data keys used for encryption operations
    - `storage, logs, snapshots, and replicas are encrypted`
    - `can't be removed` once added
  - MSSQL and ORACLE support Transparent Data Encryption (`TDE`)
    - encryption handled within the DB engine, `ie encrypted before leaving the instance`
    - ORACLE supports integration with CloudHSM
      - stronger key controls

## Aurora Architecture

- uses a `cluster`
  - made of a single `primary` instance and `0 or more replicas`
  - replicas can be used for reads during normal operation
    - provide availability and read scalability
- no local storage : uses `cluster volume`
  - shared and available to all compute instances within a cluster 
    - faster provision, improved availability and performance
  - data written to primary disk, `aurora synchronously replicates` the data across 6 replicas in 3 AZs
  - `aurora automatically detects failures` in disk volumes of shared storage
    - when segment fails, aurora `immediately repairs using data inside other storage nodes`
    - avoids data loss and reduces any need for snapshot restores
  - `Up to 15 replicas`, that can be assigned to failover operations
    - instances can be added without requiring storage provisioning
  - `All SSD Based - high IOPS, low latency`
  - Don't specify storage, `billed on what's used`, for the most used
    - create new cluster and migrate data to reduce costs
- `Cluster Endpoint`
  - points at primary instance
  - can be used for read and write operations
- `Reader Endpoint`
  - load balances across all available replicas
  - used for read operations, easier reader scaling
- `Custom Endpoint`
  - can create custom endpoints
- `individual endpoints`
  - each instance (primary or replica) has its own endpoint
- `Costs`
  - no free-tier option
    - doesn't support micro instances
  - beyond rds single az, aurora offers better value
  - compute : hourly charge per second, 10 minute min
  - storage : GB-Month consumed, IO costs per request
  - 100% DB Size in backups are included
- `Backups`
  - work in aurora in the same ay as RDS
  - restores create a new cluster
  - `backtrack` can be used which allow `in-place rewinds` to previous point in time
  - `fast clone` : makes a new databases `MUCH` faster than copying all the data
    - only stores differences of data that changed in the clone or the original

## Aurora Serverless

- removes the admin overhead of managing individual instances
- scalable `Aurora Capacity UnitsACU`
  - allocated from a shared pool managed by aws
  - represent an amount of compute and memory
  - can set `min and max` acu values
  - can go to `0 and be paused`
- billed per-second basis
- same resilience as aurora, 6 replicas across AZs
- requests go to a hidden layer `proxy fleet` managed by aws
  - which broker connection with acu
  - allows for seamless scaling
- `Use cases`
  - infrequently used application
  - new applications
  - variable workloads
  - unpredictable workloads
  - development and test databases
  - multi-tenant applications  (scaling is aligned between infrastructure size and revenue )
