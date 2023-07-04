n = int(input())
num = list(map(int, input().split()))
for i in range(n - 2, -1, -1) :
    if(num[i] < num[i + 1]) :
        for j in range(n - 1, i, -1) :
            if(num[j] > num[i]) :
                num[i], num[j] = num[j], num[i]
                num[i + 1:] = num[i + 1:][::-1]
                print(*num)
                exit()
print("-1")

