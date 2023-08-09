n = int(input())

cups = [1, 2, 3]
for _ in range(n):
    a, b = map(int, input().split())
    A = cups.index(a)
    B = cups.index(b)
    cups[A], cups[B] = cups[B], cups[A]
print(cups[0])