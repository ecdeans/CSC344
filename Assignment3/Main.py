# Author: Eva Deans
# Date: 3/19/24
# Resources:
# https://www.theunterminatedstring.com/python-bits-and-bytes/
# https://stackoverflow.com/questions/22571259/split-a-string-into-n-equal-parts
# https://www.geeksforgeeks.org/string-slicing-in-python/
# Program Purpose: To route an IP address to the correct port, as based on the
# information in a text file.

from TableEntry import TableEntry

def readFile(filename):
    """
    Read a file.

    :param filename: str: The name of the file being accessed
    :return: list: List of TableEntry Objects
    """
    routingTable = []
    with open(filename, "r") as file:
        for line in file:
            ip, prefix, port = line.strip().split(",")
            newEntry = TableEntry(ip, int(prefix), str(None), int(port))
            # check to see if there are multiple IPs for one port
            if int(port) not in routingTable:
                routingTable.append(newEntry)
            # if multiple IPs, add that IP to the corresponding port's IP list
            elif int(port) in routingTable:
                newEntry.ipAppend(ip)
    return routingTable


def toBinary(address):
    """
    Turns an address into a string representation
    of binary

    :param address: str: The address
    :return: str: The binary
    """
    binary = ""
    # break apart string
    octets = address.split(".")
    for octet in octets:
        # output binary in groups of 8 bits
        binary += "{0:08b}".format(int(octet))
    return binary


def toAddress(binary):
    """
    Turns a string representation of binary into an
    address

    :param binary: str: The binary
    :return: str: The address
    """
    address = ""
    for i in range(0, len(binary), 8):
        # slicing into groups of 8 bits
        octet = binary[i:i + 8]
        # add str version of each octet in decimal to address
        address += str(int(octet, 2)) + "."
    return address[:-1]


def getComparison(ipBin, subnetBin):
    """
    Turns a string representation of binary into an
    address

    :param ipBin: str: Binary for the IP
    :param subnetBin: str: Binary for the subnet
    :return: str: The result of the AND operation on the parameters
    """
    result = ""
    # iterates through IP and subnet strings
    for char in range(len(ipBin)):
        # compares each char in the strings to build result
        if ipBin[char] == "1" and subnetBin[char] == "1":
            result += "1"
        else:
            result += "0"
    return result


def main():
    # Program welcome
    print()
    print("This program either takes a user input IPv4 address, and determines the proper port, \n"
          "or demonstrates the program is working by finding the port for 14-16 preset IPv4 addresses.\n")

    userAnswer = int(input("Type 1 to input your own IPv4 address, and 2 to test the 14-16 addresses: "))

    # For user input IP
    if userAnswer == 1:
        # Get list of TableEntry objects
        routingTable = readFile("test.txt")
        userIP = input("Enter an IP address in the format xxx.xxx.xxx.xxx: ")

        # Set default port to 5
        port = 5
        # Iterate though the routing table to find the correct port
        for i in range(len(routingTable)):
            # perform bitwise AND on input address and subnet
            result = getComparison(toBinary(userIP), toBinary(routingTable[i].getSubnet()))
            # convert result of AND operation to an address
            result = toAddress(result)
            # if address matches the IP of the entry, set port
            if result == routingTable[i].getIP():
                port = routingTable[i].getPort()
                break
        print(f"{userIP} will be routed to port {port}.")
    # For predetermined test IPs
    elif userAnswer == 2:
        userAnswer = int(input("\nType 1 to test with the original routing table, and 2 to test with the altered routing table (Enter 2): "))
        # Without changed port 6
        if userAnswer == 1:
            print("\nYou have chosen to test 14 addresses on the original table.")
            routingTable = readFile("test.txt")
            testList = ["178.62.88.15", "178.62.88.300", "65.0.45.23", "65.0.2.2",
                        "178.62.112.112", "178.62.112.47", "14.123.156.0", "190.3.30.9",
                        "192.196.1.10", "192.168.1.11", "192.168.1.12", "192.168.1.13"]

            port = 5

            print("Testing Addresses... ")
            for ip in testList:
                for i in range(len(routingTable)):
                    # perform bitwise AND on input address and subnet
                    result = getComparison(toBinary(ip), toBinary(routingTable[i].getSubnet()))
                    # convert result of AND operation to an address
                    result = toAddress(result)
                    # if address matches the IP of the entry, set port
                    if result == routingTable[i].getIP():
                        port = routingTable[i].getPort()
                        break
                print(f"{ip} will be routed to port {port}.")
        # With changed port 6
        elif userAnswer == 2:
            print("\nYou have chosen to test 16 addresses on the changed table.")
            routingTable = readFile("testChanged.txt")
            testList = ["178.62.72.210","178.62.72.2", "178.62.88.15", "178.62.88.300",
                        "65.0.45.23", "65.0.2.2", "178.62.112.112", "178.62.112.47",
                        "14.123.156.0", "190.3.30.9", "192.196.1.10", "192.168.1.11",
                        "192.168.1.12", "192.168.1.13"]

            port = 5

            print("Testing Addresses... ")
            for ip in testList:
                for i in range(len(routingTable)):
                    # perform AND on input address and subnet
                    result = getComparison(toBinary(ip), toBinary(routingTable[i].getSubnet()))
                    # convert result of AND operation to an address
                    result = toAddress(result)
                    # if address matches the IP of the entry, set port
                    if result == routingTable[i].getIP():
                        port = routingTable[i].getPort()
                        break
                print(f"{ip} will be routed to port {port}.")



if __name__ == '__main__':
    main()