import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


dx = [0, 0, -1, 1]  #�� �� �� �� ����
dy = [1 , -1 , 0 ,0]

max_num = 0 #�ִ� ����
result = 0 #�ִ� ���������� �� 


n = int(input())
graph = []
for i in range(n) :
    row = list(map(int,input().split()))
    graph.append(row)
    max_num = max(max_num, max(row))



def dfs(x,y, num):
    for i in range(4) : #�� �� �� �� ������ Ž�� = 4��
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 :
            if graph[nx][ny] > num : 
                visited[nx][ny] = 1
                dfs(nx, ny, num)
 
for rain in range(max_num) : #�� ������ ���� ����
    visited =[[0] * n for i in range(n)]
    safe_zone = 0 #���������� �� 

    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain and visited[i][j] == 0:
                dfs(i,j,rain) #�湮���� ���� �������� dfs ����
                safe_zone +=1
    result = max(result, safe_zone)
print(result)
