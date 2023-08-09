movements = {
    'R': [1, 0],
    'L': [-1, 0],
    'B': [0, -1],
    'T': [0, 1],
    'RT': [1, 1],
    'LT': [-1, 1],
    'RB': [1, -1],
    'LB': [-1, -1],
}


king_pos, stone_pos, move_num = input().split()
king_pos = [ord(king_pos[0]) - 64, int(king_pos[1])]
stone_pos = [ord(stone_pos[0]) - 64, int(stone_pos[1])]
for _ in range(int(move_num)):
    direction = input()
    new_king = [king_pos[i] + movements[direction][i] for i in range(2)]
    new_stone = stone_pos
    if not (1 <= new_king[0] <= 8 and 1 <= new_king[1] <= 8):
        continue
    if new_king == stone_pos:
        new_stone = [stone_pos[i] + movements[direction][i] for i in range(2)]
        if not (1 <= new_stone[0] <= 8 and 1 <= new_stone[1] <= 8):
            continue
    king_pos, stone_pos = new_king, new_stone

print(chr(king_pos[0] + 64) + str(king_pos[1]))
print(chr(stone_pos[0] + 64) + str(stone_pos[1]))
