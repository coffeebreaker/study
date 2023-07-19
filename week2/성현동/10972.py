n = int(input())
string = input()
cur_perm = [int(num) for num in string.split()]

if string == string[::-1]:
    print(-1)
else:
    small = -1
    for i in range(n - 1):
        if cur_perm[i] < cur_perm[i + 1]:
            small = i
    if small == -1:
        print(-1)
    else:
        big = -1
        for i in range(n - 1):
            if cur_perm[small] < cur_perm[i]:
                big = i
        cur_perm[small], cur_perm[big] = cur_perm[big], cur_perm[small]
        cur_perm = cur_perm[:small + 1] + sorted(cur_perm[small + 1:])
        print(' '.join(map(str, cur_perm)))
