# 문제
# 어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부른다. 예를 들어 79,197과 324,423 등이 팰린드롬 수이다.

# 어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다.

# 출력
# 첫째 줄에 조건을 만족하는 수를 출력한다.

N = int(input())


def is_prime(n):
    # 예외 처리
    if n <= 1:
        return False

    # n이 2, 3이면 당연히 소수
    elif n <= 3:
        return True

    # n이 2의 배수이거나 3의 배수이면 소수 아님
    elif n % 2 == 0 or n % 3 == 0:
        return False

    # 그 외의 경우를 위해 i에 5 할당
    i = 5

    # 2와 3을 제외한 모든 소수는 6의 배수 앞이나 뒤에 위치한다는 수학적 원리 이용
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    # 위 모든 경우가 아닐 때 n은 소수임.
    return True


def is_pallindrome(n):
    if len(str(n)) <= 1:
        return True
    elif n[0] != n[-1]:
        return False
    else:
        return is_pallindrome(n[1:-1])


while True:
    if is_prime(N) and is_pallindrome(str(N)):
        print(N)
        break
    else:
        N += 1
