n = int(input())
rope = []
for _ in range(0, n) :
    num = int(input())
    rope.append(num)
rope.sort()
m = 0
for i in range(0, n) :
    m = max(m, rope[n - 1 - i] * (i + 1))
print(m)