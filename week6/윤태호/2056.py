import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

cost = [0]
pre = [[] for _ in range(n+1)]
adj = [[] for _ in range(n+1)]

for number in range(1, n+1):
    line = list(map(int, input().split()))
    cost.append(line.pop(0))
    for i in range(line.pop(0)):
        adj[line[0]].append(number)
        pre[number].append(line.pop(0))

# 해당 작업이 끝났는 지를 저장하는 리스트
checked = [False]*(n+1)

# 시작과 끝 시간을 저장하는 리스트
working_at = [[0, 0] for _ in range(n+1)]

# BFS를 위한 덱 선언 [작업 번호, 현재 시간]
q = deque()
for i in range(1, n+1):
    if not pre[i]:
        q.append([i, 0])

time = 0
# BFS
while q:
    task, time = q.popleft()

    # 해당 task의 시작시간과 끝나는 시간 설정
    working_at[task][0] = time
    working_at[task][1] = time + cost[task]

    # checked True로 변경, 시간도 작업 완료 시간으로 변경
    checked[task] = True
    time += cost[task]

    # non-checked이면서 가능한 작업 덱에 집어넣음
    for a in adj[task]:
        for t in pre[a]:
            if not checked[t]:
                break
        else:
            if not checked[a]:
                # 선행 작업의 끝나는 시간 중 최댓값 계산
                max_time = -1
                for b in pre[a]:
                    max_time = max(max_time, working_at[b][1])
                q.append([a, max_time])
    
ans = -1
for w in working_at:
    ans = max(ans, w[1])

print(ans)