import sys
input = sys.stdin.readline

MAX_NUM = 8
MAX_ORD = 'H'

move = {
    "R": [1, 0],
    "L": [-1, 0],
    "B": [0, -1],
    "T": [0, 1],
    "RT": [1, 1],
    "LT": [-1, 1],
    "RB": [1, -1],
    "LB": [-1, -1]
}

def check_outside(x, y):
    if (x > MAX_ORD) or (x < 'A') or (int(y) > MAX_NUM) or (int(y) < 1):
        return True
    return False

def moving(input, x, y):
    dx, dy = move[input][0], move[input][1]
    nx, ny = chr(ord(x) + dx), str(int(y) + int(dy))
    return nx+ny

def move_king(input, king, stone):
    nk = moving(input, king[0], king[1])
    if check_outside(nk[0], nk[1]):
        return king, stone
    if (stone[0]==nk[0]) and (stone[1]==nk[1]):
        ns = moving(input, stone[0], stone[1])
        if check_outside(ns[0], ns[1]):
            return king, stone
        return nk, ns
    return nk, stone

king, stone, n = input().split()
for _ in range(int(n)):
    input_move = input().strip()
    king, stone = move_king(input_move, king, stone)

print(king)
print(stone)