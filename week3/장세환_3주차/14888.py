import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
num = list(map(int,input().split()))
sign = list(map(int,input().split()))

max_result = -1000000000
min_result = 1000000000


def dfs(depth, result, plus, minus ,multiply, divide) :
    if depth == n :
        global max_result, min_result
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if plus :
        dfs(depth + 1 , result + num[depth] , plus - 1, minus , multiply , divide)
    if minus :
        dfs(depth + 1 , result - num[depth] , plus, minus - 1, multiply, divide)

    if multiply :
        dfs(depth + 1 , result * num[depth] , plus, minus, multiply - 1, divide)
    if divide :
         dfs(depth + 1 , int(result / num[depth]) , plus, minus, multiply, divide - 1)

dfs(1 , num[0], sign[0], sign[1], sign[2], sign[3])

print(max_result)
print(min_result)