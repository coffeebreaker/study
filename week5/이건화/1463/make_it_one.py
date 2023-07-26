import sys
input = sys.stdin.readline
n = int(input())
result = [0] * (n + 1)
# result[0] = 0, result[1] = 0
# greedy : 10 5 4 2 1
# DP : 10 9 3 1
for i in range(2, n + 1) :
    # 1을 빼는 이유 : 어차피 min에서 최소값 뽑으므로
    # 싹다해보고 최소인 것을 고른다.
    result[i] = result[i-1] + 1
    if i % 2 == 0 :
        result[i] = min(result[i], result[i // 2] + 1)
    if i % 3 == 0 :
        result[i] = min(result[i], result[i // 3] + 1)


print(result[n])

