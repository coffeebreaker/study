cur = [int(n) for n in input().split()]
dest = [1, 2, 3, 4, 5]
while cur != dest:
    for i in range(4):
        if cur[i] > cur[i + 1]:
            tmp = cur[i + 1]
            cur[i + 1] = cur[i]
            cur[i] = tmp
            print(' '.join(map(str, cur)))
