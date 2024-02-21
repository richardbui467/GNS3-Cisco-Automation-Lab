from netmiko import ConnectHandler
from my_switches import switches 

#ABOUT
#Tests SSH by opening & closing a connection with all switches

for sw in switches:
    net_connect = ConnectHandler(**sw)
    output = net_connect.send_command('sh ip int bri')
    print('SSH connection successful to ' + sw['ip'])
    print(output)
