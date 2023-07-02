# n개의 순열의 원소개수를 가지는 것을 만들고 그 다음 것을 찾아주기

from itertools import permutations

n = int(input())
next = tuple(map(int, input().split()))

permutation = list(permutations(range(1,n+1), n))

for i in range(len(permutation)-1):
    if next == permutation[i]:
        print(permutation[i+1])
if next == permutation[len(permutation)-1]:
    print(-1)