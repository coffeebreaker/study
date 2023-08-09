# 문제 실3
# 8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다. 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.

# 킹은 다음과 같이 움직일 수 있다.

# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로
# 체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.



# 입력으로 킹이 어떻게 움직여야 하는지 주어진다. 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.

# 킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 킹의 위치, 돌의 위치, 움직이는 횟수 N이 주어진다. 둘째 줄부터 N개의 줄에는 킹이 어떻게 움직여야 하는지 주어진다. N은 50보다 작거나 같은 자연수이고, 움직이는 정보는 위에 쓰여 있는 8가지 중 하나이다.

# 출력
# 첫째 줄에 킹의 마지막 위치, 둘째 줄에 돌의 마지막 위치를 출력한다.

#     a b c d e f g h
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# R : 한 칸 오른쪽으로 : [][+1]
# L : 한 칸 왼쪽으로 : [][-1]
# B : 한 칸 위로 : [-1][]
# T : 한 칸 아래로 : [+1][]
# RT : 오른쪽 아래 대각선으로 : [+1][+1]
# LT : 왼쪽 아래 대각선으로 : [+1][-1]
# RB : 오른쪽 위 대각선으로 : [-1][+1]
# LB : 왼쪽 위 대각선으로 : [-1][-1]

move = {
    "R": [1,0],
    "L": [-1,0],
    "B": [0,-1],
    "T": [0,1],
    "RT": [1,1],
    "LT": [-1,1],
    "RB": [1,-1],
    "LB": [-1,-1],
}
#input
kinga, stonea, n = input().split()
n = int(n)
king = list(map(int, [ord(kinga[0]) - 64, kinga[1]]))
stone = list(map(int, [ord(stonea[0]) - 64, stonea[1]]))

dest = [0,0]
s_dest = [0,0]

for i in range(n):
    to_where = input()
    dest[0] = king[0] + move[to_where][0]
    dest[1] = king[1] + move[to_where][1]
    s_dest[0] = stone[0] + move[to_where][0]
    s_dest[1] = stone[1] + move[to_where][1]
    
    #king이 stone으로 갈때
    if dest == stone:
        # stone이 가려는 곳이 체스판 안일때
        if s_dest[0]>0 and s_dest[0]<=8 and s_dest[1]>0 and s_dest[1]<=8:
            king[0] = stone[0]
            king[1] = stone[1]
            stone[0] = stone[0] + move[to_where][0]
            stone[1] = stone[1] + move[to_where][1]
        # stone이 가려는 곳이 체스판 밖일때
        else:
            pass
    # king이 가려는 곳이 체스판 안일때
    elif dest[0]>0 and dest[0]<=8 and dest[1]>0 and dest[1]<=8:
        king[0] = dest[0]
        king[1] = dest[1]
    # king이 가려는 곳이 체스판 밖일때
    else:
        pass

king[0] = chr(king[0]+64)
stone[0] = chr(stone[0]+64)
com_king = str(king[0]) + str(king[1])
com_stone = str(stone[0]) + str(stone[1])

print(com_king)
print(com_stone)