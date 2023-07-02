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
count = 0


def is_prime(N):
    if N <= 1:
        return False

    elif N <= 3:
        return True

    elif N % 2 == 0 or N % 3 == 0:
        return False

    i = 5
    while i*i <= N:
        if N % i == 0 or N % (i+2) == 0:
            return False
        i += 6

    return True


def next_prime(N):
    i = N + 1
    while True:
        if is_prime(i):
            return i
        else:
            i += 1


#   start_prime = 시작점
sum = 0
start_prime = i = 2

#   end_prime = sum <= N인 끝점
while sum <= N:
    sum += i

    if sum <= N:
        i = next_prime(i)
    else:
        break

end_prime = i

print(f"start_prime = {start_prime}\nend_prime={end_prime}\nsum={sum}")

#   무한루프
while True:
    if start_prime >= end_prime:
        break

    if sum == N:
        count += 1

    if sum >= N:
        sum -= start_prime
        start_prime = next_prime(start_prime)
        print(f"빼기 / sum={sum} / start_prime={start_prime}")
        continue

    if sum <= N:
        end_prime = next_prime(end_prime)
        sum += end_prime
        print(f"더하기 / sum={sum} / end_prime={end_prime}")
        continue


if is_prime(N):
    count += 1

print(count)
