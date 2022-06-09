# AWS Virtual Private Cloud {VPC}

- a virtual private network inside of AWS
- regionally resilient
  - `divided into subnets`, each located in an AZ
- private and isolated by default
- nothing in or out without explicit configuration

### Default
- one default VPC per region
- comes with  internet gateway (IGW), Security Group (SG) & NACL
- subnets assign public IPv4 addresses

*best practice not to use default VPC*

## AWS Public vs Private Services

1. `AWS Public Zone:`
    - network that is connected to the public internet
    - where aws services with public endpoints operate from, ie S3
    - internet is used as transit in with communication
2. `AWS Private Zone: Virtual Private Clouds (VPC)`
   - isolated unless configured to otherwise, can't be reached by public internet unless explicitly allowed
   - services can be hosted in these private networks
   - can communicate with aws public zone without touching the internet
   - can access the internet via `IGW`
   - can be access by on-prem using `VPN` or `Direct Connect`

## Sizing and Structure

Considerations
- what size should the VPC be
- structure tiers and resiliency (availability) zones
- are there any networks we can't use

- minimum /28 (16IP)
- maximum /16 (65456)
- *preference to start at 10.16.x.y*
- reserve 2+ networks per region being used per account

Considerations
- how many subnets are needed
- how many IP's in total
- how many per subnet

Subnets
- services use subnets where IP addresses are allocated from
  - VPC services run from within subnets
- located in one availability zone

How to pick number of subnets
1. how many availability zones to use? (4 to be safe) : split VPC into 4 subnets
   1. 1 /16 into 4 /18
2. how many tiers (choose 4) : split subnets to 4 tiers (web, app, db, pare)
   1. 4 /18 each into 4 /20 -> 16 /20

## Custom VPC's
- IPv4 private CIDR Blocks and public IP's
- 1 primary private IPv4 CIDR Block
  - min /28, max /16
- optional secondary IPv4 Blocks
- Optional single assigned IPv6 /56 CIDR Block

DNS In a VPC
- provided by R53
- VPC Base IP + 2 Address
- `enableDnsHostnames` : whether instances with public ip addresses in a VPC get public  dns names
- `enableDnsSupport` : enables DNS resolution in VPC

### VPC Subnets
- AZ Resilient
- a sub-network of a VPC, within a particular AZ
- a subnet can be in only one AZ, but an AZ can have multiple subnets
- IPv4 CIDR is a subset of the VPC CIDR
  - cannot overlap with other subnets
- can optionally have IPv5 CIDR if it is enabled
- subnets can communicate with other subnets in the VPC

Reserved Ip's (5 in total)
- Network Address, first address of subnet
- Network + 1, used by VPC router
- Network + 2, reserved for DNS
- Network + 3, reserved for future requirements
- Broadcast Address, Last Ip in subnet

DHCP Options Set
- Dynamic host configuration protocol
- how compute devices receive IP addresses automatically
- can't be edited, but can create a new one and reallocate
- Auto Assign Public IPv4 or IPv6: assign public in addition to private IP automatically
