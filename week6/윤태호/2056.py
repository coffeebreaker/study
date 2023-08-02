import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

# 해당 작업의 소요 시간 리스트
cost = [0]

# 해당 작업의 선행 작업들 이중 리스트
pre = [[] for _ in range(n+1)]

# 해당 작업의 후행 작업들 이중 리스트
adj = [[] for _ in range(n+1)]

# cost, pre, adj 채우기
for number in range(1, n+1):
    line = list(map(int, input().split()))
    cost.append(line.pop(0))
    for i in range(line.pop(0)):
        adj[line[0]].append(number)
        pre[number].append(line.pop(0))

# 해당 작업이 끝났는 지를 저장하는 리스트
checked = [False]*(n+1)

# 해당 작업의 시작과 끝 시간을 저장하는 이중 리스트
working_at = [[0, 0] for _ in range(n+1)]

# BFS를 위한 덱 선언 ([작업 번호, 해당 작업 시작 시간])
q = deque()

# 처음 시작할 수 있는 작업이 여러 개 일 수 있기 때문에, 선행작업이 없는 작업을 몽땅 집어넣음
for i in range(1, n+1):
    if not pre[i]:
        q.append([i, 0])

# BFS
while q:
    task, time = q.popleft()

    # 해당 task의 시작시간과 끝나는 시간 설정
    working_at[task][0] = time
    working_at[task][1] = time + cost[task]

    # checked True로 변경
    checked[task] = True

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
    
# 항상 마지막 인덱스가 마지막에 끝나진 않기 때문에, 가장 늦은 종료 시각이 답
ans = -1
for w in working_at:
    ans = max(ans, w[1])

print(ans)