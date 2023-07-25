size = int(input())
seq = list(map(int, input().split()))
dp = [0] * size
dp_seq = [-1] * size
for i in range(size):
    dp[i] = 1
    for j in range(i):
        if seq[j] < seq[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            dp_seq[i] = j
ans = max(dp)
p = [i for i, x in enumerate(dp) if x == ans][0]


def show(p):
    if p == -1:
        return
    show(dp_seq[p])
    print(seq[p], end=' ')


print(ans)
show(p)
