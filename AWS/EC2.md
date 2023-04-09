# Elastic Compute Cloud (EC2)

- `virtual machines` known as instances
- private service, configured to run in a `VPC` network
- is launched into a specific subnet, AZ resilient
- different sizes and capabilities available
- on-demand billing per second
  - charged for compute, storage, and external software
- storage can be local on-host or Elastic Block Store (EBS)
  - will be charged for EBS even if instance is stopped
- states : running,  stopped, terminated
- windows rdp port 3389, linux ssh port 22


## Amazon Machine Image (AMI)
- has attached permissions defining who can use it
- used to create an EC2 or from an EC2
- contains the root volume, the drive that boots the operating system
- block device mapping, used to determine which volume is root volume and which is data volume

`Permission Options:`
1. Public Access
2. Owner Only
3. Specific AWS Accounts


- used to launch ec2 instances
- can be created from an existing instance
- can get from aws or community or marketplace
- regional

`Block device mapping`
- ebs snapshots created from instance ami is created from
- block devices mapping is a table that links, the newly created snapshots with the device id the snapshots had in the original ec2 instance
- when ami is used to create a new instance
  - snapshots are used to create new ebs volumes
  - the volumes then are attached to the new instance using the same device ids as the original instance

`Extra`:
- only exist in `one region`
- `ami baking` : creating an ami from a configured instance + application
- can't be edited, launch instance, update configurations and make a new ami
- can be copied between regions, including snapshots
- default permissions is owner only

`Billing`
- storage cost of ebs volumes the ami references

## Virtualization
Process of running more than one os on a piece of hardware.

Without virtualization:
- server has hardware, os (kernel), and applications
- os runs in privileged state giving it access to the hardware 
- applications make a system call to the kernel to get access to the hardware


- `Emulated Virtualization`
  - software (hypervisor) runs in privileged state
  - guest hosts wrapped in containers called virtual machines
  - vm emulated hardware, and os is unaware of virtualization
  - binary translation :hypervisor intercepts hosts call to emulated hardware, to communicate with real hardware
- `Para-virtualization`
  - guest os aware of virtualization
  - hypercalls : guest os makes call directly to host hypervisor
- `Hardware Assisted Virtualization`
  - host hardware (cpu) aware of virtualization
  - host cpu intercepts calls from guest os and passes it to hypervisor 
- `SR-IOV`
  - hardware devices become virtualization aware
  - host network card can present itself as several mini cards
  - no translation required by hypervisor
  - host network card directly connects to host mini card
  - consistent lower latency at high amounts of consistent io

## Architecture

- `virtual machine` (os + resources)
- run on `EC2 Hosts` hardware that aws manages
- `shared hosts` hardware shared across different aws customers
- `dedicated hosts` hardware dedicated to customer
- `AZ Resilient` as hosts run in one AZ
- `local storage` instance store, temporary storage, lost if instance moves to another host
- `storage` and `data networking`
- when instances are provisioned in a specific subnet
  - a primary `elastic network interface` is provisioned in a subnet and maps to physical hardware of EC2 host
  - can have multiple network interfaces in different subnets in the same AZ
  - cannot connect cross region
- `Elastic Block Store (EBS)`, remote storage
  - runs in one AZ, can't be accessed cross zone
  - `volumes`, portions of persistent storage allocated to instances in the same AZ
- instances stay on a host until
  - host fails or is taken down
  - if instance is stopped and then started (not restarted)
- cannot natively move between AZ
  - create copies and re-provision

Use case:
- traditional os + application compute requirements
- long-running compute
- server style applications waiting for incoming connections
- burst or steady-state load requirements
- monolithic application stacks
- migrating application workloads or disaster recovery

## EC2 Instance Types

Different types of instances have different:
- raw amount of resources
- resource ratios
- storage and data network bandwidth
- system architecture / vendor
- additional features and capabilities like gpu's


- `General Purpose` (A, T, M)
  - default
  - diverse workloads, equal resource ratios
- `Compute optimized` (C)
  - media processing, HPC, scientific modelling, gaming, machine learning
  - mor cpu than memory
- `Memory optimized` (R, X, Z)
  - processing large in memory datasets
  - more memory than cpu
- `Accelerate Computing` (P, G, F)
  - hardware gpu, field programmable gate arrays (FPGAs)
- `Storage Optimized` (I, D, H)
  - large amounts of super fast local storage
  - good for sequential and random io operations
  - databases, data warehousing, elasicsearch, analytic workloads

Instance type Schema:
`<instance family><generation><additional capabilities>.<size>`

## SSH vs EC2 Instance Connect

SSH
- make sure instance security group allows your ip address

Instance connect
- uses aws ip to connect and presents it in the browser
- make sure aws ip compatible with `EC2_INSTANCE_CONNECT` in your region is allowed
 
 ## Storage Basics

 - `Direct` (local) attached storage
   - directly connected to the EC2 host
   - called the `instance store`
   - `fast` because it is directly attached to the hardware
   - if `disk` or `hardware` fails, then the storage can be lost
   - if EC2 moves between hosts the storage can be lost
 - `Network` attached storage
   - called `EBS`
   - highly `resilient`
   - separate from instance hardware so it can survive issues with EC@ host
 
 - `Ephemeral` Storage
   - temporary storage
   - `instance store`
 - `Persistent` storage
   - permanent
   - lives on past the lifetime of the instance
   - `EBS`


- `Block` Storage
  - create `volume` presented to `os` as a collection of uniquely addressable blocks
  - no structure
  - like empty hard drive/disk
  - `os creates a file system on top of the block and mounts it`
    - as c drive in windows or root in linux
  - bootable
- `File` Storage
  - presented as a file share, has structure accessible over the network
  - mountable not bootable
- `Object` Storage
  - collection of objects
  - not mountable, not bootable

Storage Performance

- `IO (block) size` size of data writing to disk (MB)
- `IOPS` input output operations per seconds (s)
- `Throughput` amount of data that can be transferred ina  given second (MB/s)

`IO X IOPS = Throughput`
- choose right block size and then maximize iops to maximize throughput

## Elastic Block Store (EBS)

- `block` storage, `raw` disk allocations
- can be written to or read using a block number
- can be encrypted using KMS
- `AZ resilient` provisioned in one AZ
- in general attached to one over a storage network
- can be detached and reattached
- not lifecycle linked to one instant, persistent
- can create a `snapshot` (back up) to S3
- can create a volume from snapshot (migrate between AZ's)
- has different, physical storage types, sizes, performance profiles
- billed based GB per month

## EBS Volume Types

### General Purpose

#### GP2
  - default general purpose ssd based storage
  - size range `1GB to 16TB`
  - created with io credit allocation
    - capacity of `5.4million` io credits
    - fills at rate of baseline performance that is based on its size
      - min of `100` credit per second per gb of volume size + 3 credits per second, per GB of volume size
    - max `4000 iops`
    - up to `3000 iops burst rate` by depleting the bucket faster than it replenishes 
    - EBS larger than `1 TB`, maximum `16,000` io credit per second
      - no burst, baseline always achieved, don't use credit system
  - good for boot volumes, low latency applications

#### GP3
  - every volume regardless of size starts with 3000 iops & 125 MiB/s
  - `20% cheaper than GP2` at base price
  - up to `16,000 iops` or `1000 MiB/s`
  - add extra iops explicitly not based on size

### Provisioned IOPS SSD

- io1/2/BlockExpress
- IOPS can be adjusted independently of size
- designed for super high performance, low latency, io intensive databases
- Up to `64,000 (256,000)` IOPS per volume and `1,000 (4,000)` MB/s (block express)
- volume size ranges that are compatible `4 GB - 16 TB io1/2 , 4GB - 64TB block express`
- max size to performance ratio
  - io1 : `50`IOPS/GB MAX
  - io2 : `500I`OPS/GB MAX
  - BlockExpress : `1000`IOPS/GB MAX
- pay for size and provisioned iops
- per instance performance (performance cap for an individual ec2 instance)
  - io1 : `260,000` IOPS & `7,500` MB/s
  - io2 : `160,000` IOPS & `4,750` MB/s
  - io2 & BlockExpress : `260,000` IOPS & `7,500` MB/s
  - cap also depends on the type and size of instance

### Hard Disk Drive (HDD)

Both options provide less IOPS than SSD. Generally chosen for cost purposes.

#### st1 
- (throughput optimized)
-  A low-cost HDD designed for frequently accessed, throughput-intensive workloads.
- big data, data warehouses, log processing
- sequentially accessed data
- `125 GB` - `16 TB` in size
- `Base : 40MB/s/TB , Burst 250MB/s/TB`
  - `max 500 IOPS - 500 MB/s`

#### sc1 
- (cold HDD)
- The lowest-cost HDD design for less frequently accessed workloads.
- cold data, archives
- `125 GB` - `16 TB` in size
- `Base : 12MB/s/TB , Burst 80MB/s/TB`
  - `max 250 IOPS - 250 MB/s`

## Instance Store

provide block storage storage devices presented to the os and used as the basis for a file system that can be used as applications

- raw volumes that can be attached to an instance 
- physically connected to `one ec2 host`
  - instances on that host can access them
- `highest storage performance in aws`
  - D3 instance type -> 4.6 GB/s throughput
  - I3 -> 16 GB/s throughput
  - `more IOPS snd throughput vs EBS`
- included in the prices, use it or lose it
  - allocated a certain number of volumes based on instance type and size
- `attach at launch time`
- `ephemeral (temporary) storage`
  - if an instance moves between hosts then data stored in instance store volume is lost
    - if stopped and started, change instance type, or undergoing maintenance

## EBS vs Instance Store

`EBS`
- pair with good size that can give the level of performance
- `persistent` storage
- `resilient` storage
- storage `isolated` from instance lifecycle

- Cheap -> ST1 or SC1
- throughput or streaming -> ST1
- Boot -> not ST1 or SC1

- GP2/3 - up to `16,000IOPS`
- io1/2 up to `64,000 IOPS (256,000 IOPS block express)`

- take lots of individual ebs volumes to create `RAID0` set
- achieve combined performance of all individual volumes
  - RADI0 + EBS up to `260,000` IOPS (io1/2-BE/GP2/3)

- keep in mind the `performance each volume gives`, and the `maximum performance of the instance itself`

`Instance Store`
- super high performance
- cost -> instance store (often included)
- `more than 260,000 IOPS`, CAN GET MILLIONS IOPS


Extra
- resilience w/ App in-build replication -> it depends
- high performance -> it depends

## EBS Snapshots

Efficient way to back up EBS volumes to s3

- the first is a full copy of `data used` on the volume
- future snaps are incremental
  - difference between previous snapshot and current state of volume
- if you delete incremental snapshot, newer snapshots will still function
  - each snapshot is self sufficient
- `volumes can be created from snapshots`
  - snapshots allow you to clone a volume
  - new volume can be created in a new AZ, or regions since they are stored in S3
  - `makes EBS volumes that are AZ resilient, to regionally resilient`

`Performance`
- new EBS -> full performance immediately
- snaps `restore lazily` - fetched gradually
- requested blocks are fetched immediately
- `can force a read of all data immediately` from s3 to volume
  - using a tool in instance os
- `Fast Snapshot Restore (FSR)` - immediate restore
  - up to 50 snaps per region, set on the snap and AZ
  - costs extra

`Billing`
- `gigabyte / month`
- used not allocated data
  - charged for `changed or new allocation in snapshot`
  - reference data that is not changed from older snapshots

## EBS Encryption

- Encryption uses KMS which uses CMK
- when an encrypted volume is created
  -  CMK saves an encrypted DEK onto the volume
- when the volume is first used
  - EBS asks KMS to use CMK to decrypt the DEK which is then loaded into the memory of the EC2 host using it
- EC2 instance running on the host can now use the decrypted DEK in the host, to interact with the encrypted EBS
- cipher text stored at rest
- snapshots of encrypted volumes, and volumes created from such snapshots all share the same DEK


- accounts can be set to encrypt by default
- each volume uses 1 unique DEK
- can't change a volume to not be encrypted
- os isn't aware of the encryption 
  - (AES256) algo is done on host
  - no performance loss

## Network Interfaces, Instance IPs and DNS

- network interface
  - Every ec2 has an elastic network interface (eni)
    - can have `secondary eni in a separate subnet but same AZ`
  - has 
    - a mac address
    - primary ipv4 private ip -> internal dns ip10-x-x-.ec2.internal
    - 0 or more secondary ips
    - 0 or 1 public ipv4 address
      - dynamic, changes when ec2 is stopped and started in a different host
      - dns -> ec2-x-x-x.compute-1.azmazonaws.com
      - inside vpc resolves to primary private ip
      -  outside of vpc it resolves to public ip
    - 1 elastic ip per private ipv4 address
      - allocated to an account
      - can be associated with primary or secondary interface
        - `if attached to primary, it replaces the public ipv4`
    - 0 or more ipv6 addresses
    - security groups
    - source/destination check
  - can detach secondary interfaces and move them to other ec2 instances

Extra:
- can move secondary eni mac licensing
- multi-homed (subnets)
  - use multiple interfaces, with different ips and security groups
- os never sees public ipv4, only sees the private
  - public ipv4 is handled by internet gateway using nat
  - ipv6 public by default
- ipv4 public ips are dynamic, stop/start or (change of host) changes ip
- public dns resolves to private in vpc
  - never leaves the vpc, for instance to instance communication

## Purchase Options

- On-Demand (default)
  - isolated, but multiple customer instances run on shared hardware
  - instances of different sizes run on the same ec2 hosts, consuming a defined allocation of resources
  - per-second billing while an instance is running
    - associated resources such as storage consume capacity, so billed regardless of instance state
  - no interruptions
  - no capacity reservation
  - predictable pricing
  - no upfront cost
  - no discount
  - choose for short-term or unknown workloads or applications which can't be interrupted

- Spot
  - aws selling unused ex2 host capacity for up to 90% discount
  - spot price is based on the spare capacity at a given time
  - if spot price goes above your maximum price, then your instances are terminated
  - never use for workloads which can't tolerate interruptions
  - for workloads that are non time critical, can be rerun, cost sensitive, stateless, has bursty capacity need

- Dedicated Hosts
  - pay for host that contained the instances, no instance charges
  - might have software licensing based on `sockets` or `cores`
  - host affinity --> if instance is stop and started it remains on the same host
  - only your instances run on the dedicated host
  - specific family and size of instance
    - nitro can use different size of instances at the same time
  - on-demand & reserved options for pricing
  - ami limits : rhel, suse linux, and windows amis aren't supported
  - amazon rds instances are not supported
  - placement groups are not supported
  - hosts can be shared with other ORG accounts using Resource Access Manager (RAM)
    - host own sees all instances running on it, but can only edit ones it owns
    - instances owners, that ar not the host owner, can only see their instances

- Dedicated Instances
  - no other customers use the same hardware
  - don't own or share the host
  - hourly fee per region regardless of how many dedicated instances are being used
  - for when you have requirements to not share hardware

*On-demand, reserved, and spot*

- Reserved
  - for long term consistent usage
  - unused reservation are still billed
  - for a particular type of instance and locked to an AZ or Region
    - reserve based on AZ also reserves capacity
  - can have a partial effect
    - ex) reservation for small T3 instances might partially apply to large T3 instances
  - plans
    - 1 year or 3 year
    - no upfront -> reduce per second fee
    - all upfront -> no per second fee, greatest discount
    - partial upfront
  - scheduled reserved instances
    - ideal for long term usage which doesn't run constantly
      - specify frequency, duration, and time
      - ex) batch processing daily for 5 hours at 23:00
    - slightly cheaper than on demand
    - doesn't support all instance types or regions
    - 1200 hours per year minimum
    - 1 year term minimum
  - capacity reservation
    - when major failure results in lack of available capacity in a region or AZ
    - there is a priority list of which purchase options get available instances first
      - reserved purchases -> on-demand -> spot
    - regional reservation
      - billing discount for valid instances launched in any AZ in that region
      - don't reserve capacity, same priority as on-demand
      - 1 or 3 year term
    - zonal reservation
      - same discount as regional reservation, but only apply to one az
      - capacity reservation in the az
      - 1 or 3 year term
    - on-demand capacity reservation
      - book to enure you always have access to capacity in an az
      - at full on demand price
      - no term limit
      - pay regardless if you consume it

- Savings Plans
  - hourly commitment for a 1 or 3 year term
  - general plan
    - reservation of general compute $ amount, save up to 66%
    - ec2, fargate, lambda
  - ec2 savings plan
    - up to 72% savings
  - products have an on-demand rate and a savings plane rate
  - get savings plan rate, up to to the amount you commit to

## Instance Status Checks & Auto Recovery

- Instance Status Checks
  - each ec2 instance gets two 2 tests
    - system status
      - loss of system power, network connectivity,, host software/hardware issue 
    - instance status
      - corrupted file system, incorrect instance networking, os kernel issue
  - resolution
    - can manually stop and start an instance, restart, or terminate and recreate

- Auto recovery
  - moves instance to new host with same configs
    - same instance ID, private IP addresses, Elastic IP addresses, and all instance metadata
  - can create a cloudwatch alarm triggered when an instance fails a status check
    - can send message
    - can take action
      - recover (auto-recover), reboot, stop, or terminate
  - works only with instances with ebs volumes attached

- Termination protection
  - can be enabled in instance settings, to protect from accidental termination
  - can separate permissions to enable and disable termination protection

## Horizontal and Vertical Scaling

Scaling is what happens when systems have to grow or shrink depending on changes to the load the experience.

- Vertical
  - `resizing the EC2 instance`
  - `requires a reboot` which can potentially cause disruption
  - generally scale during pre-agreed times (outage windows)
    - limits how quickly you can respond
  - larger instances cost more, cost increase scales faster than size increase
  - `upper cap` on performance (instance size)
  - no application modification required
  - works for all applications even monoliths

- Horizontal
  - `changes the number of instances`
  - require a `load balancer`
    - to distribute traffic across multiple instances
  - can be shifting across instances
  - requires application support or `off-host sessions`
  - `no disruption when scaling`
  - no real limits, keep adding instances
  - often `less expensive`, no large instance premium
  - `more granular`, by adding smaller instances

## Instance Metadata

- Service EC2 provides to instances
- accessible inside all instance
  - at ip `http://169.254.169.254/latest/meta-data/`
- data about the instance that can be used to configure or manage the instance
  - info on the environment that the instance is in
  - ex) networking, authentication info, user data
- not authenticated or encrypted

## Bootstrapping

Process where scripts are run when an instance is first launched. To create an instance with a certain configuration.
- enabled using user data

`User data`
- accessed via the meta-data ip
- `http://169.254.169.254/latest/user-data/`
- anything in userdata is executed by the instance Os
- only executed on launch
- ec2 doesn't interpret, the os needs to understand the user data
- it's possible to have a bad config and instance to still run
- not secure, don't use for passwords or long term credentials
- 16KB size limit
  - for larger, make script download larger file
- can be modified when instance stopped

`Boot-TimeToService`
- Basic ami -> launch instance -> manual post launch configuration
- Basic ami -> launch instance -> bootstrapping
- Baked ami -> launch instance
  - less flexible
  - do for time intensive processes

Ideally combine bootstrapping and baked ami

`Cloudformation Init (CFN-INIT)`
- a way to pass complex bootstrap configuration to an instance
- simple configuration management system
  - install packages with version awareness
  -  manipulate groups and users
  -  download sources 
  -  create files 
  -  run commands and check state 
  -  run services
- provided with directives via `metadata` and `AS::CloudFormation::init` on a CN resource
- `works with stack update

`CloudFormation CreationPolicy and Signals`
- inform cloudformation if it has been configured correctly
- creation policies create a `'WAIT STATE'` on resources 
  - not allowing the resource to move to `CREATE_COMPLETE` until signalled using the cfn-signal tool
- reported to the stack, and updates the instance state (OK or not)

## Instance Roles and Profiles

- Roles that an instance can assume.
- Anything running in the instance has the permissions granted by the role
- `instance profile` : wrapper around an iam role
  - allows permissions to get inside the instance
  - attached to the instance
- temporary credentials delivered via the instance meta-data
  - `iam/security-credentials/role-name`
- creating the role in the console also creates the profile, must create both separate with cloudformation

## SSM Parameter` Store

- storage for `configuration` and `secrets`
  - license codes, database strings, full configs and passwords
- types: `String, StringList, SecureString`
- supports hierarchy and versioning
- plaintext and `ciphertext` (with KMS)
- public parameters
- integrated with IAM to authorize access
- changes can create events

## System and Application Logging on EC2

- Monitoring inside the instance
- cloudwatch is for metrics and cloudwatch logs is for logging
  - neither natively capture data inside an instance
- `cloudwatch agent` is required with some `configuration` and `permissions`
  - software that runs inside the instance and captures os visible data and sends to cloudwatch
  - `configuration` tells the agent what to do (what data to capture)
  - `permissions` can be given by attaching a role to the instance
  - one log group for each log to capture. and one log stream in each log group for each instance sending data

## Ec2 Placement Groups

Allows you to control where ec2 instances are placed.

- `Cluster` Placement Groups (`PERFORMANCE`)
  - pack instances close together
  - best practices : to let aws find a location with needed capacity
    - launch all instances at the same time
    - use same tyupe of instances
  - `single AZ`, same rack, sometimes same host, all members have direct connections to each other
    - 10Gbps stream (vs 5 normally)
    - lowest latency and max packets per second (PPS) possible in aws
    - should use enhanced networking for best performance
  -  can span VPC peers, but performance will be impacted
  -  requires a supported instance type
  -  use cases : performance, fast speeds, low latency
- `Spread` Placement Groups (`Resilience`)
  - keep instances separated, different hardware (racks)
    - each rack has its own network and power source
  - can span multiple AZ's, 7 instances per AZ limit
  - not supported for dedicated instances or hosts
  - use case :small number of critical instances that need to be kept separated from each other
- `Partition` Placement Groups (`Topology Awareness`)
  - groups of instances spread apart
  - can span multiple AZ's
  - divided into `paritions`, max 7 per AZ
  - each partition has its own racks no sharing
  - can launch as many instances as needed, spread across the partitions
  - have awareness of which partition the instance is in
  - use case : huge scale parallel systems

## Enhanced Networking & EBS Optimized Instances

Enhanced Networking
- SR-IOV : Host has Network Interface Cards (NIC) that are virtualization aware
  - higher I/O & Lower Host CPU Usage
  - More Bandwith (fasster network speed)
  - higher packets per second (PPS) and consistent lower latency

EBS Optimized Instances
- dedicated capacity for EBS (doesn't affect data networking)
- most instances support, and have it enabled by default
- required for high performance EBS volume types
