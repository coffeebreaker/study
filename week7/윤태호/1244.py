n = int(input())
switch = [-1] + list(map(int, input().split()))
for _ in range(int(input())):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        i = 1
        while num*i <= n:
            switch[num*i] = (switch[num*i]+1) % 2
            i += 1
    # 여자
    else:
        i = 0
        while (num-i-1 >= 1) and (num+i+1 <= n) and (switch[num-i-1] == switch[num+i+1]):
            i += 1

        for j in range(num-i, num+i+1):
            switch[j] = (switch[j]+1) % 2

switch = switch[1:]
for i in range((len(switch)//20)+1):
    print(*switch[20*i:20*(i+1)])
