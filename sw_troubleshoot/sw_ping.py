import os
from my_switches.py import switches

#ABOUT
#Allows pinging of all switches & logs results

os.system('echo "This is a log for ICMP requests" > sw_ping_log.txt')
for sw in switches:
        sw = sw.strip()
        os.system('ping -q -c 3 ' + sw + ' >> sw_ping_log.txt')
        print('Pinging ' + sw + '...')

print('Results have been saved to sw_ping_log.txt')
