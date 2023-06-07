# Foundations of Data Systems

- an application has to meet two types of requirements in order to be useful
  - `functional` : what it does
  - `non functional` : general properties like reliability, scalability, maintainability

## Reliable, Scalable, and Maintainable Applications

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
