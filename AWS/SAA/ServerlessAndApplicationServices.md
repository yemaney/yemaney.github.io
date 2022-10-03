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