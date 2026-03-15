# Skill: Network Security

## What This Is
Locking down networks, analyzing traffic, and making sure nothing sneaks in or out without permission.

## Network Recon & Mapping
```bash
# Discover live hosts
nmap -sn 192.168.1.0/24

# Service version detection
nmap -sV -sC 192.168.1.1

# OS fingerprinting
nmap -O target_ip

# Shodan CLI (internet-facing assets)
shodan search "hostname:target.com"
```

## Packet Analysis (Wireshark/tcpdump)
```bash
# Capture all traffic on interface
tcpdump -i eth0 -w capture.pcap

# Filter by host
tcpdump -i eth0 host 192.168.1.1

# Filter HTTP
tcpdump -i eth0 port 80 or port 443

# Read capture file
tcpdump -r capture.pcap
```

## Firewall (iptables / ufw)
```bash
# UFW basics
ufw enable
ufw allow 22/tcp
ufw deny 23/tcp
ufw status verbose

# iptables — block IP
iptables -A INPUT -s malicious_ip -j DROP

# Log dropped packets
iptables -A INPUT -j LOG --log-prefix "DROPPED: "
```

## VPN & Tunneling
- WireGuard — modern, fast, simple config
- OpenVPN — battle-tested, more complex
- SSH tunneling: `ssh -L 8080:internal-server:80 user@jump-host`
- Reverse shells for testing: `nc -lvnp 4444`

## Wireless Security
```bash
# Put card in monitor mode
airmon-ng start wlan0

# Scan for networks
airodump-ng wlan0mon

# Capture handshake (for authorized testing)
airodump-ng -c 6 --bssid TARGET_BSSID -w capture wlan0mon

# Crack WPA2 (authorized testing only)
aircrack-ng -w rockyou.txt capture-01.cap
```

## Zero Trust Principles
1. Never trust, always verify
2. Least privilege access — minimum permissions needed
3. Assume breach — act like attackers are already inside
4. Micro-segmentation — isolate everything that can be isolated
5. Log everything — you can't detect what you don't see

## Home Network Hardening
- Separate IoT devices on their own VLAN
- Change default router credentials (obviously)
- Disable WPS (it's broken)
- Use WPA3 if available, WPA2-AES minimum
- Regularly audit connected devices
- Keep router firmware updated
