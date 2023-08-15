# https://www.acmicpc.net/problem/1874

import sys
input = sys.stdin.readline

n = int(input())
input_num = [int(input()) for i in range(n)]
stack = []
stack_num = 1
answer = []

for num in input_num:
    while stack_num <= num:
        stack.append(stack_num)
        answer.append('+')
        stack_num += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        break
else:
    for op in answer:
        print(op)
