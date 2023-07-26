import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t) :
    k = int(input()) # k층
    n = int(input()) # n호 -> 사실상 n - 1호
    # a층 b호 살고 싶어?
    # a - 1층 sum(1호 ~ b호) 보다 커야함
    # k층 n호에는 몇 명?
    # k - 1층 sum(1호 ~ b호) 보다 커야함
    f0 = [i for i in range(1, n + 1)] #0층의 0호에는 1명, 0층의 n - 1호에는 n명
    for k in range(0, k) : #k층까지 계산
        for i in range(1, n) : #n - 1호까지 계산
            f0[i] += f0[i - 1]
    print(f0[-1])
