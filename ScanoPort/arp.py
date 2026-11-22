#!/bin/python3

import sys
import time
import socket
import ipaddress


def get_ip(iface, host):
	# UDP connect sends nothing, it only tells us our own IP on this interface
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, iface.encode())
	s.connect((host, 80))
	ip = s.getsockname()[0]
	s.close()
	return ip


def arp_scan(iface, target):
	# no target = the /24 network of this interface
	if target == '':
		try:
			target = get_ip(iface, '8.8.8.8') + '/24'
		except OSError:
			print(f'\n\033[31m[x]\033[0m Cannot get the IP of \033[33m{iface}\033[0m, write the network')
			print('\033[31mExample:\033[0m \033[32msudo scanoport -a eth0 \033[1;32m192.168.1.0/24\033[0m')
			sys.exit(1)

	try:
		net = ipaddress.ip_network(target, strict=False)
	except ValueError:
		print('\n\033[31mInvaild:\033[0m \033[33m<NETWORK>\033[0m')
		print('\033[31mExample:\033[0m \033[32msudo scanoport -a eth0 \033[1;32m192.168.1.0/24\033[0m')
		sys.exit(1)

	if net.version != 4:
		print('\n\033[31m[x]\033[0m ARP works with IPv4 only')
		sys.exit(1)

	try:
		my_ip = get_ip(iface, str(next(net.hosts())))
	except (OSError, StopIteration):
		print(f'\n\033[31m[x]\033[0m Cannot use interface \033[33m{iface}\033[0m for {net}')
		sys.exit(1)

	print("-"*5)
	print(f"\033[33mARP Scanning :\033[0m {net} ({iface})")
	print("\033[33mDATE:\033[0m "+time.ctime())
	print("-"*5,"\n")
	print(f'{"---IP":<20}MAC---\n')

	try:
		sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
		sock.bind((iface, 0))
		sock.settimeout(0.2)
	except OSError:
		print('\033[31m[x]\033[0m Cannot open raw socket (need root + Linux)')
		sys.exit(1)

	my_mac = sock.getsockname()[4]

	try:
		for host in net.hosts():
			# ethernet header + ARP request
			packet = b'\xff'*6 + my_mac + b'\x08\x06'
			packet += b'\x00\x01\x08\x00\x06\x04\x00\x01'
			packet += my_mac + socket.inet_aton(my_ip)
			packet += b'\x00'*6 + socket.inet_aton(str(host))
			sock.send(packet)

		found = []
		end = time.time() + 2
		while time.time() < end:
			try:
				reply = sock.recv(2048)
			except socket.timeout:
				continue
			# ARP reply only
			if len(reply) < 42 or reply[20:22] != b'\x00\x02':
				continue
			mac = reply[22:28].hex(':')
			ip = socket.inet_ntoa(reply[28:32])
			if ipaddress.ip_address(ip) in net and ip not in found:
				found.append(ip)
				print(f'\033[32m[*]\033[0m {ip:<16}{mac}')

		print(f'\n\033[33mHosts up:\033[0m {len(found)}')
		sys.exit(0)

	except KeyboardInterrupt:
		print(f'\n\n\033[31mBye!!\033[0m')
		sys.exit(1)
