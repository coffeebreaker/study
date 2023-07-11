import sys

input = sys.stdin.readline

heights = []
for _ in range(9):
    h = int(input().strip())
    heights.append(h)
heights.sort()

height_sum = sum(heights)
troll_sum = height_sum - 100

troll = []
for i in range(len(heights)):
    for j in range(i + 1, len(heights)):
        if heights[i] + heights[j] == troll_sum:
            troll = [i, j]
            break

for i in range(len(heights)):
    if i == troll[0] or i == troll[1]:
        continue
    print(heights[i])
