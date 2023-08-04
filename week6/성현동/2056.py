from collections import deque, defaultdict

job_num = int(input())

graph = defaultdict(list)
time = [0] * (job_num + 1)
in_degree = [0] * (job_num + 1)
start_time = [0] * (job_num + 1)

for i in range(1, job_num + 1):
    info = [int(n) for n in input().split()]
    time[i], cnt = info[0], info[1]
    if cnt != 0:
        graph[i] = info[2:]
        for ahead in graph[i]:
            in_degree[ahead] += 1

q = deque()
for i in range(1, job_num + 1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    job = q.popleft()
    for before_job in graph[job]:
        in_degree[before_job] -= 1
        start_time[before_job] = max(start_time[before_job], start_time[job] + time[job])
        if in_degree[before_job] == 0:
            q.append(before_job)

max_time = max(start_time[i] + time[i] for i in range(1, job_num + 1))
print(max_time)
