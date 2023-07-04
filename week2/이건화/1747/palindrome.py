import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    word = str(n)
    if word == word[::-1] :
        return True
    else:
        return False

n = int(input())
if n == 1 :
    print(2)
    exit()
i = n
while True:
    if is_palindrome(i):
        if is_prime(i):
            print(i)
            exit()
    i += 1
# def eratos() :
#     n = 1004001
#     prime_numbers = list()
#     a = [False, False] + [True] * (n-1)
#     for i in range (2, n // 2 + 1) :
#         if a[i] == True :
#             for j in range(2 * i, n+1, i) :
#                     a[j] = False
#     return [i for i in range(2, n + 1) if a[i] == True]

# n = int(input())
# primes = eratos()
# for i in primes :
#     if i > n :
#         if is_palindrome(i) == True :
#             print(i)
#             break

        