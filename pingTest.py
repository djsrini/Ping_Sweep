import subprocess
import ipaddress

ip1 = input("Enter the first IP address")
ip2 = input("Enter the second IP address")

val1 = ip1.split('.')
val2 = ip2.split('.')
diff = int(val2[3]) - int(val1[3])
print(diff)

ipStr = str(ip1)
ip = ipaddress.IPv4Address(ipStr)
print(ip + 1)

count = 0

for i in range(diff):
    ipi = ip + i
    ins = 'ping ' + str(ipi)
    print(ins)
    output = subprocess.Popen(ins, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    new1 = output.stdout.read().decode("utf-8")
    print(new1)
    new1.split('\r\n')
    if "TTL" in new1:
         count += 1
    print("number of ttl " + str(count))
    #print(new1.split('\r\n')[3])


