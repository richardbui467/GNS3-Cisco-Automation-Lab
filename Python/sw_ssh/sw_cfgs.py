#Configs that are to be applied to every switch
basic_cfg = [
    'banner motd $This is a virtual switch used for testing$', 
    'ip default-gateway 192.168.1.17', 
    'vlan 20',
    'name Private',
    'vlan 30',
    'name Guest',
]

#Configs applied to switches individually
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
