## Architecture

### Monolith Architecture

- `all components of application are together`
  - ex) web, db, storage
- `fail together` : one component failing can affect evert other component
- `scale together` : since every component is in the same server
- `bill together` : all components have allocated resources even if they aren't consuming them

### Tiered Architecture

- `different components in different tiers`
- `still coupled together` : since each tier connects to the endpoint of another tier
- `tiers can be vertically scaled independently of other tiers`
  - ex) increase size of web tier without affecting the db tier
- `can use load balancers in between tiers`
  - abstract away connections
  - `allow tiers to horizontally scale independently`
  - tier being load balanced will still need to exist, else tiers depending on it will fail
  - `can't be scaled to zero`
  - still requires synchronous communication

### Evolving with Queues

- `worker fleet architecture`
- `Queues can be put in between tiers`
  - decouples tiers
  - `asynchronous communication`
- `AutoScaling Group`
  - min/desired/max (0,0,100)
  - scaling policy based on queue length
  - `provision instances to handle messages in queue, and scale to zero when queue is empty`
- no communication happens directly
- components are decoupled
- `components can scale independently`

### Microservice Architecture

- micro-services do individual things very well
- components in a micro-service can be `producers and/or consumers`
- producers generate event when something happens
- `event router`
  - central exchange point for events
  - has an event bus : constant flow of information
  - `producers send information to event bus, and event router delivers them to event consumers`
- `no constant running of resources or waiting for things`

## AWS Lambda

- `function as a server (FaaS)`
  - `900s` or `15mins` function timeout
  - assume `stateless` : brand new environment is used each time lambda is invoked

- `resources`
  - `direct memory (indirect CPU) allocation`
    - 128MB to 10240MB memory
    - 1vCPU per 1769MB scaling
  - disk space
    - `512MB` storage available as `/tmp`

- `billed for the duration that a function runs`

- `execution role`
  - iam role assumed by lambda
  - provides permission to interact with other aws products and services

- `design patterns`
  - `serverless applications` : s3, api gateway, lambda
  - `file processing` : s3, s3 events, lambda
  - `database triggers` : dynamodb, streams, lambda
  - `serverless cron` : eventbridge/CWEvents + lambda
  - `realtime stream data processing`: kinesis + lambda

- `networking`
  - `public networking`
    - `default`
    - can access `public aws services` and the `public internet`
    - best performance
      - can run on shared hardware and networking with nothing specific to a customer
    - `no access to VPC based services` by default
      - unless public IP's are provided and security controls allow external access
  - `private lambda`
    - ` runs in a private subnet`
    - `obey all VPC networking rules`
      - can access VPC resources
      - can't access things outside of VPC, unless VPC network configuration allows it
    - `VPC endpoints` can provide access to public aws services
    - `natGW and internetGW` are required to access internet resources
    
- `security`
  - `execution role`
    - iam role assumed by lambda
    - provides permission to interact with other aws products and services
  - `resource policy`
    - controls what services and accounts can invoke a lambda function

- `logging`
  - `cloudwatchlogs`
    - stores `logs` from lambda executions
  - `cloudwatch`
    - stores `metrics`
    - invocation success/failure, retries, latency
  - `X-Ray`
    - distributed tracing

- `invocations`
  - `synchronous`
    - cli/api invoke lambda and `wait for a response`
    - errors and retries have to be handled within the client
  - `asynchronous`
    - `aws services invoke lambda function`
    - ex) s3 event triggers lambda and s3 doesn't wait for a response
    - if event fails, can retry 0-2 times
      - retry logic handled by lambda
      - processing needs to be idempotent 
    - events can be sent to a `dead letter queue after repeated failed` processing
    - `destinations`
      - events processed by lambda can be delivered to another destination (SQS, SNS, lambda, EventBridge) depending on success or failure
  - `event source mappings`
    - `polls streams or queues` for batches of data and sends them to lambda function
    - can't have partially failed/successful batch
      - everything fails or succeeds
    - `permissions from lambda execution role are used` by event source mapping to interact with event source
    - failed batches can be sent to DLQ

- `Versions`
  - lambda function can have different versions
  - `version` : is the code and the configuration of the lambda function
  - `immutable` : never changes once published, has its own ARN
  - `$Latest` points at the latest version
  - `Aliases` (DEV, Stage, PROD) point at a version - can be changed

- `Latency`
  - `execution context` : environment a lambda function runs in
  - c`old start : ~100ms`
    - environment is created
    - runtime is downloaded and installed
    - deployment package downloaded and installed
  - `warm start : ~1-2ms`
    - if future invocation happens quickly, then same context can be used
    - `strategies`
      - `save stuff to tmp` to save time when context is reused
        - lambda needs to cope if context is brand new
      - `define stuff outside if lambda handler`, and it can be reused again in invocations that occur in same context
  - `provisioned concurrency`
    - aws creates and `keeps a number of contexts warm`, improving start speed

## CloudWatch Events and EventBridge

- `CloudWatch Events` delivers a near realtime stream of system events
  -  describing changes in aws products and service
  -  events are JSON objects
- `EventBridge` will replace cloudwatch events (a `superset`)
  - `can handle events from third parties and custom applications`


- `there is  default EventBus for a single aws account`
  - stream of events that occur from any supported service inside the aws account
  - `cloudwatch events has only one event bus`
  - `EventBridge can create additional event buses`

- `rules`
  - rules are `linked to a specific event bus`
  - define `targets`
  - `matches an event` and `routes to one or more targets`
  - `event pattern rule` : tries to matches actual events
  - `scheduled rules`
    - use a `cron expression` to schedule execution

## Serverless Architecture

- low overhead : manage few, if any servers
- applications are a collection of small and specialized functions
- stateless and ephemeral environments : duration billin
- event driven : consumption only when being used
- FaaS is used where possible for compute functionality
- managed services are used when possible : ex) S3, ddb

## Simple Notification Service

- `public` aws service
- coordinates the sending and delivery of messages
- messages are <= `256KB`
- SNS `Topics` are the base entity of SNS
  - permissions and configurations
- `Publisher` : `send` messages to a TOPIC
- `Subscribers` : `receive` messages from a TOPIC
  - HTTP endpoints, EMAIL, SQS, SMS, Lambda, Mobile Push
  - can `filter` subscribers for relevant messages
  - can `fan out a single message to multiple` sqs queues to process related workloads
- `Delivery Status` : can confirm for some resource like HTTP, lambda, SQS
- `Delivery Retries`
- `HA and Scalable within a Region`
- Supports Server Side Encryption `(SSE)`
- `Cross-Account` via Topic Policy

## Step Functions

- State Machine Service
- serverless workflow START -> STATES -> END
  - states are things that occur during the workflow
- States
  - `SUCCEED` % FAIL
  - `WAIT` : pause workflow
  - `CHOICE` : helps take a different path based on input
  - `PARALLEL` : create parallel branches within the state machine
  - `MAP` : takes a list as input, and performs an action for each item in list
  - `TASK` : single unit of work performed by a state machine
- `standard`
  - default
  - 1 year execution limit
- `express`
  - high volume
  - 5 minutes execution
- Created with Amazon States Language (`ASL`)
- IAM Role used for permissions

## API Gateway

- Create and manage APIs
- Endpoint/entrypoint for applications
- sits between applications and integrations (services)
- highly available, scalable, handles authorization, throttling, caching, CORS, transformations, OPENApi spec, direct integration with aws services
- Phases
  - Request Phase:
    - authorize, validate, transform incoming data from clients into a form that integration can handle
  - Response Phase:
    - Takes output from integration and transforms, prepares, and returns it to the client
- `Public Service`
- `HTTP`, `REST`, `WebSocket` APIs
- `Authentication`:
  - `cognito`
    - authenticate with cognito and receive token
    - pass token token with request to api gateway, which then validates the token with cognito
  - `lambda authorizer`
    - client passes bearer token with request
    - gateway calls a lambda authorizer, which returns iam policy and principle identifier
- `Endpoint Types`
  - `Edge-Optimized` : routed to nearest CloudFront point of presence (POP)
  - `Regional` : clients in the same region
  - `Private` : accessible only within a VPC
- `Stages`
  - APIs are deployed to stages, to isolate prod and testing
  - `Canary` : deployments not made to stage but to canary (subsection of stage)
  - configure certain percent of traffic to be sent to canary
  - canary can be promoted to become new base stage
- Errors
  - `4XX` : Client Error, invalid request on client side
  - `5XX` : Server Error, invalid request on server side
  - `403` : Access Denied, authorization error
  - `429` : throttling
  - `502` : bad output return
  - `503` : service unavailable
  - `504` : integration failure (29s)
- `Caching`
  - configured per stage
  - `0 t0 3600s TTL, default 300s`
  - can be `encrypted`
  - 500MB to 237GB
  - reduce load, cost, and improved performance

## Simple Queue Service (SQS)

- Public, fully managed, highly available, message queue service
- used to decouple application components
- `Standard`
  - at least once delivery
  - very high scaling
- `FIFO`
  - guarantee an order
  - exactly once delivery
  - scales less : 3000 messages per second with batching, 300 without
- Messages up to `256KB` in size
  - link to larger data
- received messages are hidden (`VisibilityTimeout`)
  - client has certain amount of time to process message and delete item from queue
  - if client fails, it will reappear (for a retry)
- `Dead-Letter Queues` can be used for problem messages
- `ASGs can scale based on length of a queue, and lambdas can be invoked based on queue length`
- `Billed based on requests`
  - 1 request = 1-10 messages up to 25kKB
  - `short polling` : immediate, can get 0 messages
  - `long polling` : immediate (waitTimeSeconds)
    - waits for messages, cheaper, preferred
  - Encryption at rest (`KMS`) and in transit
- `Queue Policy` (resource policy): can allow access from external account

## Kinesis

- scalable streaming service
- public service, high availability

- SQS vs Kinesis
  - Kineses
    - ingestion, analytics, monitoring, app clicks
    - multiple consumers
    - rolling window persistence
  - SQS
    - worker pools, decoupling, asynchronous communication
    - no persistence of messages
    - 1 production group 1 consumption group

- Kinesis
  - Data Steams : large scale ingestion of data, consumption by consumers
  - Firehose : near real time delivery services
  - Data Analysis : real time SQL processing
  - Video Streams : live video ingestion and analytics


- Firehose vs Data Analytics
  - Firehose : near realtime, simple lambda transformations
  - Data Analytics : realtime, complex SQL transformations

### Kinesis Data Streams

- allow large scale ingestion of data into aws, and consumption of data by other compute services
- `producers` send data into kinesis stream
- `multiple consumers` can access data from that moving window
- real time
- `Scaling`
  - streams can scale from low to near infinite data rates
  - uses `shard` architecture
  - starts with one shard, and addition shards are added as more performance is needed
  - `1 shard : 1MB ingestion, 2MB Consumption capacity`
  - more shards, more performance, more costly
  - streams store a `24-hour` moving window of data by default
    - can increase window to `7 days` at an increased cost
    - kinesis data record : `1MB`

### Kinesis Data Firehose

- fully managed service to load data for data lakes, data stores, and analytics services

- connects to kinesis stream and moves data to another service
  - HTTP, splunk, Redshift, Elasticsearch, S3
  - Redshift uses S3 as an intermediate storage
  - *producer can send data to firehose directly*

- automatic scaling, fully serverless, resilient
- `near real time delivery` (60 seconds)
  - delivery when buffer size fills (1MB) or buffer interval in seconds passes (60seconds)
- supports `transformation` of data on the fly
  - with `lambda`
  - optionally store source data in s3 bucket
- `billing` : based on data volume

- Use cases
  - provide persistence
  - store data in a different format

### Kinesis Data Analytics

- real time processing of data
- `Sources`
  - in-application input stream : kinesis data streams or firehose
  - reference data : from s3 used to enrich streaming data
- Kinesis Analytics Application
  - Application code processes input, using SQL
  - processed data added to in-application output streams that are mapped to destination streams
  - errors can be sent to in-application error stream
- `Destinations`
  - near real time
    - kinesis firehose (S3, Redshift, Elasticsearch, splunk)
  - real time
    - lambda
    - kinesis data streams
- pay for data processed, but not cheap
- use cases:
  - streaming data needing real-time SQL processing
    - time-series analytics, dashboards, metrics

### Kinesis Video Streams

- ingest live video data from producers
- consumers can access data frame-by-frame or as needed
- can persist and encrypt data
- can't access data directly via storage, only via APIs
- integrates with other AWS services
  - rekognition and connect

## Cognito

- authentication, authorization, and user management for web/mobile applications
- `USER POOLS`
  - `sign-in & sign-up  experience, managing user identities`
  - users can also sign in through social identity providers like google, facebook etc.
  - allows you to sign in and get a JSON Web Token (`JWT`)
    - API Gateway can  directly authenticate with JWT
  - supports MFA
- `IDENTITY POOLS`
  - Unauthenticated Identities : Guest Users
  - `Federated Identities`
    -  `SWAP external identity for temporary aws credentials`.
  - assume iam role on behalf of identity and return credentials used to access aws resources

- `User Pools and Identity Pools together`
  - use cognito user pool social sign in to create JWT
  - pass user pool token to Identity Pools
  - `benefit : user pool abstracts all identity providers into one group`, identity pool only configured for a single identity provider (the user pool)

## Glue

- Serverless ETL (Extract, Transform, Load)
  - moves and transforms data between source and destination
-  `Data catalog`
  - persistent `metadata` about data sources in region
  - `crawlers` connect to data sources, determine schema and create metadata
- `Glue Job`
  - ETL Jobs
  - uses data catalog
  - performs transformations using script
  - can be initiated manually or via events
  - glue allocates resources from warm pool when required
- `Data Sources`:
  - `Stores` : S3, RDS, JDBC compatible, dynamodb
  - `Streams` : Kinesis data stream, apache kafka
  - `Targets` : S3, RDS, JDBC databases

- *historically the ETL has been done by datapipeline*

## MQ

- AWS implementation of Apache ActiveMQ
  - supports open standards such as JMS, AMQP, MQTT, OpenWire and STOMP
- provides `both queues and topics`
  - one-to-one or one-to-many
- Single Instance or HA Pair
- `VPC` based : need private networking
- No native aws integration

- `Use case:`
  - migrating from an existing system
  - if certain protocols are needed

## AppFlow

- `fully managed integration service`
  - exchange data between applications (connectors) using flows
- architecture
  - `connections`
    - store configuration and credentials to access applications
  - configure `source to destination field mapping`
  - optional data `transformation`
  - optional `filters and validation`
- sync data across applications
  - ex) sales force records => redshift
- aggregate data from different source
- public endpoints, but works with PrivateLink
- AppFlow Custom Connector SDK (for custom connector)
