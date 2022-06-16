# VAULT

sources:
- https://www.youtube.com/watch?v=ae72pKpXe-s

## What is HashiCorp Vault

- `cloud agnostic` secrets management system
- API Driven
- safely store and manage sensitive data in hybrid cloud environemts
- used to generate `dynamic short lived` credentials or `encrypt` application data on the fly 

## Use Cases

- Secrets Management
	- centrally store, access, and distribute secrets
	- ex) KV secrets engine
- Encrypting Application Data
	- keep application data secure with centralized key management
	- ex) Encryption as a Service or Transit secrets engine
- Identity-based Access
	- authenticate and access different clouds, systems, and endpoints using trusted identities
	- ex) dynamic aws creds

## Basic Vault CLI Commands

- `vault` list of vault commands
- `vault version`
- `vault read` read secrets from vault
- `vault write` write secrets to vault
- `-h, -help, --help` get help for any command

## Vault Server Modes

- `Dev` intended for development
	- not secure
	- stores everything in memory
	- automatically `unsealed
	- root token can be specified before launching
	- never actually store real secrets in dev mode
- `Prod` used in QA and production

## Common Commands

- `vault server -dev -dev-root-token-id=root` start vault in dev mode with root use named root
- `vault status` basic meta data about server
- `vault login` login to vault
- `vault kv put secret/foo bar=baz` put the kv (bar=baz) in the path (secret/foo)
- `vault kv get secret/foo` read metadata and the recent version of the secret
- `vault kv delete secret/foo` dekete a key from vaualt
- `vault kv undelete -versions=2 secret/foo` undelete a secret

## Vault Architecture - Interals

 - Core
 - API
 - Storage Backend
 - Barrier

## Seal and Unseal Concept

- vault starts up in a `sealed state`
- vault can access the physical storage, but can't decrypt it
- no operations are possible with vault exept to `unseal` the vault and check the `status` if the vault
- `vault data is `encrypted` using the `encryption key` in the `keyring`
- the keyring is encrypted by the `master key`
- and the `master key` is encrypted by the `unseal key`
- shamir is the `default` mechanism to `split` the key into shards
- a certain `threshold` of shards is required to reconstruct the unseal key
- `vault operator unseal` command to unseal
- `vault operator seal` command to seal the vault
- sealing removes the master key in memory an requires another unseal prcoess to restore it
- sealing requires a `single` operator with `root privileges
- once a vault node is unsealed, it remains unsealed until
	- it is resealed via the api
	- the server is resetarted
	- vaults storage layer encounters an unrecoverable error

- `Auto unseal` reduces the operational complexity of keeping the unseal key secure
- delegates the responsibility of securing the unseal key from `uers` to a `trusted device or service`'
- at startup vault will connect to the device or service implementing the seal and ask it to `decrypt` the master key vault read from storage

- initialization with shamir -> unseal keys
- initialization with auto unseal -> recovery keys

## The Configuration File

Running a vault server in `prod` mode involves multiple steps:

- specify the configuration in a configuration file
	- can be JSON or HCL
- start the server
- initialize the server to get unseal keys and an initial root token
- unseal the vault server with the unseal keys

- `vault server -config=./vault-config.hcl` to runa  production server

## Authentication Overview

1. authenticate to a specific path
1. Once authenticated, vault returns a `token` and a `policy`
1. token has a time to live, allow user to extract secrets from vault
1. the policy lets vault know what you allowed to use

## Types of Auth Moethds

- Methods for Users
	- userpass
	- github
	- LDAP
	- JWT
	- OIDC
	- Okta

- Methods for Applications
	- AppRoles
	- AWS
	- Azure
	- Google Cloud
	- AliCloud
	- Kubernetes


- most vault auth methods need to explicitly enabled
- this is done with `vault auth enable` command
- each auth method has a default path
- alternate paths can be specified to enable multiple instances
- custom paths must be specified in CLI commands and API calls

## Policies Overview

Vault uses policies to :
- govern the behaviour of clients
- instrument role based access control by specifying access priviledges with least priviledged principle
- authorization to access secrets
- deny by default

Built-in Poliies:

- default policy
	- can't be removed but can be modified
	- attached to all tokens
	- can be explicitly excluded at token creation time
		- `vault token create -no-default-policy`
	- allows basic functionality such as letting the token look up data about itself and use its cubbyhole data

- root policy
	- can't be removed nor modified
	- aany user associated with this policy becomes a root user
	- best practice to revoke root tokens in production
		- `vault token revoke <token>`
	- one is created to allow root user to do the initial configuration, therafter initial root token should be revoked and more strictly controlled usersand authentication should be used

# Token Overview

- tokens are the core metod for authentication within vault
- tokens can be used directly or dynamically generated by the auth methods
- clients need valid tokens to interact with vault

## The Token Store

- same as the `token authentication backend`
- responsible for creating and storing tokens
- can't be disabled
- only auth method with no login capability
- built-in and automatically available at path `/auth/token`
- you can create tokens directly and bypass other auth methods

## Secrets Engine Overview

- the component of the vault architecture that manages secrets
- store, generate, and encrypt data
- enabled at a path
- flexible and pluggable

Multiple functions
- store and read data
- connect to external services and generate dynamic credentials on demand
- provide encryption as a service
- one time password generation
- certificates

Life Cycle
- `enable` at a given path, 
	- by default they are enabled at their "type" (aws enables at aws/)
- `disable`
	- when a secrets engine is disabled, all of its `secrets are revoked`
	- all the data stored for that engine in the physical storage layer is `deleted`
- `move`
	- move the path for an existing secrets engine
	- reokves all secrets, since secret leases are tied to the path they were created at
	- configuration data stored for the engine persists through the move
- `Tune`
	- tunes global configuration for secrets engine such as TTLs


Commands:

- `vault secrets list` list all  enabled  egines
- `vault secrets enable database` enable a new secrets engine


## Replication Design with DR and PR

- `performance replication clusters` are active services put in different regions
	- no dynamic secreets, leases, or tokens get replicated across
	- static kv secrets engine is replicaated
- `disaster revovery replication clusters` are warm standbys
	- receive data from their respective primary data clusters
	- everything gets replicated
	- manually promote if primary fails

## Vault Agent Overview

- a `client daemon` that uses the same vault binary
- ussed to easily adopt vault without making code changes in your apps

What is does:
- authentication into vault (Auto-Auth)
- manage the token renewal process (Auto-Auth)
- client side caching of tokens and leased secrets / dynamic secrets (caching)
- templating which allows dropping serets into a config file following your desired format

- `vault agent -config=/etc/vault/agent-config.hcl`

