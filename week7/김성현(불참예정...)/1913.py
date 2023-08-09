import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
snail = [[0]* n for _ in range(n)]

x = (n-1)//2
y = (n-1)//2
snail[y][x]=1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
i=2
pivot =3
while x != 0 or y!=0:
    while i<= pivot * pivot:
        if x==y==(n-1)//2:
            up,down,left,right=pivot,pivot-1,pivot-1,pivot-2
            x+=dx[0]
            y+-dy[0]
            up -=1
        elif right >0:
            x +=dx[3]
            y+=dy[3]
            right -=1
        elif down >0:
            x+=dx[1]
            y+=dy[1]
            down -=1
        elif left >0:
            x+=dx[2]
            y+=dy[2]
            left-=1
        elif up >0:
            x+=dx[0]
            y+=dy[0]
            up-=1
        snail[x][y]=i
        i+=1
    n-=2
    pivot +=2
for j in range(len(snail)):
    print(*snail[j])
    if m in snail[j]:
        mx = j+1
        my = snail[j].index(m) +1
print(mx,my)