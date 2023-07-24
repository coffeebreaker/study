# 퀸은 앞 뒤 옆 대각선 어떤 방향이든지 원하는 만큼 이동이 가능하다
# 자신의 기준으로 가로 세로 대각선에는 아무것도 놓으면 안된다

#2차원을 pca로 진행 -> 차원 축소

#2차원 짜리를 1차원으로 index와 값으로 생각해보자

# i는 몇번째인지와 
# j는 그 뒤에 비교해줄 것인데
# i와 j의 차이 만큼 perm[i]에 더해주고 빼주는 값의 인덱스는 대각선이라서 안된다 -> check로 확인
# 가로 세로는 permutation으로 방지 가능
from itertools import permutations
n = int(input())

def n_queens(n):
    a = list(range(n))
    candidate = permutations(a, n)
    perfect_candidate = []
    for perm in candidate:
        check = [[True] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if (perm[i] + j - i) <= n-1:
                    check[j][perm[i] + j - i] = False
                if (perm[i] - j + i) >= 0:
                    check[j][perm[i] - j + i] = False
        for i in range(n):
            if check[i][perm[i]] is False:
                break
        else:
            perfect_candidate.append(perm)
    print(len(perfect_candidate))

n_queens(n)



        


