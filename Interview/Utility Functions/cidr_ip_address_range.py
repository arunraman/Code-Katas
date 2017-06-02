
import sys, struct, socket

str = '192.168.1.0/24'

(ip, cidr) = str.split('/')
cidr = int(cidr)
host_bits = 32 - cidr
i = struct.unpack('>I', socket.inet_aton(ip))[0] # note the endianness
start = (i >> host_bits) << host_bits # clear the host bits
end = i | ((1 << host_bits) - 1)

for i in range(start, end):
    print(socket.inet_ntoa(struct.pack('>I',i)))