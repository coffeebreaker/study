line = int(input())

ropes = []
for _ in range(line):
    ropes.append(int(input()))
ropes.sort()

maximum = 0
min_rope = ropes[0]
for i in range(line):
    cur_max = ropes[i] * (line - i)
    if cur_max > maximum:
        maximum = cur_max

print(maximum)
