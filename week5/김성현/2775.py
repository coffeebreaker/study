# 부녀회장이 될테야!
# a층의 b호 -> (a-1)층의 1호 부터 b호까지 사람들의 수의 합과 같아야한다
# 1층의 3호면 0층의 1,2,3이니 6
# 2층의 3호면 1층의 1,2,3호의 합 -> 1층의 1호는 1, 2호는 3, 3호는 6 이니 10


import sys
input = sys.stdin.readline
q = int(input())
dp = [list([0]* 15) for _ in range(15)]
for i in range(1,15):
    dp[0][i] = i

for k in range(1,15):
    for n in range(1,15):
        dp[k][n] = sum(dp[k-1][1:n+1])

for _ in range(q):
    k = int(input())
    n = int(input())
    print(dp[k][n])
    

# 풀이
# 미리 dp[][]2차원 배열을 만들어 줍니다. 총 14층짜리 14호짜리이니 만들어주돼
# 처음 값들이 필요하니 0층짜리를 넣어주고
# dp[k][n] = sum(dp[k-1][1:n+1])로 문제의 조건을 만족시키도록 해줍니다