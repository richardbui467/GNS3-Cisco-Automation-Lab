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

def wr_cmd(x):
    net_connect.send_command(x)

#File containing basic configs
basic_cfg = [
    'banner motd $This is a virtual switch used for testing$', 
    'ip default-gateway 192.168.1.17', 
    'vlan 20',
    'name Private',
    'vlan 30',
    'name Guest',
]

sw_a1_cfg = [
    'int g3/2',
    'switchport mod acc',
    'switchport acc vlan 20',
    'int g0/2',
    'switchport mod acc',
    'switchport acc vlan 30',
]

sw_a2_cfg = [
    'int g0/0',
    'switchport mod acc',
    'switchport acc vlan 20',
    'int g0/1',
    'switchport mod acc',
    'switchport acc vlan 30',
]

sw_a3_cfg = [
    'int g0/0',
    'switchport mod acc',
    'switchport acc vlan 20',
    'int g0/1',
    'switchport mod acc',
    'switchport acc vlan 30',
]

x = 0

#SSH to each SW 
for sw in switches:
    x += 1 
    net_connect = ConnectHandler(**sw)
    #net_connect.send_command('hostname sw-a' + str(x)) 
    net_connect.send_config_set(basic_cfg)
