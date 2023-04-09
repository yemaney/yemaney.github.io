# AWS Backup

- `fully managed `data-protection (backup/restore) service
- `consolidate management `into one place
  - across accounts and regions
- supports a wide range of aws products
  - ec2. ebs, efs, rds, ddb, s3 ...etc
- Backup plans
  - `frequency` : how often to make snapshots
  - `window` : time that backups begin and duration
  - `lifecycle` : transition to cold storage
  - `vault`
  - `region copy` : copy backups from one region to another
- Resources : what resources are backed up
- `Vaults` : Backup destination
  - assign kms key for encryption
  - default read and write
  - `vault lock` : write once, read many, 72 hour cool off, then even aws can't delete it
- `On-Demand` : manual backups created as needed
- `Point in time recovery` : restore resource to a specific date and time
