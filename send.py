#!/usr/bin/env python3
import sys
import argparse
import readline
import time
import string
import random
import datetime
from probe_hdrs import *

def main():
	while(True):
		doit("10.1.1.1", 2, 10000)
		
def doit(dest, teni, nopa):
	randchar = random.choice(string.ascii_letters)
	addr = socket.gethostbyname(dest)
    	dummy = 720*"$"
    
	probe_pkt = Ether(dst='ff:ff:ff:ff:ff:ff', src=get_if_hwaddr('eth0')) / Probe(tenant=teni) / IP(dst=addr) / randchar
    
    	try:
		with open(str(probe_pkt[IP].src)+".s.txt", "a") as myfile:
    			for i in range(nopa):
    				probe_pktt = probe_pkt / (str(i+1)) / dummy
    				sendp(probe_pktt, iface='eth0')
    				myfile.write(randchar+str(i+1)+","+str(time.time())+"\n")
	except KeyboardInterrupt:
		sys.exit()

if __name__ == '__main__':
    main()
