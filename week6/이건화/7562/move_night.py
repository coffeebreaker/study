import sys
from collections import deque

input = sys.stdin.readline
test_n = int(input())
option = [(-2, +1), (-1, +2), (+1, +2), (+2, +1), (+2, -1), (+1, -2), (-1, -2), (-2, -1)]

def bfs(start, dest, size) :
    #세팅
    distance = [[-1 for _ in range(size)] for _ in range(size)]
    #하나씩 가보면서 queue에 넣자
    visit_queue = deque()
    visit_queue.append(start)
    while visit_queue :
        # 사실상 방문하는 행위
        n = visit_queue.popleft()
        # 방문한 곳이 도착지일 때
        if n == dest :
            return distance[dest[0]][dest[1]]
        # 방문한 곳이 도착지가 아닐 때!
        else :
            # 현재 방문한 곳 주변을 살펴보자
            for i in range(8) :
                next_y = n[0] + option[i][0]
                next_x = n[1] + option[i][1]
                # 갈 수 있는 곳이라면!
                if 0 <= next_y < size and 0 <= next_x < size :
                    # 안 간 곳이라면!
                    if distance[next_y][next_x] == -1 :
                        # 갈 곳의 거리를 정해주고!
                        distance[next_y][next_x] = distance[n[0]][n[1]] + 1
                        # 방문할 곳이라고 정해주자
                        visit_queue.append([next_y, next_x])

for _ in range(test_n):
    size = int(input())
    start = list(map(int, input().split()))
    dest = list(map(int, input().split()))
    result = bfs(start, dest, size)
    print(result + 1)