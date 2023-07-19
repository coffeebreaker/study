n = int(input())
rope = []
for i in range(n) :
    rope.append(int(input()))
rope.sort(reverse=True)
max_result = 0
for i in range(n) :
    max_result = max(max_result, rope[i] * (i + 1))
print(max_result)
