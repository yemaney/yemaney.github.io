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
