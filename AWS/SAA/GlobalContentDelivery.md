# Cloudfront 

## Architecture

- `content delivery network.` : Improve delivery of content from original location of data to viewers
  - done by caching and an efficient global network
  - integrates with ACM for HTTPS
  - download caching only
- `Origin` : Source location of your location
  - S3 ORigin or Custom Origin
- `Distribution` : configuration unit of cloudfront
  - unique domain name is created for each distribution or can use your own domain name
  - after configuration is complete : deploy distributution to cloudfront network
    - configuration sent to all chosen edge locations
  - `Behavior`
    - use origins as content source
    - linked to distributions, which can have on or more behavior
    - configured with path patterns
- `Edge Location` : local cache of your data
  - more cache hits equals lower origin load
- `Regional Edge Cache` : larger version of edge location
  - for things accessed less frequently
  - only supported by custom origins

- `Flow`
  - customer searches, and goes to edge location
  - go to regional edge cache if supported and edge location doesn't have content
  - go to origin


## Origins

- `Origins`
  - if edge location gets a request for an object that isn't cached, it is retrieved from the origin
  - `origin groups` : collection of 2 or more origins that can be used by a behavior
    - provide resilience
  - `S3 Buckets`
    - origin domain name : point directly at s3 bucket
    - origin path : use a particular path of bucket
    - `origin access identit`y : give cloudfront a virtual identity
    - view protocol and origin protocol are the same
    - origin custom headers
    - if static website hosting is configured, it is view as a custom origin
  - `media package channel endpoints`
  - `media store container points`
  - `custom origins`
    - minimum origin SSL protocol
    - `origin protocol policy` : HTTP only, HTTPS only, match viewer
    - `HTTP/S port` : where origin listens on, used for connections between edge locations and origin
    - custom headers : configure origin to accept connections only from cloudfront


## Distributions & Behaviors

- `Distribution settings:`
  - `can have multiple behaviors` which have a precedence
  - price class (which edge locations to use)
  - WAF
  - alternate domain name
  - SSL certificate
    - default comes with default cname
    - custom required for custom cname
    - SNI or non SNI
    - security policy (TLS version)
    - supported HTTP versions
    - logging
    - enabled, disabled
- `Behavior settings :`
  - where caching controls and restricting viewer access are configured
  - origin or origin group
  - `viewer protocol policy` (policy used between viewer and edge location)
  - allowed HTTP methods
  - field level encryption
    - encrypt from point data enters edge location
  - `cache directives`
    - methods that are cached
    - cache based on header
    - TTL
    - restrict viewer access
      - must specify trusted signers
    - compress objects automatically
    - lambda edge functions


- `Time To Live (TTL)`
  - default `24hrs` (behavior) (validity period)
  - object in cache `expires` after TTL, but is `not deleted`
    - next request will make cache forward request to origin to check object version
    - if object is not modified (304) : object in cache is marked as current and returned to user
    - if there is a new version (200) : origin returns new object
  - `Object Specific TTL`
    - Custom Origin or S3 (via object metadata)
    - Origin Header : Cache-Control `max-age` (`seconds`)
    - Origin Header : Cache-Control `s-maxage` (`seconds`)
    - Origin Header : `Expires` (`Date and Time`)
      - data and time an object should be viewed as expired
  - `minimum` and `maximum` TTL
    - `limit the object specific TTL` values

- `Invalidation`
  - performed on a distribution, applies to all edge locations : takes time
  - `immediately expires all objects that match a path pattern`, regardless of their TTL
  - use `versioned file names` : to avoid needing invalidation 
    - avoid cost of invalidation
    - logging is more effective
    - still keep all version of objects to switch between

- `SSL`
  - cloudfront distributions are created with default domain names (cname) that comes with SSL
    - SSL cert covers all distributions
  - alternate domain names can be used to access distributions
  - verify ownership (optionally HTTPS) using SSL certificate
  - generate certificate in `us-east-1` with ACM
  - options : HTTP or HTTPS, HTTP => HTTPS, HTTPS only
  - Two SSL connections
    - viewer - cloudfront
    - cloudfront - origin

- `SNI (Server Name Indication)`
  - TLS extension allowing client to tell server which domain name to access
  - `resulting in many SSL certs/Hosts using a shared IP`
  - HTTPS encryption happens at TCP layer, lower than HTTP
  - no extra cost
  - not supported by old browsers
    - will require dedicated IPs at a cost

## Access

- `OAI (Origin Access Identities)`
  - for S3 Origins
  - associated with cloudfront distribution
  - can be used in s3 bucket policies
    - DENY all but one or more OAIs
- `Custom Headers`
  - for custom origins
    - make require custom header
  - configure cloudfront to send custom headers with original request
- `IP Based FW Blocks`
  - For Custom Origins
  - traditional firewall around origin, configured to accept only from edge location IPs

## Lambda@Edge

- `Lambda@Edge`
  - lightweight lambda at edge location
  - adjust data between teh viewer and origin
  - node.js or python
  - run in aws public space
  - layers are not supported
  - `different limits`
    - viewer : 128MB, 5sec
    - origin : 30sec
  - use cases :
    - A/B testing : viewer request
      - change url viewer requested
    - migrating between s3 origins : origin request
      - gradually transfer traffic to different s3 origin
    - different objects based on device : origin request
    - content by country : origin request


## AWS Certificate Manager (ACM)

- `regional`
  - `us-east-1` for cloudfront use-case
- allows the creation, management and renewal of certificates
- allows deployment of certificates onto `ONLY` supported AWS services such as `CloudFront`, `API Gateway` and `ALB`
  - `not EC2` or on-premise

- HTTPS uses SSL/TLS to encrypt data in-transit
- servers prove identity using digital certificates signed by trusted authorities
- deploying to cloudfront distribution
  - all edge locations also get the certificate

##  Global Accelerator

- 2 anycast IP addresses
  - 1.2.3.4 & 4.3.2.1
  - allow a single IP to be in multiple locations, routing moves traffic to closest edge location
  - traffic initial uses public internet and enters a global accelerator edge location
  - edge locations transit data over aws global network

- network product
  - non http/s
  - TCP, UDP
