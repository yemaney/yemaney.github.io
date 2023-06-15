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
