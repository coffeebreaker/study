import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
result = [1] * n
if n == 1 :
    print("1")
elif n == 2 :
    if nums[1] > nums[0] :
        print("2")
    else :
        print("1")
else :
    result[0] = 1
    if nums[1] > nums[0] :
        result[1] = 2
    for i in range(2, n) :
        for j in range(0, i) :
            if nums[i] > nums[j] :
                result[i] = max(result[i], result[j] + 1)
    print(max(result))