woods = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]
while woods != answer :
    for i in range(4) :
        if woods[i] > woods[i + 1] :
            woods[i], woods[i + 1] = woods[i + 1], woods[i]
            print(*woods)