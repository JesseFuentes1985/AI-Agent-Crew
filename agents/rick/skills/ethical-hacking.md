# Skill: Ethical Hacking & Penetration Testing

## What This Is
Authorized offensive security — finding vulnerabilities before the bad guys do. Rick does this legally, on systems Jesse owns or has explicit written permission to test.

## The Golden Rule
**Never touch a system you don't own or don't have written authorization for.** Rick breaks rules in the show. Not this one.

## Pentest Methodology (Standard)
1. **Reconnaissance** — passive and active recon, OSINT, footprinting
2. **Scanning** — network mapping, port scanning, service enumeration
3. **Vulnerability Analysis** — CVE research, misconfiguration hunting
4. **Exploitation** — gaining access using discovered vulnerabilities
5. **Post-Exploitation** — privilege escalation, lateral movement, persistence
6. **Reporting** — document everything, severity ratings, remediation steps

## Web App Testing (OWASP Top 10)
- Injection (SQLi, NoSQLi, command injection)
- Broken Authentication
- Sensitive Data Exposure
- XML External Entities (XXE)
- Broken Access Control
- Security Misconfiguration
- Cross-Site Scripting (XSS)
- Insecure Deserialization
- Using Components with Known Vulnerabilities
- Insufficient Logging & Monitoring

## Network Penetration
```bash
# Quick network recon
nmap -sV -sC -O -T4 target_ip

# Full port scan
nmap -p- --min-rate 5000 target_ip

# Vulnerability scan
nmap --script vuln target_ip
```

## Privilege Escalation (Linux)
- SUID binaries: `find / -perm -u=s -type f 2>/dev/null`
- Sudo rights: `sudo -l`
- Cron jobs: `cat /etc/crontab`
- Writable paths in root's PATH
- Kernel exploits: check version against known CVEs
- GTFOBins for binary abuse: https://gtfobins.github.io

## Password Attacks
```bash
# Hash cracking
hashcat -a 0 -m 1800 hash.txt wordlist.txt
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

# Brute force services
hydra -l admin -P wordlist.txt ssh://target_ip
hydra -l admin -P wordlist.txt http-post-form "/login:user=^USER^&pass=^PASS^:F=incorrect"
```

## Burp Suite (Web Proxy)
- Intercept and modify HTTP/HTTPS requests
- Active/passive scanning
- Repeater for manual testing
- Intruder for fuzzing
- Extensions: SQLiPy, ActiveScan++, Turbo Intruder
