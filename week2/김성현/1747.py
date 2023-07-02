import math
n = int(input())
# 1~1,000,000

#소수인지 확인하기
def prime(n):
    if n==1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def pel(a):
    if a == a[::-1]:
        return True


for i in range(n, 1003002):
    if prime(i) == True and pel(str(i)) == True:
        print(i)
        break