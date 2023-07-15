total = 1000
n = int(input())

choice = [500,100,50,10,5,1]
dp = [float('inf')]*10000
dp[0] = 0
#내가 고려해야하는 것들을 한번씩 다해주자 -> 그리디
# 그중에서 max나 min이 되는 것들만을 살려주자 -> dp
for i in range(1,total-n+1):
    for jandon in range(6):
        if i >= choice[jandon]:
            dp[i] = min(dp[i], dp[i-choice[jandon]]+1)
print(dp[total-n])

