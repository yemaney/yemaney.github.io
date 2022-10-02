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
