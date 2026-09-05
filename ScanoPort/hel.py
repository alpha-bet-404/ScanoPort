#!/bin/python3

def help():

    print("""
ScanoPort - Modular TCP Port Scanner

Usage:
  sudo scanoport <Target> [Port/Range/List]

Options & Examples:
  sudo scanoport 192.168.1.1          Scan default top ports
  sudo scanoport 192.168.1.1 80       Scan a single port
  sudo scanoport example.com 22,80,443 Scan specific ports list
  sudo scanoport 10.10.10.1 1-1000    Scan a range of ports
  
""")
