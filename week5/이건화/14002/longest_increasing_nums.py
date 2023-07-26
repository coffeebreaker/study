import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

if n == 1 :
    print("1")
    print(nums[0])

elif n == 2 :
    if nums[1] > nums[0] :
        print(2)
        print(nums[0], nums[1])
    else :
        print(1)
        print(nums[0])

else :
    result = []
    for _ in range(n) :
        temp = []
        result.append(temp)

    #0번
    result[0].append(nums[0])
    #1번
    if nums[1] > nums[0] :
        result[1] = result[0].copy()
        result[1].append(nums[1])
    else :
        result[1].append(nums[1])
    #2번
    for i in range(2, n) :
        result[i].append(nums[i])
        for j in range(0, i) :
            if nums[i] > nums[j] :
                if len(result[i]) < len(result[j]) + 1 :
                    result[i] = result[j].copy()
                    result[i].append(nums[i])
    # print(result)
    max_i = 0
    max_l = 0
    for i in range(0, n) :
        if len(result[i]) > max_l :
            max_l = len(result[i])
            max_i = i
    print(max_l)
    print(*result[max_i])