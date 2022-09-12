# High Availability and Scaling

## Regional and Global AWS Architecture

- `R53` (DNS Service)
  - `Global Service Location and Discovery`
    - how does your machine discover where to point at
  - `Global Health Checks and Failover`
    - detecting if infrastructure is healthy or not in a one location and moving customers to another Country as required
- `CloudFront`
  - `Content Delivery` (CDN) and optimization
    - how does content get to users globally : from distributed or central location
    - cache content globally as close to end user as possible to improve performance

![Architecture](./HighLevelDiagramOfAWSArchitecture.PNG)

- `web tier`
  - provide entry point to customer
  - abstracts internals away from customer
- `compute tier`
  - provide functionality for the customer
- `storage tier`
  - provide storage for compute infrastructure
- `cache tier`
  - faster data access by caching data
  - reduce db reads, to improve performance and reduce costs
- `db tier`
  - data storage
- `app service`
  - provide functionality to applications like queues, data streaming etc.

- `Regional Scaling and Resilience`

## Elastic Load Balancer Evolution

- 3 types of load balancers (ELB) available
  - split between between v1 (avoid) and v2(prefer)
- CLB (v1), lacking features, more expensive
- Application Load Balancer (ALB)
  - HTTP/S/WebSocket
- Network Load Balancer (NLB)
  - TCP/TLS/UDP
  - email, ssh
- v2 : faster, cheaper, support target groups and rules

## Elastic Load Balancer Architecture

- accept connections from customers and distribute them across any registered backend compute
- `abstracts user away from physical infrastructure`
  - means the amount of infrastructure can change without affecting customers
  - infrastructure can fail and be repaired, hidden from customers
- pick if using ipv4 only or ipv4 and ipv6
- pick which AZs the load balancer will use
  - `2 or more AZs`
  - `one subnet` per AZ
  - one load balancer is made up of `many nodes`
  - product places one or more load balancer nodes into the subnets
- load balancer created with a `DNS record` 
  - A record
  - `points to all of the ELB nodes` created with the product
  - incoming requests are `distributed equally across all the nodes`
  - nodes scale within the AZ
    - `HA` : if one fails it is replaced
    - if load increases, then addition nodes are provisioned
- `Internet facing `: have private and public IPs
- `Internal` : have only privates IPs
  - generally used to separate different tiers of applications
    - like web,app,db etc.
  - `allows tiers to scale independently of each other`
- Nodes are configured with `listeners`
  - controls what the load balancer is listening to
  - accept traffic on a part and protocol
  - communicate with targets on a port and protocol
- nodes can make connections with instances that are registered with the load balancer
  - `can connect to both public and private` instances
- need `8+ freeIPs` per subnet and a `/27` or larger subnet to allow for scale
- `Cross-Zone Load Balancing`
  - allows node to distribute connections equally across `all registered instances across all AZs`
  - allows for more even load balancing : when different AZs have unequal compute infrastructure
