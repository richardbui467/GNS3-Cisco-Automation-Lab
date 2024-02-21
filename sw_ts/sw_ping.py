import os

f = open('myswitches.txt')
os.system('echo "This is a log for ICMP requests" > sw_ping_log.txt')

for sw in f:
        sw = sw.strip()
        os.system('ping -q -c 3 ' + sw + ' >> sw_ping_log.txt')
        print('Pinging ' + sw + '...')

print('Results have been saved to sw_ping_log.txt')
