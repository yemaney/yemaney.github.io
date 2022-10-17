# AWS Virtual Private Cloud {VPC}

- a virtual private network inside of AWS
- regionally resilient
  - `divided into subnets`, each located in an AZ
- private and isolated by default
- nothing in or out without explicit configuration

### Default
- `one default VPC per region`
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

- `minimum /28 (16IP)`
- `maximum /16 (65456)`
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

`Reserved Ip's (5 in total)`
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

## Routing

- a vpc router is a highly available device, present in every vpc
- default routes traffic between subnets within a vpc
- route tables control what happens to data as it leaves a subnet
- `destination ips with larger prefix are given priority` when router chooses which route to use
- destination is matched with a `target` which the router will forward data to
- `route tables attached to zero or more subnets`
- `subnet has to have a route table` either main or custom one attached
- local routes always exist, and have first priority


## Internet Gateway

- `Regionally resilient` attached to a VPC
- VPC can have 0 or 1 IGW
- IGW can be attached to 0 or 1 VPC
- runs from within the aws public zone
- traffic between the VPC and the internet or aws public zone
- managed service

Steps:
1. Create IGW
2. attach IGW to VPC
3. Create custom route table
4. Associate RT with VPC
5. Default routes => IGW
6. configure subnet to allocate IPv4

- a record is created and is maintained by IGW
  - links instances private ips to their public IPv4
  - instance doesn't know its public address
- IPv6 can be publicly routed by default
  - IGW does no tranlations
  - instances do know their IPv6


Bastion Host / Jumpbox
- instance in a public subnet
- incoming management connections
- then access internal VPC resources
- management point or entry point for private only VPC's

## Stateful vs Stateless Firewalls

`Stateless firewall`
- see `inbound` and `outbound` traffic as two `separate parts`
- will require two rules, one rule for outbound traffic and another for inbound
  - outbound rule must allow all ports
- requests are bound for a well known ports
- response is to a random ephemeral port used by the client to make a request

`Stateful firewall`
- can identify the request and response components of a connection as being related
  - using port numbers and IP's
- allowing a request automatically allows the response, and vice versa
  - don't have to allow all outbound ports, since port relations are understood

## Network Access Control Lists (NACL)
Traditional firewall available within aws vpcs. 
- (`stateless`)
- see `inbound` and `outbound` traffic as two `separate parts`

- `associated with subnets`
  - every subnet has one nacl
  - a nacl can be associated with many subnets
  - filers traffic crossing the `subnet boundary`
  - doesn't impact connections within a subnet
  - cannot be assigned to aws resources, only subnets
- rule match the DST IP/range, DST Port, protocol and Allow or Deny
  - can explicitly deny and allow
  - no logical resources
- rules are `processed in order`
  - lowest to highest rule numbers
  - once a match occurs process stops
  - * is an implicit deny if nothing else matches
- app port & ephemeral ports are needed on each NACL for each communication type which occurs
  - within a VPC
  - to a VPC
  - from a VPC
- vpc's are created with a default nacl that has no effect
  - has an allow all and implicit deny rule for both inbound and outbound rules
- custom nacls can be created for a specific vpc and are initially associated with no subnets
  - default only has the implicit deny, so all traffic is denied
- used together with security groups to add explicit deny

## Security Groups (SG)

- stateful - detect response traffic automatically
  - allowed (in or out) request -> allowed response
- no explicit deny
  - only allow or not allow (implicit deny)
  - can't block specific bad actors
- supports IP/CIDR and logical resources
  - including other security groups and itself
- attached to elastic network interfaces (ENI)
  - attaching to an instances -> attach primary network interface of the instance

Logical Reference
- reference a security group in rules
  - considers all instances within the security group being referenced
- reference itself
  - considers anything with the SG attached
  - scales with adds and removes from the SG

## Network Address Translation (NAT) and Nat Gateways
Set of processes for remapping SRC and DST IP's.
- when you want to keep resources private but give them access to making requests to resources in the public zone


- `IP masquerading` many private IP's to one public IP
  - gives private CIDR range outgoing internet access
    - can make request and receive response
  - cannot initiate from public internet to these private resources as each public IP maps to many private
- runs from a `public subnet`
  - so it can be given a public IP address
  - default route table points to an Internet gateway
- `AZ resilient service`
  - deploy one in each AZ for regional resilience
- pricing
  - hourly charge per hour
  - data processing charge per GB of processed data
- `isn't required and doesn't work for IPv6 `
  - since all IPv6 are publicly routable, unless nacl or sg are used


EC2 as a NAT instance vs Nat Gateway
- instance
  - disable source and destination checks
  - can be cheaper, but more management overhead
  - use as a bastion server
  - support NACL or SG
- GW
  - HA, high scalability, fully managed
  - GW cannot be a bastion server
  - only support nacl, use sg on instances behind GW

## SSH Agent Forwarding

- connecting using agent forwarding creates a separate ssh channel
  - allowing agent running on the client to be used ont he bastion
- when user, in bastion, connects to another resource
  - the bastion can use the client ssh-agent to prove identity
- private key remains on the client at all times
  - authentication requests are forwarded
  - same identity is used to connect to bastion and then through to the other resource

- `eval ssh-agent` to check if agent is running
- `ssh-add -K ./keyName.pem` add private key to ssh agent
- `ssh -A -i "A4L.pem" ec2-user@ec2-34-229-86-153.compute-1.amazonaws.com` make an ssh connection with agent forwarding enabled
- `ssh  ec2-user@10.16.109.185` ssh from bastion to other resource

## VPC Flow Logs

- `capture metadata (not content)`
  - src ip, dest ip
  - src port, dest port
  - protocol
    - ICMP=1, TCP=6, UDP=17
  - action : ACCEPT, REJECT
- can be attached to:
  - `VPC` : applies to all ENIs in the VPC
  - `Subnet` : applies to all ENIs in the Subnet
  - `ENI` directly
- `not realtime`
- `destinations`
  - S3
    - Can query with Athena
  - CloudWatchLogs
- can capture ACCEPTED, REJECTED, or ALL metadata

- not logged
  - ec2 metadata service : 169.254.169.254
  - DHCP
  - amazon DNS, windows license

## Egress-Only Internet gateway

- alternative to internet gateway, but gives privacy like NAT to IPv6
- outbound-only for IPv6
- create eigw, and make it as target for ::/0 route in VPC RT
