N,B = input("N과 B를 입력해주세요: ").split() #N이 수고 B가 진법
B = int(B)
length = len(str(N))

num_str = str(N)
num_arr = []
for digit in num_str:
    if digit.isdigit():
        num_arr.append(int(digit))
    else:
        num_arr.append(ord(digit)-55)

i = 0
ans = 0
a = length
while(i<length):
    ans += num_arr[i] * (B**(a-1))
    i += 1
    a -= 1

print(ans)