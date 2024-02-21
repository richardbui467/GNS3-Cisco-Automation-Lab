import telnetlib
import getpass

user = input("Enter telnet username: ")
pw = getpass.getpass()

file = open("myswitches.txt")

sw_num = 0

for IP in file:
        #Open connection & provide Telnet creds
        IP = IP.strip()
        print("Configuring " + (IP))
        tn = telnetlib.Telnet(IP)
        tn.read_until(b"Username: ")
        tn.write(user.encode("ascii") + b"\n")
        if pw:
                tn.read_until(b"Password: ")
                tn.write(pw.encode("ascii") + b"\n")

        #Enter commands into Cisco iOS
        #Leaves user at global config mode after
        config = open("sw_setup.txt")
        for cmd in config:
                tn.write(str(cmd).encode("ascii") + b"\n")

        #Config hostname using variable incrementing each connection
        sw_num += 1
        hostname = "SW" + str(sw_num)
        hostname = hostname.strip()
        tn.write(b"hostname " + str(hostname).encode("ascii") + b"\n")

        #Config VLANs
        for vlan_num in range(20, 40, 10):
                tn.write(b"int vlan" + str(vlan_num).encode("ascii") + b"\n")
                tn.write(b"no shut\n")

        #End to leave interface & global config mode, exit to close connection
        tn.write(b"end\n")
        tn.write(b"wr\n")
        tn.write(b"exit\n")
        print(tn.read_all().decode("ascii"))
