# Skill: Cryptography

## What This Is
Understanding encryption — how it works, when it's strong, and when it's broken.

## Hashing
| Algorithm | Status | Use |
|---|---|---|
| MD5 | ❌ Broken | Legacy only, never for passwords |
| SHA1 | ❌ Weak | Avoid for new systems |
| SHA256/SHA512 | ✅ Good | File integrity, digital signatures |
| bcrypt | ✅ Strong | Password hashing (slow by design) |
| Argon2 | ✅ Best | Modern password hashing standard |

## Symmetric Encryption
```bash
# AES-256 encrypt a file (OpenSSL)
openssl enc -aes-256-cbc -pbkdf2 -in plaintext.txt -out encrypted.bin

# Decrypt
openssl enc -d -aes-256-cbc -pbkdf2 -in encrypted.bin -out decrypted.txt

# Generate random key
openssl rand -hex 32
```

## Asymmetric Encryption (RSA/ECC)
```bash
# Generate RSA keypair
openssl genrsa -out private.pem 4096
openssl rsa -in private.pem -pubout -out public.pem

# Encrypt with public key
openssl rsautl -encrypt -inkey public.pem -pubin -in message.txt -out encrypted.bin

# Sign a file
openssl dgst -sha256 -sign private.pem -out signature.bin file.txt

# Verify signature
openssl dgst -sha256 -verify public.pem -signature signature.bin file.txt
```

## TLS/SSL
- Always TLS 1.2 minimum, TLS 1.3 preferred
- Check certs: `openssl s_client -connect target.com:443`
- Test SSL config: `testssl.sh target.com`
- Common weaknesses: expired certs, weak cipher suites, BEAST, POODLE, Heartbleed

## Common Crypto Attacks
- **Brute force**: weak keys, short passwords
- **Rainbow tables**: pre-computed hash lookup (defeated by salting)
- **Padding oracle**: CBC mode decryption oracle
- **Timing attacks**: non-constant-time comparison
- **Replay attacks**: capture and resend valid auth tokens
- **Weak RNG**: predictable random number generation

## Hash Cracking
```bash
# Identify hash type
hashid hash_value

# Crack with hashcat (GPU)
hashcat -a 0 -m 0 hash.txt rockyou.txt     # MD5
hashcat -a 0 -m 1800 hash.txt rockyou.txt  # SHA512crypt (Linux)
hashcat -a 0 -m 3200 hash.txt rockyou.txt  # bcrypt

# John the Ripper
john --wordlist=rockyou.txt hash.txt
john --show hash.txt
```

## Key Management Rules
1. Never hardcode keys in source code
2. Use environment variables or a secrets manager (Vault, AWS Secrets Manager)
3. Rotate keys regularly
4. Different keys for different environments (dev/staging/prod)
5. Audit access to private keys
