direction = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}

row, col = map(int, input().split())
cur_robot = [int(n) for n in input().split()]
state = [[0] * col for _ in range(row)]
for i in range(row):
    state[i] = [int(n) for n in input().split()]

cleaned_room = 0
while True:
    y, x, dir = cur_robot[0], cur_robot[1], cur_robot[2]
    if state[y][x] == 0:
        state[y][x] = 2
        cleaned_room += 1

    found = False
    for dy, dx in direction.values():
        if state[y + dy][x + dx] == 0:
            found = True
            break

    if not found:
        new_y, new_x = y - direction[dir][0], x - direction[dir][1]
        if state[new_y][new_x] == 1:
            print(cleaned_room)
            exit()
        cur_robot[:2] = [new_y, new_x]
        continue
    else:
        dir = (dir - 1) % 4
        new_y, new_x = y + direction[dir][0], x + direction[dir][1]
        if state[new_y][new_x] == 0:
            cur_robot[:2] = [new_y, new_x]
        cur_robot[2] = dir
