# 한번에 1칸 or 한번에 2번 앞앞으로 + dp[i-1] or dp[i-1] + dp[i-2] , 첫번째를 a 두번쨰를 b로
# 한번에 3칸 연속으로 안됨  -> a,b가 순서 상관없이 연속으로 x 
# 마지막은 무조건 밟는다

import sys
input = sys.stdin.readline

n = int(input())
stairs= list([0]*(n+1))
dp= list([0]*(n+1))
for i in range(n):
    stairs[i] = int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
for i in range(2,n):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
print(dp[n-1])

# 풀이 -> 연속3칸은 안되니까 1칸을 밟거나 2칸을 밟는것으로 간주하고 생각한다