# ScanoPort 🛡️

A modular, dependency-free CLI TCP port scanner written in Python 3. Designed for lightweight network reconnaissance, baseline security assessments, and custom scanner integration.

---

## Key Capabilities ⚡

* **Modular Design**: Clean separation between argument parsing, target resolution, and network interaction.
* **Flexible Input Specifications**: Accepts individual ports, arbitrary comma-separated lists, range boundaries, or default top-port profiles.
* **Domain & IP Resolution**: Native IPv4/IPv6 address parsing and hostname resolution.
* **Zero External Dependencies**: Built entirely on standard Python 3 core modules (`socket`, `sys`, `ipaddress`).

---

## Demo 

![ScanoPort Demo](https://raw.githubusercontent.com/alpha-bet-404/ScanoPort/main/DEMO/Demo.gif)

---

## Installation & Deployment 📦
```
git clone https://github.com/alpha-bet-404/ScanoPort.git
cd ScanoPort
chmod +x scanoport
```

# Optional: Create system-wide binary link
```
sudo ln -s $(pwd)/scanoport /usr/local/bin/scanoport
```
---

## Usage Syntax & Examples 🎯

# Basic usage
```
scanoport <Target_IP_or_Domain> [Port_Specification]
```
# Single target port
```
scanoport 192.168.1.1 80
```
# Arbitrary port list
```
scanoport scanme.nmap.org 22,80,443,8080
```
# Sequential port range
```
scanoport 10.10.10.1 1-1024
```
---

## Project Structure 🏗️

ScanoPort
```
  ├── scanoport           # Primary execution CLI interface
  ├── check.py            # Target resolution and input validation logic
  ├── TypesForScan.py     # Socket connection handling & scan loops
  └── ports.py            # Static port list mappings & top-ports data
```
---

## License 📜

Distributed under the MIT License.
