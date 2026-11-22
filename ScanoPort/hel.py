#!/bin/python3

def help():

    print("""
ScanoPort - Modular TCP Port Scanner

Usage:
  sudo scanoport <Target> [Port/Range/List]
  sudo scanoport -a <Interface> [Network]

Options & Examples:
  sudo scanoport 192.168.1.1          Scan default top ports
  sudo scanoport 192.168.1.1 80       Scan a single port
  sudo scanoport example.com 22,80,443 Scan specific ports list
  sudo scanoport 10.10.10.1 1-1000    Scan a range of ports
  sudo scanoport -a eth0              ARP scan the network of eth0
  sudo scanoport -a eth0 192.168.1.0/24  ARP scan a specific network
  
""")
