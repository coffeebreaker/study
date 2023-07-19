
"""
from collections import deque
from itertools import permutations

# 먼저 로봇청소기의 위치를 정해주고
# 먼지의 위치도 dust에 담아 준다
# 왔던길을 다시 갈 수도 있으니 check가 필요없고 dp처럼 누적 합으로 만들어주자
# bfs로 *로 가는 거리를 모두다 만들어놓자

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i, j, check):
    check[i][j] = 1
    q = deque()
    q.append([(i, j)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            cx = x + dx[k]
            cy = y + dy[k]
            if 0 <= cx < m and 0 <= cy < n and check[cx][cy] == 0 and graph[cx][cy] != 'x':
                q.append((cx, cy))
                check[cx][cy] = check[x][y] + 1
#check에는 어느지점까지의 최소거리가 모두저장되어 있다        
                    
#bfs로 거리를 찾아주고, dust를 찾으면 그 찾은 것들을 각각 iteration으로 해주고 가장 값이 작은 것을 찾아준다
# 청소기에서 먼지 까지의 거리를 찾아주고 그 먼지에서 다른 먼지로를 찾아준다
# 청소기 -> 먼지 1 -> 먼지 3 -> 먼지 2 or 청소기 -> 먼지 2 -> 먼지 1 -> 먼지 3 등


def initialize(check):
    for i in range(n):
        for j in range(m):
            check[i][j] = 0


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        graph = [list(input()) for _ in range(m)]
        check = [[0] * m for _ in range(n)]
        dust = []
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 'o':
                    rx, ry = i, j
                elif graph[i][j] == '*':
                    dust.append((i, j))
        total = len(dust)
        valid = [[0] * total for _ in range(total)]
# dust[0] 은 0번째 먼지, dust[1]은 1번째 먼지 등등
# dust의 값을 bfs에 넣고 이 check[dust값]을 하나씩 조합해야한다
        for i in range(total):
            initialize(check)
            bfs(dust[i][0], dust[i][1], check)
            for j in range(total):
                valid[i][j] = check[dust[j][0]][dust[j][1]]

        dp = [[0] * total for _ in range(total)]
        for i in range(1, total):
            for j in range(total):
                dp[i][j] = valid[i][j] + min(dp[i - 1][k] for k in range(total) if k != j)
        print(min(dp[total - 1]))
"""

from collections import deque
from itertools import permutations

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(i, j, check):
    check[i][j] = 1
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            cx = x + dx[k]
            cy = y + dy[k]
            if 0 <= cx < n and 0 <= cy < m and check[cx][cy] == 0 and graph[cx][cy] != 'x':
                q.append((cx, cy))
                check[cx][cy] = check[x][y] + 1


def initialize(check):
    for i in range(n):
        for j in range(m):
            check[i][j] = 0


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    else:
        graph = [list(input()) for _ in range(n)]
        check = [[0] * m for _ in range(n)]
        dust = []

        # m은 y, n은 x
        for i in range(m):
            for j in range(n):
                if graph[j][i] == 'o':
                    rx, ry = j, i
                elif graph[j][i] == '*':
                    dust.append((j, i))
        total = len(dust)
        valid = [[0] * total for _ in range(total)]

        for i in range(total):
            initialize(check)
            bfs(dust[i][0], dust[i][1], check)
            for j in range(total):
                if i!=j:
                    valid[i][j] = check[dust[j][0]][dust[j][1]]

# permutation을 통해서 0 123등으로

        candidate =[]
        permutation = list(permutations(range(1,total+1)))
        
        i=0
        current=0
        for per in permutation:
            total = 0
            for p in per:
                total +=valid[current][p]
                current = p
            candidate.append(total)
    print(min(candidate))
            
            

            

