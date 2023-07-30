import sys
from collections import deque
input = sys.stdin.readline

# 첫번째까 걸리는 시간
# 두번째 부터 선행관계에 있는 작업들의 개수와 번수

# ex) 4 3 3 5 6 이면 3, 5, 6이 끝나고 진행되어야하는 4만큼 걸리는 것이 3개가 있다
# 그럼 i 번째가 끝나야지 진행되는 것들을 따로 저장해서 시간대를 체크 한다. 

# dp[3].append(4)이런씩으로 진행한다.
# 두번째 만큼 dp[line[i][3:4].append(느낌?)]

# 그럼 예시에서
#graph[0] =5
#gprah[1] = 1, 6
#graph[2] = 3,1,8
#graph[3] = 4
#graph[4] = 



n = int(input())
times =[0] *(n+1)
graph =[[] for _ in range(n+1)]
for i in range(1,n+1):
    lst = list(map(int, input().split()))
    times[i] = lst[0]
    if lst[1] == 0:
        continue
    for j in lst[2:]:
            graph[i].append(j)
            graph[i] = list(set(graph[i]))

# graph[i]가 끝나야지 실행이 가능하다
#맨처음부터 돌면서 그 값의 times의 값과 지금까지의 값을 비교한다

#dp에는 결국 마지막놈이 끝나야지 실행되는 그 마무리 단계의 시간의 값을 가진다

dp =times.copy()
for i in range(2,n+1):
     time =0
     for j in graph[i]:
        time = max(time, dp[j])
     dp[i] += time
print(max(dp))

