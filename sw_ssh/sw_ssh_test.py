from netmiko import ConnectHandler
from my_switches import switches 

#SSH to each SW
for sw in switches:
    net_connect = ConnectHandler(**sw)
    output = net_connect.send_command('sh ip int bri')
    print('SSH connection successful to ' + sw['ip'])
    print(output)
