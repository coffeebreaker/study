import sys
input = sys.stdin.readline
n = int(input())
suyul = list(map(int,input().split()))

dp = list([1]*(n+1))

if n ==1:
    print(1)

else:
        for i in range(n):
            for j in range(i):
                if suyul[i] > suyul[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        print(max(dp))

#처음부터 끝까지의 배열에 대해서 검사를 하는데
#그 배열의 처음부터 끝까지도 검사를 해주는데, 그 배열의 마지막것과 그 다음의 것의 차이를 통해서 dp를 계산해 줍니다
