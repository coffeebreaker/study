import sys

input = sys.stdin.readline

mushroom_list = []
for _ in range(10):
    mushroom = int(input().strip())
    mushroom_list.append(mushroom)

total = 0
end = len(mushroom_list)
for i in range(end):
    one_more = total + mushroom_list[i]
    if one_more - 100 <= 100 - total:
        total = one_more
    else:
        break

print(total)
