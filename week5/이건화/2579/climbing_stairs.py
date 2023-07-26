import sys
input = sys.stdin.readline
n = int(input())
stairs = []
points = [0] * (n)
for _ in range(n) :
    num = int(input())
    stairs.append(num)
if len(stairs) == 1 :
    print(stairs[0])
elif len(stairs) == 2:
    print(stairs[0] + stairs[1])
else :
    points[0] = stairs[0]
    points[1] = stairs[0] + stairs[1]
    points[2] = stairs[2] + max(stairs[0], stairs[1])
    for i in range(3, n) :
        points[i] = max(points[i - 2] + stairs[i], points[i - 3] + stairs[i - 1] + stairs[i])
    print(points[n - 1])