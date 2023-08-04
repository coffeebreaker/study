from collections import deque
import sys

N, k = map(int, input().split())
map = [list(map(int, list(input()))) for _ in range(2)]

q = deque([(0, 0, 0)])
visited = [[False]*N for _ in range(2)]
visited[0][0] = True

while q:
    x, y, t = q.popleft()

    # 앞으로
    try:
        if (map[x][y+1] == 1) and not visited[x][y+1]:
            visited[x][y+1] = True
            q.append((x, y+1, t+1))
    except IndexError:
         print(1)
         sys.exit()
    
    # 뒤로
    try:
        if (y-1 > t) and (y-1 >= 0) and (map[x][y-1] == 1) and not visited[x][y-1]:
            visited[x][y-1] = True
            q.append((x, y-1, t+1))
    except IndexError:
         print(1)
         sys.exit()

    # 다른 칸 k 뒤로
    try:
        if (map[(x+1)%2][y+k] == 1) and not visited[(x+1)%2][y+k]:
                visited[(x+1)%2][y+k] = True
                q.append(((x+1)%2, y+k, t+1))
    except IndexError:
         print(1)
         sys.exit()

print(0)