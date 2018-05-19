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