"""
n = int(input())
meeting = [[0] * 3 for _ in range(n+1)] 
for i in range(n):
    meeting[i][0], meeting[i][1] = map(int, input().split())
    gap = meeting[i][1] - meeting[i][0]
    meeting[i][2] = gap
meeting.sort(key = lambda x:x[1])
sorted_meeting = meeting.copy()
maximum = sorted_meeting[n][1]
meeting.sort(key=lambda x:x[0])


dp = [1] * (maximum+1)
#dp를 마지막부터 시작해서 만들어 보자
for i in range(1, n+1):  # i가 0에서 시작하면 안 됨
    for j in range(i):  
        if meeting[j][1] <= meeting[i][0]:  # 인덱스 수정
            dp[meeting[i][1]] = max(dp[meeting[i][1]], dp[meeting[j][1]]+1)  # 인덱스 수정
print(max(dp)) """
import sys
n = int(sys.stdin.readline())
meeting = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    gap = end - start
    meeting.append((start, end, gap))

meeting.sort(key=lambda x: (x[1], x[0]))

dp = [0] * (n+1)
dp[1] = 1  # 첫 번째 회의는 항상 포함

for i in range(2, n+1):
    max_dp = 0
    for j in range(1, i):
        if meeting[j-1][1] <= meeting[i-1][0]:
            max_dp = max(max_dp, dp[j])
    dp[i] = max_dp + 1

print(max(dp))
