import itertools
import sys

input = sys.stdin.readline


def calc(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num1 < 0:
            return -(-num1 // num2)
        else:
            return num1 // num2


num_size = int(input())
num_list = [int(i) for i in input().split()]

ops = [int(j) for j in input().split()]
op_list = ['+'] * ops[0] + ['-'] * ops[1] + ['*'] * ops[2] + ['/'] * ops[3]
op_perm_list = list(set(itertools.permutations(op_list)))


total_list = []
for op_perm in op_perm_list:
    cur_total = num_list[0]
    for num, op in zip(num_list[1:], op_perm):
        cur_total = calc(cur_total, num, op)
    total_list.append(cur_total)

print(max(total_list))
print(min(total_list))
