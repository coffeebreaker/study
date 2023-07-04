n = int(input())
cur_perm = [int(num) for num in input().split()]

i = n - 2
while i >= 0 and cur_perm[i] >= cur_perm[i + 1]:
    i -= 1

if i == -1:
    print(-1)
else:
    j = n - 1
    while cur_perm[j] <= cur_perm[i]:
        j -= 1
    cur_perm[i], cur_perm[j] = cur_perm[j], cur_perm[i]
    cur_perm = cur_perm[:i+1] + cur_perm[n-1:i:-1]
    print(' '.join(str(e) for e in cur_perm))
