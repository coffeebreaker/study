for _ in range(int(input())):
    floor = int(input())
    room = int(input())

    apt = [[1] * room for _ in range(floor + 1)]
    apt[0] = [i for i in range(1, room + 1)]

    for row in range(1, floor + 1):
        for col in range(1, room):
            if col == 1:
                apt[row][col] = apt[row - 1][col] + 1
            else:
                apt[row][col] = apt[row - 1][col] + apt[row][col - 1]

    print(apt[floor][room-1])
