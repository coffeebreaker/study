branch = list(map(int, input().split()))
i = 0
while sorted(branch) != branch:
    if branch[i] > branch[i+1]:
        branch[i], branch[i+1] = branch[i+1], branch[i]
        print(*branch)
    i = (i+1)%4