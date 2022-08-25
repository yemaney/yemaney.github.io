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
