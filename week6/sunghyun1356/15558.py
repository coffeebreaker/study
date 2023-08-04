import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
map = [list(input().rstrip())for _ in range(2)]
visited = [[False] * n for _ in range(2)]



def bfs():
    q = deque()
    q.append((0,0))
    # n 칸 만큼 있기때문에 n번 만큼 진행해준다
    for i in range(n):
        # while q랑 똑같습니다만 n만큼 반복해주니 이렇게 해줍니다.
        for j in range(len(q)):
            x,y = q.popleft()
            # 앞으로 갈건지 뒤로 갈건지 아니면 k칸 앞의 반대쪽으로 갈건지를 결정해야한다
            for nx, ny in (x,y-1), (x,y+1), (not x, y+k):
                if ny >= n :
                    print(1)
                    return
                # 그게 아니라
                # i만큼 -> 충분히 i칸만큼 (즉 1씩 앞으로 가고) 가고, 가본곳이 아니라 안전한 곳이다?
                if ny > i and not visited[nx][ny] and map[nx][ny] =='1':
                    q.append((nx,ny))
                    visited[nx][ny]=True
    # 근데 이게 ny가 n보다 초과다? 이새끼는 지나친거이니 패스

    print(0)

bfs()