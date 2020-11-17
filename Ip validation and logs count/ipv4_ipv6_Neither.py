import ipaddress

def validateAddresses(addresses):
	lst=[]
	for ip in addresses:
		try:
			if('IPv4' in str(type(ipaddress.ip_address(ip)))):
				lst.append('IPv4')
			elif('IPv6' in str(type(ipaddress.ip_address(ip)))):
				lst.append('IPv6')
			else:
				lst.append('Neither')
		except (Exception) as error:
			lst.append('Neither')
	return lst

addresses=['121.18.19.20','0.12.12.34','121.234.12.12','23.45.12.56','0.1.2.3']
result=validateAddresses(addresses)
print(result)

addresses=['000.012.234.23','1:22:333:4444']
result=validateAddresses(addresses)
print(result)