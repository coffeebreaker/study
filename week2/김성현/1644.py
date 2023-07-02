n = int(input())
primes = []
# 소수 리스트 만들어주기
def find_primes(n):
    prime_check = [True] * (n+1)    
    prime_check[0] = prime_check[1] = False    
    p = 2
    while p * p <= n:
        if prime_check[p]:
            for i in range(p * p, n+1, p):
                prime_check[i] = False
        p += 1    
    for i in range(2, n+1):
        if prime_check[i]:
            primes.append(i)

# 투포인터 활용
def two_pointer(prime):
    cnt =0
    start = 0
    end =0
    point =0
    for i in range(len(prime)):
        while point < n and end < len(prime):
            point+=prime[end]
            end+=1
        if point == n:
            cnt +=1
        point -= prime[i]
    print(cnt)
find_primes(n)
two_pointer(primes)
        