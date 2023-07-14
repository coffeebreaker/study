import sys
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

end_time = meetings[0][1]
count = 1

for meeting in meetings[1:]:
    if meeting[0] < end_time:
        continue

    else:
        end_time = meeting[1]
        count += 1

print(count)
