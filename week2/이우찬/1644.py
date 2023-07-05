N = int(input("정수를 입력하세요: "))

is_prime = [True] * (N+1)
is_prime[0] = is_prime[1] = False

primes = []
for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i*2, N+1, i):
            is_prime[j] = False

for i in range(2, N+1):
    if is_prime[i]:
        primes.append(i)

count = 0
start = 0
end = 0
sum = 0

while(True):
    if(start==len(primes)):
        break
    elif(sum > N):
        sum -= primes[start] # sum이 N보다 클 때 start 빼주고, start 포인터 이동 
        start += 1
    elif(end == len(primes)):
        end -= 1
        pass
    elif(sum == N):
        count += 1 # sum == N일때
        sum -= primes[start]
        start += 1
    else:
        sum += primes[end] #sum이 N보다 작을 때 더하고 end 포인터 이동
        end += 1


print(count)    