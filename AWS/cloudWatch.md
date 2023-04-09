# Cloud Watch

Collects and manages operation data

Performs three main jobs
- `metrics` : collection, monitoring, and action data related to aws instances, like cpu utilizations
- `logs` : collection, monitoring, and action based on logging data
- `Events` : event hub
  - generate actions based on an aws service or time

### `Namespace`
- container for monitoring data
  - *aws/service is reserved for aws*

### `Metric`
- collection of related data points in a time ordered structure
- `data points` : one time point of a specific metric
- `dimension` : name : value pairs used to separate data points for different things, ex) instance type and value
- `alarm` : linked to a specific alarm, can take action based on alarms state (`OK`, `ALARM`) that is decided by some logic on the metric

### CloudWatch Logs
- `public` service : useable from aws on-premise as long as you have network connectivity and permissions
- `store`, `monitor`, and `access` logging data
- built in integration with aws services such as EC2 and Lambda
- for anything outside of aws, use the `unified cloudwatch agent`
- can generate a metric based on logs with `metric filter`

#### Architecture
- a `regional` service
- a `log event` are messages from a source
- a `log stream` is a sequence of log events from the same source
- a `log group` is a container for multiple log streams for the same type of loggingq
  - `retention` and `permission` configurations are set here
  - `metric filters` are also defined here

## Cloud Trail
- logs api calls that affect an aws account (almost everything) as `CloudTrail Event`
- `90` days stored by default in `Event History`
  - need to create a trail to customise this
- `Management` or `Data` Events
  - `Management` : creating or terminating resources (logged by default)
  - `Data` : information about resource operations, like accessing s3 object (must be enabled)
- `regional` service
  - `one` region
  - `all regions` : trail in every region is aggregated as if it is one trail
  - `global` services log to `us-east-1` (must enable global service event logging)
- can store in an s3 bucket indefinitely as compressed json files
- can be integrated with cloudwatch logs
  - CloudTrail can put its logging data into cloudwatch logs
- can create an organization trail to log OU
- `not realtime`