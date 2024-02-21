from netmiko import ConnectHandler

#Switches
sw_a1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.2',
    'username': 'cisco',
    'password': 'cisco',
}

sw_a2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.3',
    'username': 'cisco',
    'password': 'cisco',
}

sw_a3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.4',
    'username': 'cisco',
    'password': 'cisco',
}

switches = [sw_a1, sw_a2, sw_a3]

#SSH to each SW
for sw in switches:
    net_connect = ConnectHandler(**sw)
    output = net_connect.send_command('sh ip int bri')
    print('SSH connection successful to ' + sw['ip'])
    print(output)
