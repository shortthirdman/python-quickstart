import psutil
from tabulate import tabulate

class Network_Details(object):
    def __init__(self):
        self.parser = psutil.net_if_addrs()

    def  __repr__(self):
        self.interfaces = []
        self.address_ip = []
        self.netmask_ip = []
        self.broadcast_ip = []
        self.address_family = []

        for interface_name, interface_addresses in self.parser.items():
            self.interfaces.append(interface_name)
            for address in interface_addresses:
                if str(address.family) == 'AddressFamily.AF_INET':
                    self.address_ip.append(address.address)
                    self.address_family.append(address.family)
                    self.netmask_ip.append(address.netmask)
                    self.broadcast_ip.append(address.broadcast)

        data = {"Interface:" : [*self.interfaces],
            "Address-Family" : [*self.address_family],
            "IP-Address:" : [*self.address_ip],
            "NetMask:" : [*self.netmask_ip],
            "Broadcast-IP" : [*self.broadcast_ip]
            }
        return tabulate(data, headers="keys", showindex="always", tablefmt="pretty")

if __name__ == "__main__":
    print(Network_Details())
