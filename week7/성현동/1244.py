def boy(n):
    for i in range(1,switch_num+1):
        if i % n == 0:
            state[i] ^= 1


def girl(n):
    for i in range(1, switch_num+1):
        if i == 1:
            state[n] ^= 1
        left, right = n - i, n + i
        if left <= 0 or right > switch_num:
            return
        if state[left] != state[right]:
            return
        state[left] ^= 1
        state[right] ^= 1


switch_num = int(input())
state = [0]+[int(n) for n in input().split()]
for _ in range(int(input())):
    gender, num = map(int, input().split())
    if gender == 1:
        boy(num)
    else:
        girl(num)

for i in range(1, switch_num + 1):
    print(state[i], end=" ")
    if i % 20 == 0:
        print()
