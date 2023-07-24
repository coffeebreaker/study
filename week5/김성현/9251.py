# 2차원 배열을 사용합니다
# 각각의 문자열이 한 index를 차지하고 dp[][] 이런 형태로 만들어 줍니다
# 한 문자를 다음 문자의 한 글자가 지나가면서 나랑 같은게 있나??? 하면서 쭉 지나가겠죠??
# 만약에 같은게 있다면 그 인덱스를 가지는 dp의 값을 그 전값에서 더해줍니다 -> dp에서 당연한거겠죠? 점화식이니
# 근데 같지 않으면 2가지 방법으로 나눠서 합니다
# (1) first라는 문자를 index a까지 가지고 있는데 second문자의 index인 b까지를 검색한 값까지 구한 dp값과
# (2) first라는 문자를 index a-1까지 가지고 있는데 second문자의 index인 b+1까지를 검색한 값까지 구한 dp값을
# 비교를 해줘서 큰 값으로 만들어줍니다
# why ? -> 같지 않기 때문에 +1을 해줄 필요가 없는데
# (1)번과 (2)번에서 first문자index를 하나 늘려서 보든 아니면 second문자index를 하나 늘려서 보든 어차피 지금은 그 값(문자)가
# 동일하지 않다는 걸 알고있기 때문에 (1)번과(2)번의 결과 같으로 그 다음을 유추 가능하다는 거죠.
# 그래서 쭉 진행해서 마지막에 도달하는 dp의 값을 전달을 하면 됩니다.

# 보통 생각해야하는것 (리스트, 튜플 등 문제에서 주는 값)이 하나이기 때문에 보통 dp를 for문 하나로만 해결했잖아요?
# 생각해야하는게 2개니까 for문 2개를 이용해서 풀면 됩니다

import sys
input = sys.stdin.readline
first, second = input().rstrip(), input().rstrip()

dp = [[0] * (len(second)+1) for _ in range(len(first)+1)]

for i in range(1,len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1] == second[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])
