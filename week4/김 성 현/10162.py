total = int(input())

# 첫번째는 150초 60초 10초

#사실 그냥 수학 형태로 풀어도됨
"""
a = total // 300
b = (total % 300) // 60
c = ((total % 300) % 60 ) // 10
d = (((total % 300) % 60 ) % 10) 
if d == 0:
    print(a,b,c)

else:
    print(-1)
"""
# 위와 같이 하면 런타임이 생긴다

# 2차원 배열로 이걸 [총 합이 되는 것][해당 어떤 버튼을 사용한 것인지]
# 각각을 뽑아줘야 하니까 조건에 맞게 해주는 것이 중요하다


def dpdp(n):
    dp = [float('inf')]*(n+1)
    dp[0] =0
    button = [0,300,60,10]
    for i in range(1, n+1):
        for choice in range(1,4):
            if i>= button[choice]:
                #지금의 것이랑 그전에서 총 choice를 뺀거에서 total을 더해준것 비교
                dp[i] = min(dp[i], dp[i-button[choice]]+1)
    if dp[n] == float('inf'):
        return -1
    choices = [0] * 3
 
    while n>0:
        for choice in range(1,4):
            # 오름차순이니까 가장 제일 큰걸 뺴주고 순서대로 진행해야 하는데 최소를 만족하도록 해줘야한다
            # 가장 큰것을 빼주는데 total보다는 커야하고 빼줘도 dp의 값들이 유지가 되어야한다
            if n >= button[choice] and dp[n] == dp[n-button[choice]]+1:
                choices[choice-1]+=1
                n -= button[choice]
                break
    return choices
    
answer = dpdp(total)

if answer == -1:
    print(-1)
else:
    print(answer[0], answer[1], answer[2])
