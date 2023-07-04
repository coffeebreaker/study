n = int(input())
p = list(map(int, input().split()))

i = n - 1
while i > 0 and p[i-1] >= p[i]: # 오름차순이 깨지는 위치 찾기
    i -= 1
if i == 0:  #마지막인경우
    print(-1)
else:
    j = n - 1 
    while p[j] <= p[i-1]:
        j -= 1
    p[i-1], p[j] = p[j], p[i-1]    # 교환
    p[i:] = sorted(p[i:])# 오름차순 정렬
    print(*p)