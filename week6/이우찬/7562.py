#실버1 정답!
# 문제
# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?



# 입력
# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

# 출력
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

# 1 0 0 0 2 0 0 0
# 0 0 1 0 0 0 0 0
# 2 1 0 0 2 0 0 0
# 0 2 0 2 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 2 0 0 0 0 0 0 0

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(a,b):
    # visited = [[False for _ in range(M)] for _ in range(N)]
    q = []
    q.append([a,b])

    while q:
        x,y = q.pop(0)
        for i in range(8):
            #8방위 시작
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<L and 0<=ny<L and matrix[nx][ny]!=1:
                if matrix[nx][ny] == 2:
                    res = count[x][y] + 1
                    return res
                # 안만나면 증가
                else:
                    matrix[nx][ny] = 1
                    q.append([nx,ny])
                    count[nx][ny] = count[x][y] + 1

#input
T = int(input())
for _ in range(T):
    L = int(input())
    matrix = [[0 for _ in range(L)] for _ in range(L)]
    x,y = map(int, input().split())
    matrix[x][y] = 1
    z,w = map(int, input().split())
    if x==z and y==w:
        print(0)
        pass
    else:
        matrix[z][w] = 2
        count = [[0 for _ in range(L)] for _ in range(L)]
        res = bfs(x,y)
        print(res)