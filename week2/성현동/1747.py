#1747
def is_palindrome(n):
    return n == n[::-1]


def is_prime(value):
    for div in range(2, int(value ** 0.5) + 1):
        if value % div == 0:
            return False
    return True


n = input()
val = int(n)

while True:
    if val == 1:
        print(2)
        break

    if is_palindrome(n) and is_prime(val):
        print(n)
        break
    else:
        val += 1
        n = str(val)
