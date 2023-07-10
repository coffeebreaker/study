nanjeng = []

# 키 입력 받기
for _ in range(9):
    height = int(input())
    nanjeng.append(height)

start, end = 0, 8
nanjeng.sort()
sum = 0
while start < end:
    sum = sum(nanjeng)
    sum -= (nanjeng[start] + nanjeng[end])
    
    if sum == 100:
        break
    elif sum > 100:
        start += 1
    else:
        end -= 1

nanjeng.pop(start)
nanjeng.pop(end - 1)

for height in nanjeng:
    print(height)
