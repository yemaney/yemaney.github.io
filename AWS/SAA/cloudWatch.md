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