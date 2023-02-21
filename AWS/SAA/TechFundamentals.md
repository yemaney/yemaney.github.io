## Hash Functions & Hashing

- hashing
  - take data and create fixed length representation
  - unique hash for different data
  - can't turn hash into original data
- hash function : algorithm to convert data into string
- collision : if different data get the same hash value

## Digital Signatures

- `public key cryptography`
  - public key used to encrypt data
  - private key used to decrypt data
  - private key can sign data, and public key can verify it
- `digital signature`
  - verifies integrity and authenticity
  - hash of data is taken, original data unchanged
  - digital sign hash using private key (authenticates the hash)
  - use public key to verify the hash signature
    - exposes original hash
  - use same algorithm to hash data and see if it matches with the hash exposed by public key