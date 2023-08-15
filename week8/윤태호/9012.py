# https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    line = input()
    stack = []
    
    for a in line:
        if not stack and a==')':
            stack.append(a)
            break
        elif a=='(':
            stack.append(a)
        elif a==')':
            stack.pop(0)

    if stack:
        print('NO')
    else:
        print('YES')