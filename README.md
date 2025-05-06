# py-pinghosts
This repository contains python script for pinging live hosts in a network (DnsHostName or IPaddress)

The script uploads every hosts wrote in hosts.txt and sends 4 ICMP Echo Requests, known commonly as "ping requests".
The ping command is wrote for being executed from a Windows machine ("ping -n 4 ...") but it can be modified for Linux/MacOS machines.
For each ping request the result is stored under "ping_results.csv"

Requirements: Python3 installed on main host, ICMP requests enabled in the environment (firewall rules can easly block this protocol). 
