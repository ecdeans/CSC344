# Author: Eva Deans
# Date: 3/19/24
# Resources:
# https://www.theunterminatedstring.com/python-bits-and-bytes/
# https://stackoverflow.com/questions/22571259/split-a-string-into-n-equal-parts
# https://www.geeksforgeeks.org/string-slicing-in-python/
# Program Purpose: To route an IP address to the correct port, as based on the
# information in a text file.

class TableEntry:
    """
    Represents an entry in a Routing Table.
    """
    def __init__(self, ip, prefix, subnet, port):
        """
        Initializes a TableEntry object.
        """
        # to avoid creating another object with port 6, made ip a list
        self.ip = [ip]
        self.prefix = prefix
        self.subnet = self.calcSubnet(self.prefix)
        self.port = port

    # Getters
    def getIP(self):
        """
        Returns all IPs contained by a TableEntry object.
        """
        for i in self.ip:
            return i

    def getPrefix(self):
        """
        Returns the prefix of a TableEntry object.
        """
        return self.prefix

    def getSubnet(self):
        """
        Returns the subnet of a TableEntry object.
        """
        return self.subnet

    def getPort(self):
        """
        Returns the port of a TableEntry object.
        """
        return self.port

    # Setters
    def setIP(self, ip):
        """
        Sets the IP of a TableEntry object.
        """
        self.ip = ip

    def setSubnet(self, subnet):
        """
        Sets the subnet of a TableEntry object.
        """
        self.subnet = subnet

    def setPort(self, port):
        """
        Sets the port of a TableEntry object.
        """
        self.port = port


    # Other Methods

    def ipAppend(self, ip):
        """
        Appends an IP to a TableEntry object's IP list.
        """
        self.ip.append(ip)


    def calcSubnet(self, prefix):
        """
        Calculates the subnet of a TableEntry object.

        :param prefix: int: The prefix of a TableEntry object
        :return: str: The subnet mask in format "xxx.xxx.xxx.xxx".
        """
        # create list of 32 bits
        subnet = [0] * 32

        # set number of prefix bits to 1
        for i in range(prefix):
            subnet[i] = 1

        # convert to single str of bits
        subnet = [str(i) for i in subnet]
        subnetString = "".join(subnet)
        # iterates in steps of 8 and extracts each substring to store in variable
        parts = [subnetString[i:i + 8] for i in range(0, len(subnetString), 8)]

        subnet = []
        for i in parts:
            # turn to decimal
            subnet.append(int(i, base=2))

        # turn to str and join on "."
        subnet = [str(i) for i in subnet]
        finalSubnet = ".".join(subnet)
        #
        return finalSubnet
