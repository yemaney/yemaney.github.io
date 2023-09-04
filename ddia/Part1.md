# Foundations of Data Systems

- an application has to meet two types of requirements in order to be useful
  - `functional` : what it does
  - `non functional` : general properties like reliability, scalability, maintainability

## 1. Reliable, Scalable, and Maintainable Applications

### Reliability

- system should work even when faced with faults and prevent failures from ocurring
  - `fault`: one component of system deviates from its spec
  - `failure`: entire system stops providing service

`hardware faults`:
- add redundancy to hardware components
- use fault-tolerannt software to tolerate loss of entire machines

`software errors`
- tend to cause more issues since software is shared accross nodes
- think about assumptions, testing, isolate processes, allow process to crash and restart,  monitor system in production

`human errors`
- design systems to minimize opportunites for error
  - don't make to limiting as people will try to get around it
- decouple place where people make mistakes from where they can cause failures
  - sandbox environments
- test thoroughly: unit tests, system wide integration tetss, manual tests
- make it fast to roll back configuration changes

### Scalability

- systems ability to cope with increased load
- depends on system architecture. load can be volume of reads, volume of writes, volume of data to store, complexity of data, response times, access patterns

`describing load`
- `load parameters` depends on architecture of system: requests per second, reads and writes to database, number of simulatneous users
- focus on average case vs bottleneck cases

`describe performance`
- when load parameter is increased and system resources are unchanged, how is performance affected
- when you increase a load parameter, how much do you need to increase the resources to keep performance unchanged
- `reponse time`: what client sees. inclues service time, network delays, queing delays etc.
- `latency` : time requests is waiting to be handled
- use `percentiles` to understand median performance, and outliers
- queing delays account for a large part of the reponse time at high percentiles
  - `head of line blocking`: early slow request delay others behind in queue. which is why it's important to measure response times on the client side
  - or when several backend calls are required to serve a single request

`approaches for coping with load`
- `scaling up / verical scaling`: moving to a more powerful machine
  - common wisodom to scale databases up for simplicity
- `scaling out / horizontal scaling`: distubuting the load across multiple smaller machines, also known as *shared-nothing*
  - `elastic`: can automatically add computing resources  when load increases.

### Maintainability
- it should be reasonable to expect different people can work on the system productively 

- majority of cost of software is ongoing maintenence
- `operability`: make it easy to keep the system running smoothly
  - good visibility into systems health
- `simplicity`: make it easy for new engineers to understand
  - complexity increases risk of bugs by hiding assumptions, unintedned consequences, and unexpected interactions
  - `abstractions`: can hide implementation detail
- `evolvability`: make it easy to make changes to the system in the future

## 2. Data Models and Query Languages

- application are built by layering data models
  - objects/data structures > JSON/XML > bytes in memory/disk/network > electrical currents
- data models embody assumptions about how it is going to be used
  - some usage are easy and some are not supported; some operations are fast and some perform badly
-  One model can be emulated in terms of another model, but the result is often awkward.
   -  different systems for different purposes, not a single one-size-fits-all solution.
- schemas can either be explicit (enforced on write) or implicit (handled on read)

### Relational Model Versus Document Model

`Models`
- `hierarchal model`
  - represented all data as a tree of records nested within records
  - not good for representing many-to-many relationships
- `network model`
  - record could have multiple parents
    - ex: one record for a location which is linked to many users, allowing many to one and many to many
  - many access paths, became cumbersome, updating code for querying and updating the database complicated and inflexible
- `relational model`
  - all data in a relation (table) made of up of rows
  - no complicated access paths, query optimizer decides optimal path
- `document model`
  - similar storage as hierarchal model, with data in JSON
  - greater scalability than relational, very large datasets or very high write throughput

`Comparison`

|     | Relational | Document |
| --- | ---------- | -------- |
|joins|better support for joins, many to one, and many to many relationships|joins not natively supported, work of joins shifted to application code, use document reference (unique identifier) to point to other documents and resolve using follow up queries |
|schema|schema enforced at write time, changes require migrations|schema-on-read approach (don't enforce any schema), more flexible, can immediately write new document structures and have application code handle variants|
|data locality|if getting document like data, requires access multiple different tables|can enjoy better data locality if application needs most of document since entire document will be loaded, since updates can require rewriting of entire document it is recommended to keep documents small| 
|Object-Relational Mismatch|require translation layer between objects in application code and the database model|JSON model in document databases is usually similar to objects in application code, resulting in easier translation| 

Extra
- Many-to-One and Many-to-Many Relationships
  - if a certain data is used by many different entities, it can make sense to store it as an ID
    - enforce consistency across entities
    - avoid ambiguity by making distinctions
    - localization support (for translation)
    - better search
    - ease of updating, as changes only has to happen in one place
      - less write overhead and inconsistencies
      - removing duplication helps normalization in databases

- convergence of document and relational databases
  - most relational databases support xml and json
  - some document databases support relational like joins

### Query Languages for Data

`imperative vs declarative`
  - `imperative`: tell computer to perform certain operations in a specific order
  - `declarative`: specify end goal but not how to get there
    - concise, easier to  use, hides implementation details, more room for optimization, lends itself to parallel execution which is hard for imperative
    - `SQL is declarative` 

- `map reduce querying`
  - programming model for processing large amounts of data in bulk across many machines
  - `in between declarative and imperative`
  -  logic of the query is expressed with snippets of code, which are called repeatedly by the processing framework

### Graph-Like Data Models

- graph made of two objects: `vertices/nodes and edges`

`Graph models`
- `property graphs`
  - each vertex consists of:
    - a unique identifier, set of outgoing edges, set of incoming edges, collection of properties (key-value pairs)
  - each edge consists of:
    - a unique identifier, vertex where it starts (tail), vertex where it ends (head), label describing the relationship between the two vertices, collection of properties (key-value pairs)

- `triple-stores`
  - mostly similar to property graph model
  - all information is stored in three part statement: `subject, predicate, object`
  - subject is a vertex
  - object can be either
    - a value in a primitive datatype such as string or number
      - in which case the predicate and object are the key value of property on the subject vertex
    - another vertex in the graph
      - in which case the predicate is and edge, the subject is the tail, and the object is the head


- `graph store`:
  - represent property graph using a relational schema 
  - two relational tables, one for vertices and one for edges
  - any vertex can have an edge connecting it with any other vertex (no schema restriction)
  - given any vertex you can efficiently find both its incoming and outgoing edges, and traverse the graph
  - can store different kinds of information using labels while still keeping a clean data model


`Querying`
- `cypher query language`
  - declarative query language for property graphs for Neo4j graph database
- `graph queries in sql`
  - can be done using the WITH RECURSIVE syntax to follow paths, but is difficult
- `sparql query language`
  - query language for triple-stores using the rdf data model
- `datalog`
  - query language of datomic
  - data model similar to triple store, writes a `predicate(subject, object)`
  - define rules that it uses to find data, less convenient for simple one off queries by copes better with complex data

`Comparison`

||Network Model|Graph Database|
|-|-|-|
|schema|had schema specifying which record type could be nested within other record type|no restrictions|
|access|traverse an access path to reach a record|refer directly to any vertex by unique id or use an index to find vertices with a particular value|
|order|data is ordered and database maintained ordering|no order|
|querying|imperative|support declarative|

## 3. Storage and Retrieval
- database should be able to do two things:
  - store data
  - give back data at a later time
- application developer should know how databases handle storage and retrieval of data
  - to make decision on what storage engine to use in your project
### Data Structures That Power Your Database
- `index`
  - an addition structure containing metadata about primary data to speed up reads
  - slows down writes, because the index will have to be updated every time data is written
  - application developer creates index depending on typical queries that are expected
#### Log Structured
- designed around the concept of many append-only log segment files
- new data and modifications are appended to a log file sequentially
- periodically `compact` and `merge`: to remove old duplicates of keys

`hash indexes`
  - in memory hash map where every key is mapped to the location where the value can be found
  - `crash recovery`: if database is restarted in memory hash maps are lost, store snapshot of each segments hash map on disk which can be loaded into memory more quickly
- `SSTables`
  - same log structure as hash index
  - `sorted string table sstable` : sort sequence of key-value pairs by key
  - range queries are more efficient since data is sorted
  - `merging` is more efficient : look at files side by side and copy lowest key
  - `save memory`: don't need to keep index of all keys in memory can use a `sparse index`
  - `save disk space and i/o bandwidth` : compress blocks that use same index key

`LSM-Trees`
  - log structured merge-tree
  - cascade of SSTables that are merged in the background
  - writes go to sorted in memory structure which is eventually written to disk

- `bloom filters` : tell you if keys appears in database, to avoid wasting time looking for non existent keys
#### Page-Oriented
- B-Trees are the most widely used index, standard index implementation in relational databases
- break database down into fix sized blocks/pages
  - each page can be identified using and address/location
  - one page is designated as the root of the b-tree
  - page contains several keys and references to child pages
  - each child is responsible for a continuous range of keys and references to their children nodes
- update: search for the leaf page containing the key, and change the value, write to disk
- adding: find page whose range encompasses the new key and add it to that page
- if there isn't enough space in page, then page is split into two half-full pages and parent is updated to account for new subdivision of key ranges

- `write-ahead log (WAL/redo log):` append-only file to which every B-tree modification must be written before it can be applied to the pages of the tree
  - used after crash to restore database to consistent state
#### Comparison
- `Log-Structured Storage Engines`
  - LSM-trees typically have `higher write throughput`
  - smaller files by merging produce smaller files, more read and write requests within the available I/O
  - compaction process can interfere with ongoing reads and writes and consumes bandwidth
  - growing number of unmerged segments can slow down reads
- `Page-Oriented Storage Engines`
  - B-Trees typically have faster reads
  - `Read Performance`: B-Tree structure reduces the number of disk accesses needed to locate data, faster reads
  - `Predictable Latency`: Random read times are relatively stable
  - fragmentation when page is split or when a row cannot fit into an existing page
#### Other Index Structures
`Storing values within the index`
- key in an index is the thing that queries search for, but the value can be one of two things
- `nonclustered index`
  - storing only references to the data within the index
  - avoids duplicating data when multiple secondary indexes are present: each index references a location in the heap file and the actual data is kept in one place
- `clustered index`
  - store all row data within the index
  - hop from the index to the heap file is too much of a performance penalty
- `covering index or index with included columns`
  - stores some of a table’s columns within the index
  - compromise between a clustered index and a nonclustered index
- clustered and covering indexes can speed up reads, but they require additional storage and can add overhead on writes

`Full-text search and fuzzy indexes`
- search for one word expands to include synonyms, ignore grammatical variations, and to search for occurrences of words near each other in the same document
- `Lucene` is able to search text for words within a certain edit distance

`Keeping everything in memory`
- `inmemory` databases
- performance boost comes from avoiding the overhead of encoding in-memory data structures in a form that can be written to disk 
- providing data models that are difficult to implement with disk-based indexes: priority queues and sets
- some intended for caching use only, where it's acceptable for data to be lost if a machine is restarted
- for persistence: write periodic snapshots to disk, or  replicate the in-memory state to other machines

### Transaction Processing or Analytics

- Online Transaction Processing (OLTP)
  - access pattern: look up, insert, update, small number of records based on users input
  - interactive
- Online Analytic Processing (OLAP)
  - access pattern: scan over a huge number of records, usually a few columns, calculate aggregate statistics


|Property|Online Transaction Processing (OLTP)|Online Analytic Processing (OLAP)|
|-|-|-|
|Read Pattern|small number of records per query, fetched by key|Aggregate over large number of records|
|Write Pattern|random-access, low latency writes from user input|Bulk import (ELT) or event stream|
|Used By|end user/customer, via web application|Internal analyst, for decision support|
|Data Represents|latest state of data|History of event over time|
|Dataset Size|Gigabytes to Terabytes|Terabytes to Petabytes|
|Bottleneck|Disk seek time|Disk bandwidth|

#### Data Warehousing

- Data Warehouse
  - database separate from the ones used for OLTP systems
  - analyst can query without affecting OLTP operations
  - contains read-only copy of data in all the various OLTP systems of company
  - data extracted from OLTP databases, transformed into analysis friendly schema, and then loaded into data warehouse (ELT)
  - data warehouse can be optimized for analytic access patterns
  - data model usually relational as SQL is good for analytics

#### Schemas For Analytics
- star schema (dimensional modeling)
  - fact table: each row represents an event that happened at some point in time, created by referencing a bunch of dimensional tables that give data about event
  - simple
- snowflake schema
  - dimensions are further broken down into sub-dimensions
  - more normalized

### Column-Oriented Storage

- row oriented : store all values from one row together
  - loads all attributes for each row before filtering
- column oriented: store all values from each column together
  - queries only loads required columns to save time

#### Column Compression

- column oriented storage lends itself well to compression, which reduces disk throughput demand by compressing data
  - number of distinct values in a column are small compared to number of rows
  - can use bitmap encoding

`Memory bandwidth and vectorized processing`
- column compression allows more rows from a column to fit in the same amount of L1 cache
- vectorized processing: operate on such chunks of compressed column data directly

#### Sort Order In Column Storage
- can impose an order for how the rows are stored
- data sorted entire row at a time, the key chosen based on common query
- a second column can be used to sort rows that have same value in first sort column
- helps with compression since sorting creates long sequences of repeating number if there isn't many distinct values

`Several different sort orders`
- redundantly store data sorted in different ways
- different queries benefit from different sort orders

#### Writing To Column-Oriented Storage
- read optimizations make writes a little more difficult
- like LSM-Tree, writes go to in memory sorted structure before being written to disk
- queries will have to examine both column data on disk and recent writes in memory

#### Aggregation: Data Cubes and Materialized Views
- data warehouse queries often involve an aggregate function, such as COUNT, SUM, AVG, MIN, or MAX in SQL
- materialized view: copy of the query results, written to disk
  - need to be updated when underlying data changes
  - updates make writes more expensive, make more sense in read heavy warehouse
- virtual view: shortcut for writing queries
  - SQL engine expands it into the view’s underlying query on the fly and then processes the expanded query
- data cube or OLAP cube: common special case of a materialized view
  - grid of aggregates grouped by different dimensions (example: SUM sales for each combination of date and product)
  - certain queries become very fast because they have effectively been precomputed
  - not as flexible as querying raw data: used to improve specific queries

### Summary

- OLTP: user facing, small queries, large volume of requests,  disk seek time is bottleneck
- OLAP: analyst facing, large queries, lower volume of requests, disk bandwidth is bottleneck
  - large number of rows, indexes are much less relevant.
  - becomes important to encode data very compactly, to minimize the amount of data
that the query needs to read from disk
- log-structure: append to files and delete obsolete files but never update in place
  - systematically turn random-access writes into sequential writes on disk to enable higher write throughput
  - Bitcask, SSTables, LSM-trees, LevelDB, Cassandra, HBase, Lucene
- page-oriented: treats the disk as a set of fixed-size pages that can be overwritten
  - BTrees, RDBMS
