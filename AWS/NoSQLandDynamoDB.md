## DynamoDB

### Architecture

- nosql : `key/value & document`
- `Public` database-as-a-service
- `fully managed`
- scaling options
  - `manual`
  - `automatic`
  - `on-demand`
    - cost per interaction
  - `capacity`
      - write capacity unites (`WCU`)
        - 1 WCU -> 1KB per second
      - read capacity unites (`RCU`)
        - 1RCU -> 4KB per second
- `highly resilient`
  - across `AZs`
  - optionally : `global`
- `Really fast`, single-digit milliseconds (SSD Based)
- supports backups, point in time recovery, encryption at rest

- `Tables`
  - grouping of items with the same primary key
  - `primary key` :
    - `simple` : partition key
    - `composite` : partition key + sort key
  - item max `400kb`
  - item can have one, all, mixture, or different attributes

- `Backups`
  - on-demand : full copy of table retained until removed
    - migrate data
    - restore with or without indexes
    - adjust encryption settings
  - `point-in-time-recovery (PITR)`
    - continuous record of changes
    - 35 day recovery window
    - 1 second granularity

- considerations :
  - nosql or key/value : preference for ddb

## Operations, Consistency and Performance

- `Capacity Provisioning`
  - 1RCU -> 4KB per second
  - 1 WCU -> 1KB per second
    - can only write to leader node, scale less, so more expensive than RCU
  - every tables has a RCU and WCU burst pool
    - 300 seconds
  - `On-Demand`
    - for unknown or unpredictable load
    - low admin
    - cost:
      - charged per million R/W units
  - `Provisioned`
    - set RCU and WCU on a per table basis
      - every operations consumes at least 1 RCU/WCU
    - cost : cheaper than on-demand

- `Operations`
  - `Query`
    - can return 0 or more items
    - capacity consumed is the size of all returned items
    - filter discards attribute data , but still consumes it
    - can only query on PK or PK + SK
  - `Scan`
    - least efficient, more flexible
    - scans through entire table, consumes capacity for every item
    - can scan for any attribute besides PK/SK

- `Consistency`
  - do transactions started in the future necessarily see the effects of other transactions committed in the past
  - ddb data is replicated across storage nodes in different AZs
  - writes are directed at the leader node
    - then data is replicated to other nodes
  - `eventually consistent read`
    - reads direct to one of the storage node
    - not guaranteed to get latest data
    - scales better since can use any node
    - lower price
  - `strongly consistent read`
    - reads directed to only the leader node

- Calculation
  - WCU Calculation
    - roundup(item size / 1KB) * (number per second)
  - RCU Calculation
    - roundup(item size / 4KB) * (number per second)

## Local and Global Secondary Indexes

- a way to improve efficiency of data retrieval
- provide an alternative view on table data
- attribute propagation : all, keys_only, or include others
  - projecting uses capacity
- indexes are sparse : only items that have values in new PK/PK+SK are added

- `LSI`
  - use for `strong consistency`
  - must be created with a table
  - 5 LSI's per base tables
  - alternative `SK` on the table
  - `share the capacity` (RUC/WCU) with table

- `GSI`
  - use as `default`
  - can be created at any time
  - default limit of 20 per base table
  - alternative `PK` and `SK`
  - `have their own capacity` (RCU/WCU) allocations
  - `eventually consistent`,asynchronous replication

## Streams & Lambda Triggers

- `stream`
  - time ordered list of item changes in a table
     - `inserts, updates, and deletes`
  - `24 hour` rolling window
  - enabled on per table basis
  - `view types`
    - keys only
    - new image
    - old image
    - new and old image

- `Lambda Triggers`
  - Lambda can be integrated to provide trigger functionality 
  - invoking when new entries are added on the stream.

## Global Tables

- provide `multi-master cross-region replication`
  - can re`ad and write to any region and replica`
  - generally `sub-second replication` between regions
- `steps`
  - create tables in multiple regions
  - then add them all to the same global table 
- `last writer wins` is used for conflict resolution
- globally eventually consistent
  - strongly consistent reads only in the same region as writes
- provides `global HA`, Global DR/BC

## Accelerator (DAX)

- `in-memory cache` that improves performance
  - `faster`
  - `can reduce costs`
- application uses dax sdk and makes  a single call for data
  - dax either returns data from cache or from database
- `directly integrated with ddb`
  - `less complexity` and admin overhead
- runs in `VPC`
  - `deploy nodes across AZ for HA`
  - data replicated from primary node across replica nodes
  - endpoint load balances across cluster nodes
- `caches`
  - `item cache`
    - holds items from (Batch)GetItem call
  - `query cache`
    - holds data based on query/scan parameters
- can scale `up` and `out`
- supports `write-through`
  - can write to ddb using dax sdk
- eventually consistent
- good for read heavy operation

## Athena

- serverless query service
- ad-hoc query on data stored in s3
- pay only for data consumed

- flow
  - data stored in s3
    - unstructured, semi-structured, or structured
  - define schema
    - define how to get original source data to a table structure
  - data is projected through the schema when read
- allows sql-like queries
- output can be sent to other services

## ElastiCache

- in-memory databases
  - high performance
  - not persistent
- engines
  - `Redis`
    - advanced structures
    - multi AZ
    - back up and restore
    - transactions : improve consistency
  - `Memcached`
    - simple data structures
    - no replicated
    - no backups
    - multi-threaded
- `uses case`
  - used to cache data
  - for `read heavy workloads` with low latency requirements
  - `reduces database workloads and costs`
  - `store session data` for stateless servers
- requires application code changes

## Redshift

- `petabyte-scale data warehouse`
- design for reporting and analytics
- `OLAP` (`column` based)
- pay as you use
- redshift spectrum : direct query s3
- federated query : direct query other DBs
- sql-like interface (`JDBC/ODBC`) connections
- server based (not serverless)
  - takes time to provision, so no for adhoc queries like athena
- `integration`
  - copy data from `dynamodb`
  - `DMS` migrate from db
  - stream using `kinesis firehose`
- `One AZ` in a `VPC` : `not HA`
  - data is replicated to 1 additional node
  - `automatic snapshot` to s3 (8hrs/5GB)
    - 1-35 day retention
  - `manual snapshots` to s3
  - `snapshots can be migrated across regions`
- leader node : query input, planning and aggregation
  - manages distributing data to node slices
- compute node : perform queries of data
- `enhanced vpc routing`
  - advanced networking control
  - by default public routes are used for external sources like S3
  - allows traffic routing using vpc configuration

