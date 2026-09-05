#!/bin/python3

import sys
import socket
import subprocess
import ports
from datetime import datetime




def scan_top_1000_port(ip,port):
	print("-"*5)
	print(f"\033[33mScanning :\033[0m {ip}")
	print("\033[33mDATE:\033[0m "+str(datetime.now()))
	print("-"*5,"\n")
	ip = str(ip)
	print(f'---PORT\tSTATE---\n')
	top_ports = ports.top(port)
	try:
		for scanp in top_ports:
			scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			exitcode = scan.connect_ex((ip,scanp))
			if exitcode == 0:
				print(f'\033[32m[*]\033[0m {scanp}\t\033[32mOPEN\033[0m')

			else:
				print(f'\033[31m[x]\033[0m {scanp}\t\033[31mCLOSE\033[0m')
		sys.exit(0)
	except KeyboardInterrupt:
		print(f'\n\n\033[31mBye!!\033[0m')
		sys.exit(1)

def port_scan_range(ip,port):
	print("-"*5)
	print(f"\033[33mScanning :\033[0m {ip}")
	print("\033[33mDATE:\033[0m "+str(datetime.now()))
	print("-"*5,"\n")
	port = port.split('-')
	ip = str(ip)
	print(f'---PORT\tSTATE---\n')
	try:
		if len(port) == 2:
			num1 = int(port[0])
			num2 = int(port[1])+1
			for scanp in range(num1,num2):
				scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(1)
				exitcode = scan.connect_ex((ip,scanp))
				if exitcode == 0:
					print(f'\033[32m[*]\033[0m {scanp}\t\033[32mOPEN\033[0m')
				else:
					print(f'\033[31m[x]\033[0m {scanp}\t\033[31mCLOSE\033[0m')
			sys.exit(0)

		else:
			print("\n\033[31m[x]\033[0m Invaild RANGE")

	except KeyboardInterrupt:
		print(f'\n\n\033[31mBye!!\033[0m')
		sys.exit(1)






def Scan_specific_ports(ip,port):
	print("-"*5)
	print(f"\033[33mScanning :\033[0m {ip}")
	print("\033[33mDATE:\033[0m "+str(datetime.now()))
	print("-"*5,"\n")
	port = port.split(',')
	ip = str(ip)
	print(f'---PORT\tSTATE---\n')
	try:
		for scanp in port:
			scanp = int(scanp)
			scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			exitcode = scan.connect_ex((ip,scanp))
			if exitcode == 0:
				print(f'\033[32m[*]\033[0m {scanp}\t\033[32mOPEN\033[0m')
			else:
				print(f'\033[31m[x]\033[0m {scanp}\t\033[31mCLOSE\033[0m')
		sys.exit(0)

	except KeyboardInterrupt:
		print(f'\n\n\033[31mBye!!\033[0m')
		sys.exit(1)






def scan_one_port(ip,port):
	ip = str(ip)
	port = int(port)
	print("-"*5)
	print(f"\033[33mScanning :\033[0m {ip}")
	print("\033[33mDATE:\033[0m "+str(datetime.now()))
	print("-"*5,"\n")
	try:
		scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		exitcode = scan.connect_ex((ip,port))
		if exitcode == 0:
			print(f'---PORT\tSTATE---\n')
			print(f'\033[32m[*]\033[0m {port}\t\033[32mOPEN\033[0m')
		else:
			print(f'\033[31m[x]\033[0m {port}\t\033[31mCLOSE\033[0m')
		sys.exit(0)

	except KeyboardInterrupt:
		print(f'\n\n\033[31mBye!!\033[0m')
		sys.exit(1)
