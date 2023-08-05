change_num = int(input())
cup_pos = 1
for _ in range(change_num):
    pos1, pos2 = map(int, input().split())
    if pos1 == cup_pos:
        cup_pos = pos2
        continue
    if pos2 == cup_pos:
        cup_pos = pos1

print(cup_pos)
