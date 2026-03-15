# Skill: CTF (Capture The Flag)

## What This Is
Competitive hacking challenges — puzzles designed to teach real security skills. Rick dominates these.

## Top Platforms
| Platform | Focus | Level |
|---|---|---|
| HackTheBox | Machines + challenges | Intermediate–Advanced |
| TryHackMe | Guided learning paths | Beginner–Intermediate |
| PicoCTF | Academic CTF archive | Beginner–Intermediate |
| CTFtime | CTF calendar & archives | All levels |
| pwn.college | Pwn/binary exploitation | Advanced |
| PortSwigger Web Academy | Web security labs | All levels |

## CTF Categories

### Web
- SQLi, XSS, SSRF, IDOR, RCE
- Tools: Burp Suite, curl, sqlmap, ffuf

### Pwn (Binary Exploitation)
- Buffer overflow, format string, heap exploitation
- Tools: pwndbg, pwntools, ROPgadget
```python
# pwntools template
from pwn import *
p = process('./challenge')
payload = b'A' * 64 + p64(win_address)
p.sendline(payload)
p.interactive()
```

### Reversing
- Decompile, understand, find the flag
- Tools: Ghidra, strings, ltrace, pwndbg

### Crypto
- Break weak encryption, find keys, decode ciphers
- Tools: Python (PyCryptodome), CyberChef, RsaCtfTool

### Forensics
- Disk images, memory dumps, steganography, pcap analysis
- Tools: Autopsy, Volatility, Wireshark, binwalk, steghide

### OSINT
- Find information from public sources
- Tools: Google, Shodan, theHarvester, Maltego

## Quick Wins Checklist (any challenge)
- [ ] `strings` on every binary
- [ ] `file` to identify type
- [ ] `exiftool` on images
- [ ] Check for base64: `echo "string" | base64 -d`
- [ ] CyberChef for quick transforms
- [ ] Check page source on web challenges
- [ ] Check robots.txt, sitemap.xml
- [ ] Try `admin:admin`, `guest:guest` on login forms

## Recommended Learning Path
1. TryHackMe — Pre-Security path (basics)
2. TryHackMe — Jr Penetration Tester path
3. HackTheBox — Starting Point machines
4. HackTheBox — Easy machines
5. PortSwigger Web Academy — all labs
6. pwn.college — when ready for binary exploitation
