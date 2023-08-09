import sys
input = sys.stdin.readline
switch = int(input())
status = list(map(int,input().split()))

n = int(input())
for i in range(n) :
    sex, num = map(int,input().split())

    if sex == 1 :
        for j in range(num - 1, switch ,num) :
            status[j] = 1 - status[j]

    else :
        cnt = 0
        while True :
            left = num - 1 - cnt
            right = num - 1 + cnt
            if left < 0 or right >= switch or status[left] != status[right]: 
                break

            status[left] = 1 - status[left]
            status[right] = 1 - status[right]
            cnt += 1
for i in range(0, switch, 20):
    print(*status[i:i+20])
