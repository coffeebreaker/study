import sys
input = sys.stdin.readline

f = int(input())
n = int(input())
vote = list(map(int, input().split()))

frame = []
vote_count = []

for i in range(n) :
    if vote[i] in frame :
        vote_count[frame.index(vote[i])] += 1
    else :
        if len(frame) == f :
            target = vote_count.index(min(vote_count))
            del frame[target]
            del vote_count[target]
        frame.append(vote[i])
        vote_count.append(1)

frame.sort()
print(*frame)