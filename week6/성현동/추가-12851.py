from collections import deque

# easy_version: 1697번
# different_version: 13549번

start, dest = map(int, input().split())
if start == dest:  # 엣지케이스
    print(0)
    print(1)
    exit(0)

# 위치와 이동시간 기록
q = deque([(start, 0)])
# 방문을 여러번 할 수 있으므로, [소요시간,횟수]로 기록
# 일반론: 중복 방문이 가능한 경우, 단순 불리언이 아닌 다차원배열로 여러 정보를 담아야한다
visited = [[-1, 0] for _ in range(100001)]
min_time = 0
while q:
    cur_pos, cur_time = q.popleft()
    for new_pos in [cur_pos - 1, cur_pos + 1, cur_pos * 2]:
        new_time = cur_time + 1
        if not (0 <= new_pos <= 100000):
            continue
        # 원래는 목적지 도달시 exit하는 것이 맞으나, 경로개수를 모두 집계해야하므로 최소 소요시간만 기록하고 계속 진행
        if new_pos == dest and min_time == 0:
            min_time = new_time
        if visited[new_pos][0] == -1:  # 최초방문
            visited[new_pos][0] = new_time
            visited[new_pos][1] = 1
            q.append((new_pos, new_time))
        elif visited[new_pos][0] == new_time:  # n차방문
            visited[new_pos][1] += 1
            q.append((new_pos, new_time))  # 무한루프를 돈다면, visited 처리가 미흡하거나 q에 넣으면 안되는 원소를 삽입한 경우다

print(min_time)
print(visited[dest][1])
