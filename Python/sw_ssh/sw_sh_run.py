from netmiko import ConnectHandler
from myswitches import switches

#ABOUT
#Gathers running-config from switches

for sw in switches:
    net_connect = ConnectHandler(**sw)
    net_connect.enable()
    output = net_connect.send_command('sho run')
    with open('runcfg.txt', 'a') as log:
        log.write(output)
