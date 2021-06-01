"""What is an defanged ip address: When sending the contents of an artifact within an email notification,
any web and IP addresses are automatically “defanged” to prevent the user from inadvertently
clicking a malicious link.

To convert an IP address to a defanged IP address, we need to replace “.” with “[.]”.
During coding interviews, a standard problem for changing an IP address is that you receive a valid IP address,
you must return a defanged version of that IP address."""

def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address

ipaddress=ip_address(input("Enter the ip address: ")) #ip_address("1.1.2.3")
print(ipaddress)