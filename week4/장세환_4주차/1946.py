import sys
input = sys.stdin.readline
t = int(input())
for i in range (t) :
    n = int(input())
    cnt = 1
    score = []
    for i in range(n) :
        doc, inter = map(int,input().split())
        score.append((doc,inter))
    score.sort(key=lambda x : x[0])
    max_score = score[0][1]
    for i in range(1, n) :
        if score[i][1] < max_score :
            max_score = score[i][1]
            cnt += 1
    print(cnt)
