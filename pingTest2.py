import os
import socket
import ipaddress

ip1 = input("Enter the first IP address")
ip2 = input("Enter the second IP address")

val1 = ip1.split('.')
val2 = ip2.split('.')
diff = int(val2[3]) - int(val1[3])
print(diff)

ipStr = str(ip1)
ip = ipaddress.IPv4Address(ipStr)

for i in range(diff+1):
    ipi = ip + i
    ins = 'ping ' + str(ipi)
    ping = os.system(ins)
    try:
        output = socket.gethostbyaddr(str(ipi))
        print(output[0])
    except OSError:
        print("DNS Unavailable")
    print(ping)

