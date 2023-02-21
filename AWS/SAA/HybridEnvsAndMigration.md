## Site-to-Site VPN

- a logical connection between a VPC and on-premises network
- `encrypted in transit using IPSec`
- running over the public internet
- Partial `HA`
  - has different endpoints in different AZ
  - single point of failure is customers end
  - Full HA
    - use an additional connection using a separate router
- Quick to provision (`less than an hour`)
- `Virtual Private Gateway (VGW)`
  - associated with one vpc
  - target of one or more route tables
- `Customer Gateway (CGW)`
  - logical configuration in aws
  - or physical device the logical configuration represents
- `VPN Connection`
  - between VGW and CGW

1. Step 1
   1. get ip address of the vpc
   2. get ip range of on premise network
   3. get address of customers physical router
2. Step 2
   1. Create VGW and attach it to VPC
   2. Create CGW for customers physical router
      1. define public ip address to mach physical router
3. Step 3
   1. Create a VPN connection
      1. linked to VGW
   2. Specify CGW to use
      1. tunnels between each endpoint and the physical router will be created

- Static VPN
  - static routes, and network configs
  - simple
  - no load balancing or multi-connection failover
- Dynamic VPN
  - uses Border Gateway Protocol (BGP)
  - create a relationship between VGw and customer router
    - allows to communicate about networks, an state of links
  - multiple vpn connections
    - provide HA and traffic distribution
  - route propagation
    - routes are added RT's dynamically
    - routes learned from VGW

- Consider the following
  - `1.25Gbps` speed limit
  - latency: inconsistent since its over the public internet
  - hourly cost, GB out cost, data cap (on prem)
  - fast setup (hours)
  - can be used as a backup for or with direct connect

## Direct Connect (DX)

- a `1Gbps` or `10Gbps` network port into AWS
  - at a DX location
  - 1000-Base-LX or 10GBASE-LR standards
- just a `port`
  - customer/partner router needs to be connected to the port inside the DX location
  - you need to arrange for cable to be extended to physical premises
- `No HA`
- `No Encryption`
- takes weeks or months
- Customer Router
  - requires `VLANS` AND `BPG`
- `Virtual Interfaces (VIFS)`
  - isolated virtual connection that run overtop the physical DX connection
  - can have multiple over one DX
  - `private VIF`
    - associated with a `VGW` 
    - connect to a single VPC
  - `public vif`
    - provide connectivity to aws public zone services
  - one vif = one VLAN and on BGP session

- Consideration
  - takes much long vs vpn
  - faster than vpn : 40Gbps with aggregation
  - low latency : doesn't use business bandwidth, uses aws network
  - no encryption
  - run IPSEC VPN over public VIF

### Resilience and HA

- region, DX location, Customer premises
- AWS Regions have multiple DX locations
  - dx locations are connected to regions with HA networking
- cross-connect : a single cord connection bw DX port and customer router in DX location
- DX  is extended to customer premises]
- single points of failure
  - DC location, DX router, Cross-connect, Customer DX router, Extension,, Customer Premises, customer router
- Adding Resilience and HA
  - create multiple connections in same DX location
    - use more than one DX routers connected to their own customer DX router and extension
  - Use more than one DX locations and customer premises

## Transit Gateway (TGW)

- Network Transit Hub to connect VPC's to each other and on premises networks
  - uses site-to-site VPN's and direct connect
- reduces network complexity
- single network object : HA and Scalable
- Attachments to other network types
  - VPC, Site-to-Site VPN, Direct Connect Gateway
- VPC
  - configured with a subnet in each AZ where service is required
  - acts as HA inter VPC router (VPC peering replacement)
  - transitive routing
- Site-to-Site VPN
  - each customer premises gateway only has to connect to single transit gateway
  - gives VPC's connection to on premises environment using VPN attachment
- Direct Connect Gateway
- Peering TGW
  - Cross-Region, Same/Cross-Account
  - uses aws global network : benefits from better latency than public internet
- Support multiple route tables allowing complex routing architectures

- Considerations
  - supports transitive routing
  - can be used to create global networks
  - share between accounts using AWS RAM
  - peer with different regions, same or cross account
  - less complexity routing complexity


## Storage Gateway

- hybrid storage virtual appliance
  - virtual environment on premises or in a data center
- `Use Cases`
  - `Extension` of File & Volume Storage into AWS
  - Volume Storage or Tape `backups` into AWS
  - `Migration` of existing infrastructure into AWS
- `Modes`
  - `Tape Gateway` (VTL)
    - storage gateway pretends to be a iSCSI tape library, changer, and drive
    - stores virtual tapes in S3/Glacier
    - virtual tape 100GB - 5TiB, `1PB` total storage across 1500 virtual tapes
    - unlimited VTS (archived glacier) storage
  - `File` 
    - SMB and NFS
    - file storage backed by S3 objects
    - lifecycle policies can automatically control storage classes
    - integrates with `Active Directory` for file authorization
  - `Volume`
    - `Stored`
      - 16TB per volume, 31 volume limit, `512TB` total capacity
      - primary data is stored on-premises
      - volumes are made available via iSCSI for network based servers to access
      - backup data is asynchronously replicated to AWS creating EBS snapshots
      - Ideal fo `migration and disaster recovery`
    - `Cached`
      - primary data is stored in AWS, and snapshots are stored as standard EBS snapshots
      - data that is accessed frequently is cached locally
      - `ideal for extending storage into AWS`
      - 32TB per volume, 32 volumes, `1PB` total capacity

## Snowball, Snowball Edge and Snowmobile

- move large amounts of data `IN and OUT` of AWS
- `Snowball`
  - ordered from AWS, device delivered  (not instant)
  - data is encrypted using KMS
  - 50TB or 80TB
  - 1Gbps or 10Gbps network cabal needed to connect to device
  - `10TB to 10PB economical range`
  - `multiple devices to multiple premises`
  - `only storage`
- `Snowball Edge`
  - `Storage and Compute`
  - large capacity than snowball
  - faster networking than snowball
  - `storage optimized`(with EC2)
    - 80TB, 24vCPU, 32Gib RAM
    - 1TB SSD if EC2 included
  - `compute optimized`
    - 100TB + 7.68 NVME, 52vCPU, and 208GiB RAM
  - `compute with GPU`
    - same as compute optimized with a GPU
  - ideal for remote sites, or where data processing on ingestion is needed
- `Snowmobile`
  - portable DC on a truck
  - special order
  - ideal for single location when 10PB+ is required
  - up to 100PB per snowmobile
  - note economical for multi-site or sub 10PB

## Directory Service

- `provides managed directory service instances`
  - store of users, objects, and other configurations
- Directory
  - store objects with a structure (domain/tree)
    - users, groups, computers, servers, file shares
  - multiple trees can be grouped into a forest
- commonly used in windows environments
- sign-in to multiple devices with same username/password, provides centralized management for assets
- runs within a vpc
- HA, deploys multiple AZs
- some AWS services need a directory eg) Amazon Workspaces


- `Modes`
  - `Simple AD`
    - implementation of Samba 4 (compatibility with basics AD functions)
    - 500 users (small) or 5000 (large)
    - isolated, not designed to integrate with existing on-premises directory
  - `Managed Microsoft AD`
    - primary running location is in AWS
    - can create a trust relationship with existing on-premises directory
      - over private networking (VPN or DX)
      - resilient if the VPN fails : aws services will still be able to access the directory service
    - directly supports applications that required actual Microsoft AD
  - `AD Connector`
    - need to establish private network connectivity with on-premises
    - proxies requests back to an on-premises directory
    - primary directory still on-premises
    - proxy won't work if private connection fails
    - ideal when on-premises directory already exists, and you don't want to create another on
- `Picking a Mode`
  - `simple AD` : default
  - `Microsoft AD` : when MS AD is required by application, or you need to trust AD DS
  - `AD Connector` : use aws services which need a directory

## DataSync

- `Data transfer service TO and FROM AWS`
- Migrations, Data processing Transfers, Archival/Cost Effective Storage, or DR/Business Continuity
- keeps metadata eg)permissions
- built in data validation
- Scalable : 10Gbps per agent (~100TB per day)
- Bandwidth Limiters : avoid the saturation of internet links
- Incremental and scheduled transfer options
- Compression and encryption in transit
- automatic recovery
- `AWS Service integration : S3, EFS, FSx`
- pay as you use : per GB
- agent runs on-premises and connects with AWS DataSync endpoint
- read data from NFS or SMB
- transfers data into AWS

- `Task` : A job within DataSync
  - define what is being synced, how quickly, from and where to
- `Agent` : Software used tot read or write to on-premises data stores using NFS or SMB
- `Location`
  - FROM and TO
  - NFS, SMB, EFS, FSx, S3

## FSx 

### FSx for Windows Servers

- fully `managed` native windows file servers/shares
- `designed for integration with windows environments`
- `integrates with directory service or self-managed AD`
- single or multi-AZ within a VPC
- on-demand and scheduled backups
- accessible using, VPC, Peering, VPN, DX
- KMS at rest encryption and in transit
- shares accessed via `SMB` protocol
- supports volume shadow copies : file level versioning
- `highly performant` : 8MB/s -> 2GB/s, 100ks IOPS, <1ms latency>
- `VSS` : user driven restore of files
- `windows permission model`
- supports `DFS` : scale out file share structure (distributed file system)

### FSx for Lustre

- `managed` Lustre
- designed for `HPC` - Linux Clients
  - machine learning, big data, financial modelling
- supports `POSIX`
- 100's GB/s throughput and sub millisecond latency
- `Deployment Types`
  - `Scratch`
    - highly optimized for short term
    - no replication
    - no HA
    - fast
    - 200MB/s per TiB
  - `Persistent`
    - longer term
    - HA in one AZ
    - self-healing
    - 50/100/200MB/s per TiB
  - burst : 1300MB/s per TiB (credit system)
- Accessible within VPC, over VPN, or Direct Connect
- Can be associated with a repository
  - which is an S3 bucket
  - objects in bucket are visible in file system
  - data is lazily loaded from S3 into file system when first accessed
  - data can be exported back to S3 using `hsm_archive`
- Architecture
  - metadata store on metadata targets (MDTs)
  - objects are stored on called object storage targets (OSTs)
    - 1.17TiN in size
  - storage servers handle requests placed against the file system, and provide cache for frequently accessed data
  - `baseline performance based on size`
    - size min 1.2TiB


- Considerations
  - larger file systems mean more servers, more disks and more chances of failure

## Transfer Family

- managed file transfer service
- `supports transferring TO and FROM s3 and EFS`
- providers managed servers which support  protocols
- Protocols
  - File Transfer Protocol (`FTP`) : unencrypted
  - File Transfer Protocol Secure (FTPS) : TLS encryption
  - Secure Shell (`SSH`) File Transfer Protocol (`SFTP`) : over SSH
  - Applicability Statement 2 (AS2) : structured B2B data
- Identities
  - Service managed
  - Directory service
  - Custom (lambda/APGW)
- Managed File Transfer Workflows (MFTW)
  - serverless file workflow engine
- Endpoint Types
  - `Public`
    - endpoint in aws public zone, accessible from public internet
    - only SFTP
    - dynamic IP
  - VPC
    - VPC with Internet
      - SFTP, FTPS, AS2
    - VPC Internal
      - SFTP, FTP, FTPS, AS2
    - accessible via VPN/DX
    - static IP, can use SG or NACL
- Multi-AZ, resilient and scalable
- billed server per hour and data transferred
- FTP and FTPS : Directory Service or Custom IDP only
- FTP : VPC internal only
- AS2 : VPC only
- if you need to access S3/EFS but with existing protocols
- integrating with existing workflows
