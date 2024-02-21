from netmiko import ConnectHandler
from my_switches import switches
from sw_cfgs.py import *

x = 0

#SSH to each SW 
for sw in switches:
    x += 1 
    net_connect = ConnectHandler(**sw)
    #net_connect.send_command('hostname sw-a' + str(x)) 
    net_connect.send_config_set(basic_cfg)
