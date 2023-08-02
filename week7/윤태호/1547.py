ball = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    if not ball in (a, b):
        continue
    else:
        ball = b if a == ball else a
print(ball)