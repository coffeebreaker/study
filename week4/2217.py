n = int(input())
a = [0] *(n+1)
for i in range(n):
    a[i] = int(input())
a.sort()
answer =0
# n, n-1, n-2, ..... 1개 사용한다 루프
# a, b, c, d, .......z 를 할수 있는 루프
# n*a, n-1*c ..... z*1 중에 min 찾자
for i in range(1,n+1):
    if answer < a[n-i+1]* i:
        answer = a[n-i+1] * i
print(answer)