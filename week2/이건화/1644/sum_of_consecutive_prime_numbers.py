def eratos() :
    n = 4000000
    prime_numbers = list()
    a = [False, False] + [True] * (n-1)
    for i in range (2, n // 2 + 1) :
        if a[i] == True :
            for j in range(2 * i, n+1, i) :
                    a[j] = False
    return [i for i in range(2, n + 1) if a[i] == True]

n = int(input())
prime_numbers = eratos()
answer = 0
start = 0
end = 0
while end <= len(prime_numbers):
    temp_sum = sum(prime_numbers[start:end])
    if temp_sum == n:
        answer += 1
        end += 1
    elif temp_sum < n:
        end += 1
    else:
        start += 1
print(answer)