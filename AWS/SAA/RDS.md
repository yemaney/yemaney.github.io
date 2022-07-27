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
