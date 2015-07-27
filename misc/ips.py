__author__ = 'win7vm'
from IPy import IP

print IP('192.168.1.1').version()
#list all available ips in subnet
ip=IP('192.168.0.0/24')
print ip.len()
for x in ip:
	print x
	
#resolve hostname
print ip.reverseName()

# ip type (private or public)
print ip.iptype()

#convert to integer
print ip.int()
# to binary
print ip.strBin()
# to Hex
print ip.strHex()
#convert Hex to normal
print (IP(0xc0a80000))

#convert to network address
print (IP('192.168.5.17').make_net('255.255.255.0'))
print (IP('192.168.1.0-192.168.1.255',make_net=True))
print IP('192.168.1.0/24').strNormal(0)
print IP('192.168.1.0/24').strNormal(1)
print IP('192.168.1.0/24').strNormal(2)
print IP('192.168.1.0/24').strNormal(3)

#check if a network contains another
print IP('10.0.0.0/24') in IP('10.0.0.0/16')
print IP('192.168.1.23') in IP('192.168.0.0/16')

#check 2 networks if overlap
print IP('192.168.0.0/23').overlaps('192.168.0.0/14')
print IP('192.168.0.0/23').overlaps('192.168.0.0/28')




