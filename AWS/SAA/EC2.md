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

Permission Options:
1. Public Access
2. Owner Only
3. Specific AWS Accounts

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

- `GP2`
  - default general purpose ssd based storage
  - size range `1GB to 16TB`
  - created with io credit allocation
    - capacity of `5.4million` io credits
    - fills at rate of baseline performance that is based on its size
      - max of `100 or 3 io credit per second per gb of volume size
      - `250 MiB/s`
    - default of 3000 iops by depleting the bucket faster than it replenishes 
    - EBS larger than `1 TB`, maximum `16,000` io credit per second
      - baseline higher that burst, baseline always achieved, don't use credit system
  - good for boot volumes, low latency applications
- `GP3`
  - every volume regardless of size starts with 3000 iops & 125 MiB/s
  - `20% cheaper than GP2` at base price
  - up to `16,000 iops` or `1000 MiB/s`
  - add extra iops explicitly not based on size
