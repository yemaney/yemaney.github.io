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
