import os
import socket
import ipaddress

state = "b"
count = -1
input1 = []

while state != "a":
    count = count + 1
    temp = input("Enter the IP:")
    if temp == "a":
        state = "a"
    else:
        input1.append(temp)

print(input1)

for i in input1:
    ipTemp = i
    print(ipTemp)
    ipSplitter = ipTemp.split(" ")
    print(ipSplitter)
    val1 = ipSplitter[0].split('.')
    val2 = ipSplitter[1].split('.')
    diff = int(val2[3]) - int(val1[3])
    print("The Difference is: " + str(diff))

    ipStr = str(ipSplitter[0])
    ip = ipaddress.IPv4Address(ipStr)

    for j in range(diff+1):
        ipi = ip + j
        ins = 'ping ' + str(ipi)
        ping = os.system(ins)
        try:
            output = socket.gethostbyaddr(str(ipi))
            print(output[0])
        except OSError:
            print("DNS Unavailable")
        print(ping)



