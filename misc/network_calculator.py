__author__ = 'win7vm'
from IPy import IP

ip_s =raw_input('input an ip or net-range: ')
ips = IP(ip_s)
if len(ips) >1:
	print ('net address: %s' % ips.net())
	print ('netmask: %s' % ips.netmask())
	print ('broadcast: %s' % ips.broadcast())
	print ('reverse address: %s' % ips.reverseNames()[0])
	print ('sbunet: %s' % len(ips))
else:
	print ('reverse address: %s' % ips.reverseName())
print ('hexadrcimal: %s' % ips.strHex())
print ('binary: %s' % ips.strBin())
print ('iptype: %s' % ips.iptype())

