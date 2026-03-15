# Skill: Reverse Engineering

## What This Is
Taking apart compiled software to understand how it works — without the source code.

## Tools
| Tool | Use Case |
|---|---|
| Ghidra | Free NSA decompiler — excellent for most binaries |
| IDA Pro | Industry gold standard (expensive but worth it) |
| Binary Ninja | Modern, scriptable, great UI |
| radare2 | CLI-based, extremely powerful, steep learning curve |
| pwndbg | GDB plugin for exploit development |
| ltrace/strace | Trace library/system calls at runtime |
| strings | Quick win — dump readable strings from binary |
| file | Identify file type and architecture |

## Static Analysis Workflow
```bash
# 1. What are we looking at?
file target_binary
strings target_binary | grep -i "password\|key\|flag\|admin"

# 2. Check imports/exports
nm -D target_binary
objdump -d target_binary | head -100

# 3. Open in Ghidra
# File → New Project → Import binary → Auto-analyze → Start reversing
```

## Dynamic Analysis
```bash
# Run with strace to see syscalls
strace ./target_binary

# Trace library calls
ltrace ./target_binary

# GDB with pwndbg
gdb ./target_binary
break main
run
info registers
x/20xw $rsp    # examine stack
```

## Common Targets
- Malware analysis (in isolated VM only)
- CTF challenges (pwn, reversing categories)
- License key validation bypass (authorized/research only)
- Protocol reverse engineering (proprietary binary protocols)
- Firmware analysis (IoT devices, routers)

## Firmware Analysis
```bash
# Extract firmware
binwalk -e firmware.bin

# Check for hardcoded creds
grep -r "password\|passwd\|admin" extracted/

# File system analysis
find extracted/ -name "*.conf" -o -name "*.sh"
```

## CTF Tips
- Check for strings, XOR obfuscation, base64 first — low-hanging fruit
- Use Ghidra's decompiler — reads cleaner than raw ASM for most people
- Look for `main()`, `strcmp()`, `check_password()` type functions
- Dynamic analysis often faster than static for simple challenges
