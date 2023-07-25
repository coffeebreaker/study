stairs = [0]
num_stairs = int(input())
for _ in range(num_stairs):
    stairs.append(int(input()))

num_stairs += 1
dp = [0] * num_stairs
dp[1] = stairs[1]

if num_stairs > 2:
    dp[2] = stairs[1] + stairs[2]
for n in range(3, num_stairs):
    dp[n] = max(stairs[n] + stairs[n - 1] + dp[n - 3], stairs[n] + dp[n - 2])

print(dp[num_stairs - 1])
