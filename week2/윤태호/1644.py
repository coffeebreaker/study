# 문제
# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.

# 3 : 3 (한 가지)
# 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
# 53 : 5+7+11+13+17 = 53 (두 가지)
# 하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다.
# 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.

# 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 4,000,000)

# 출력
# 첫째 줄에 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.

N = int(input())
prime_list = list()


def find_primes(N):
    prime_check = [True] * (N+1)
    prime_check[0] = prime_check[1] = False

    p = 2
    while p * p <= N:
        if prime_check[p]:
            for i in range(p*p, N+1, p):
                prime_check[i] = False
        p += 1
    for i in range(2, N+1):
        if prime_check[i]:
            prime_list.append(i)


def count_sum(prime_list):
    if not prime_list:  # prime_list가 비어 있으면 0을 출력하고 함수를 종료합니다.
        print(0)
        return

    count = 0
    start = 0
    end = 0
    sum = prime_list[0]

    while True:
        if start > end:
            break

        if sum < N:
            end += 1
            if end >= len(prime_list):
                break
            sum += prime_list[end]

        elif sum > N:
            sum -= prime_list[start]
            start += 1

        else:
            count += 1
            sum -= prime_list[start]
            start += 1

    print(count)


find_primes(N)
count_sum(prime_list)
