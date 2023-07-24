import sys
input = sys.stdin.readline

k = int(input())
dp = list([0]*(k+1))
dp[1] =0
for i in range(2,k+1):
    dp[i] = dp[i-1] +1
    if i % 2 ==0:
        dp[i] = min(dp[i], dp[(i//2)] +1)
    if i % 3 ==0:
        dp[i] = min(dp[i], dp[(i//3)] + 1)
print(dp[k])

# 풀이
# 그냥 디폴트 값으로는 i-1해준거에 dp[i-1]+1 = dp[i] 라고 생각해주는데 이게 
# 2나 3으로 나눠지면 나눈 dp값이랑 원래 값이랑 비교를 해서 min값을 도출