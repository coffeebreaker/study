import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
r,c,d = map(int, input().split())
arr =[]
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
# d= 0 북 1 동 2 남 3 서
check = [[True] * (m+1) for j in range(n+1)]
check[r][c] =False
sum=1

# 계속 반복 해서 실행한다
while 1:
        temp=0
        # 반시계 방향이면 0 3 2 1방향으로 맞춰준다
        for i in range(4):
            nx = r + dx[(d+3)%4]
            ny = c + dy[(d+3)%4]
            d = (d+3)%4
            # 범위 안넘고 만약에 벽이 아니라면
            if 0<=ny <m and 0<=nx <n and arr[nx][ny]==0:
                if check[nx][ny] == True:
                    check[nx][ny]=False
                    # 청소구역 +1 해주고
                    # 지금 위치 업데이트 해주기
                    sum +=1
                    c = ny
                    r = nx
                    temp =1
                    # 다시 다른 방향으로 돌아야하기 때문에 전환을 위해서 break
                    break
        # 4방향중 한방향이라도 청소를 했는데 이제 할 곳이 없다면? 다시 돌아갈 곳이 만약에 벽이라면?
        if temp ==0 and  arr[r-dx[d]][c-dy[d]] ==1:
                print(sum)
                break
        # 4방향 다돌고 이제 청소를 다시 할 곳이 생겼다면? 
        if temp ==0 and arr[r-dx[d]][c-dy[d]] ==0:
                r = r -dx[d]
                c = c-dy[d]
