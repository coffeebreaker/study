from collections import deque

pos_a, pos_b = map(int, input().split())

q = deque([(pos_a, 0)])
visited = [False] * 100001
while q:
    cur_pos, cur_time = q.popleft()
    if cur_pos == pos_b:
        print(cur_time)
        exit()

    if cur_pos < 0 or cur_pos > 100000:
        continue
    if not visited[cur_pos]:
        visited[cur_pos] = True
        q.extend([(cur_pos - 1, cur_time + 1), (cur_pos + 1, cur_time + 1), (cur_pos * 2, cur_time + 1)])
