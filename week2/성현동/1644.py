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

left, right = 0, 1
end, count = len(prime_sum), 0
while right < end:
    cur_sum = prime_sum[right] - prime_sum[left]
    if cur_sum < target:
        right += 1
    elif cur_sum > target:
        left += 1
    else:
        count += 1
        right += 1

print(count)
