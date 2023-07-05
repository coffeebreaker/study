# 1644
target = int(input())

prime_list = []
visited = [False] * (target + 1)
for head in range(2, target + 1):
    if not visited[head]:
        prime_list.append(head)
        for cur in range(head, target + 1, head):
            visited[cur] = True

prime_sum = [0] * (len(prime_list) + 1)
for idx, prime in enumerate(prime_list):
    prime_sum[idx + 1] = prime_sum[idx] + prime

left, right, end = 0, 1, len(prime_sum)
cnt = 0
while right < end:
    cur_sum = prime_sum[right] - prime_sum[left]
    if cur_sum < target:
        right += 1
    elif cur_sum > target:
        left += 1
    else:
        cnt += 1
        right += 1

print(cnt)
