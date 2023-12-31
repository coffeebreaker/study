#골드4
# 문제
# 수행해야 할 작업 N개 (3 ≤ N ≤ 10000)가 있다. 각각의 작업마다 걸리는 시간(1 ≤ 시간 ≤ 100)이 정수로 주어진다.

# 몇몇 작업들 사이에는 선행 관계라는 게 있어서, 어떤 작업을 수행하기 위해 반드시 먼저 완료되어야 할 작업들이 있다. 이 작업들은 번호가 아주 예쁘게 매겨져 있어서, K번 작업에 대해 선행 관계에 있는(즉, K번 작업을 시작하기 전에 반드시 먼저 완료되어야 하는) 작업들의 번호는 모두 1 이상 (K-1) 이하이다. 작업들 중에는, 그것에 대해 선행 관계에 있는 작업이 하나도 없는 작업이 반드시 하나 이상 존재한다. (1번 작업이 항상 그러하다)

# 모든 작업을 완료하기 위해 필요한 최소 시간을 구하여라. 물론, 서로 선행 관계가 없는 작업들은 동시에 수행 가능하다.

# 입력
# 첫째 줄에 N이 주어진다.

# 두 번째 줄부터 N+1번째 줄까지 N개의 줄이 주어진다. 2번째 줄은 1번 작업, 3번째 줄은 2번 작업, ..., N+1번째 줄은 N번 작업을 각각 나타낸다. 각 줄의 처음에는, 해당 작업에 걸리는 시간이 먼저 주어지고, 그 다음에 그 작업에 대해 선행 관계에 있는 작업들의 개수(0 ≤ 개수 ≤ 100)가 주어진다. 그리고 선행 관계에 있는 작업들의 번호가 주어진다.

# 출력
# 첫째 줄에 모든 작업을 완료하기 위한 최소 시간을 출력한다.

# []
# 1: 5 | 0
# 2: 1 | 1 | 1
# 3: 3 | 1 | 2
# 4: 6 | 1 | 1
# 5: 1 | 2 | 2 4
# 6: 8 | 2 | 2 4
# 7: 4 | 3 | 3 5 6
# # [x][0] 으로 작업 시간 확인
# # [x][1] 로 작업 갯수 확인
# # [x][2] 부터로 작업 확인

# 0: []
# 1: [2,4]
# 2: [3,5,6]
# 3: [7]
# 4: [5,6]
# 5: [7]
# 6: [7]
# 7: []

#bfs 돌려서 가장 max time 구하면 되는건가?
#일단 선행이 없는 놈은 예외 처리 해줘야됨
#전체 bfs의 maxtime 구하고 선행이 없는놈이랑 max한번 더해주면 될듯?

def bfs():
    q = []
    q.append(1)
    visited[1] = True
    time[1] = works[1][0]
    while q :
        x = q.pop(0)
        for i in link[x]:
            if visited[i]==False :
                if max(time[k] for k in works[i][2:])==time[x]:
                    q.append(i)
                    visited[i] = True
                    time[i] = time[x] + works[i][0]


#input
N = int(input())

works = [[] for _ in range(N+1)]
for i in range(1, N+1):
    works[i] = list(map(int, input().split()))
for i in range(1, N+1):
    works[i][2:] = sorted(works[i][2:])

link = [[] for _ in range(N+1)]

for i in range(2, N+1):
    if works[i][1]==1:
        link[works[i][2]].append(i)
    else:
        for j in range(2, len(works[i])):
            link[works[i][j]].append(i)

visited = [False] * (N+1)
time = [0] * (N+1)
bfs()
res = max(time)
zero_list = []
for i in range(1, N+1):
    if works[i][1]==0:
        zero_list.append(works[i][0])

result = max(res,max(zero_list))

print(result)