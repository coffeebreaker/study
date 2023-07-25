test_case = int(input())
numbers = list(map(int, input().split()))

dp = [1] * (len(numbers))
max_v = 1
for i in range(1, len(numbers)):
    for j in range(i - 1, -1, -1):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    max_v = max(max_v, dp[i])

print(max_v)
