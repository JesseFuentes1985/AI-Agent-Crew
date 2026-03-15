# Skill: OSINT (Open Source Intelligence)

## What This Is
Gathering intelligence from publicly available sources. No hacking needed — just knowing where to look.

## The OSINT Framework
Start here: https://osintframework.com

## People & Identity
```bash
# Username search across platforms
sherlock username

# Email breach check (via CLI)
holehe email@example.com

# Phone number lookup
phoneinfoga scan -n "+1XXXXXXXXXX"
```

## Domain & IP Recon
```bash
# DNS enumeration
amass enum -d target.com
subfinder -d target.com

# DNS records
dig target.com ANY
dnsx -d target.com -a -mx -txt

# WHOIS
whois target.com

# Reverse IP lookup — find other domains on same server
# Use: viewdns.info, hackertarget.com

# Shodan
shodan host IP_ADDRESS
shodan search "org:target company"
```

## Google Dorking
```
# Find login pages
site:target.com inurl:login

# Find exposed files
site:target.com filetype:pdf confidential

# Find subdomains
site:*.target.com

# Find email addresses
"@target.com" filetype:xlsx OR filetype:csv

# Exposed cameras
inurl:/view/index.shtml
inurl:top.htm inurl:currenttime
```

## Social Media Intelligence
- LinkedIn: org charts, employee names, tech stack (job postings reveal everything)
- Twitter/X: real-time sentiment, executive statements
- GitHub: accidentally committed credentials, internal tooling, employee activity
- Instagram/Facebook: physical location leaks, schedule patterns

## Metadata Extraction
```bash
# Extract metadata from files
exiftool image.jpg
exiftool document.pdf

# Strips GPS coords, device info, author names from docs
```

## Dark Web Monitoring
- Tor Browser for .onion exploration (legal, authorized research)
- Paste sites: Pastebin, ghostbin, hastebin for leaked data
- Have I Been Pwned API: check breach exposure

## OSINT Ethics
- Only collect publicly available data
- Don't access private systems to gather intel
- Use intel for defense and authorized research only
