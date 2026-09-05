#!/bin/python3

import sys
import socket
import ipaddress
import TypesForScan


import os
import sys

def check_root():
	if os.geteuid() != 0:
		print("\n\033[31m[-] Not running as root. Please run with sudo.\033[0m")
		sys.exit(1)

def start(target,port):

	try:
		ip = ipaddress.ip_address(target)
		type_of_scan(ip,port)
	except ValueError:
		try:
			print(f"\n\033[33m[*]\033[0m \033[1;32m{target}\033[0m TO <IP> ??")
			ip = socket.gethostbyname(target)
			print(f"[$] {target} TO {ip}")
			type_of_scan(ip,port)

		except socket.gaierror:
			print('\n\033[31mInvaild:\033[0m \033[33m<IP>\033[0m')
			print('\033[31mExample:\033[0m \033[32mpython3 scanoport \033[1;32m192.168.1.0\033[0m OR \033[1;32mgoogle.com\033[0m <PORT>')
			sys.exit(1)
def type_of_scan(ip,port):
	if port == '':
		TypesForScan.scan_top_1000_port(ip,port)
	elif '-' in port:
		TypesForScan.port_scan_range(ip,port)
	elif ',' in port:
		TypesForScan.Scan_specific_ports(ip,port)
	elif port.isdigit():
		TypesForScan.scan_one_port(ip,port)
	else:
		TypesForScan.ask_usr_for_port(ip,port)
