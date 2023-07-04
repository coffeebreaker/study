input_line= input()
inputs = input_line.split()
n = inputs[0]
b = int(inputs[1])
sum = 0
for i in range(len(n)) :
    if(n[i].isdigit()):
        num = int(n[i])
    else :
        num = ord(n[i]) - ord('A') + 10
    if(num < b) :
        sum *= b
        sum += num
print(sum)

