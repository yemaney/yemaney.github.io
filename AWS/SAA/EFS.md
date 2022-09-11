# Elastic File System (EFS)

## EFS Architecture

- AWS managed implementation of NFS which allows for the creation of shared `filesystems`
-  shared between many EC2 instances
-  private service
-  made available via `mount targets` inside a VPC
   -  mount targets : exist in subnets with an IP from it
   -  should put mount target in every AZ a VPC uses for high availability
   -  EC2 instances connect to the mount target to access EFS
-  can be accessed from on-premises : VPN or DX
-  `Linux Only`
-   `Performance modes`
   -  `General Purpose` : default for 99.9% of use cases
   -  `Max I/O` : for anything that is highly parallel
-  `Throughput Modes`
   -  `Bursting`
      -  throughput scales with size of the file system
   -  `Provisioned`
      -  specify throughput requirements separate from the amount of data being stored
-  `Storage classes`
   -  `Standard`
      -  default, frequently accessed data
   -  `Infrequent Access`
      -  to save money for anything not used a lot
   -  `Lifecycle policies` can be used with classes
