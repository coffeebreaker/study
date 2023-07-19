# 각 케이스를 받고 그 다음 케이스가 숫자가 하나라도 적으면 바로 패스하고
# 가장 낮은것을 저장해 놓다가 만약에 그 숫자가 둘다 많으면 그 친구는 탈락
# check하는 것이 필요

# 다음것이 지금보다 다 작다면 초기화 해줘야 함
# 근데 그 전것들도 확인을 해줘야한다.
# 이러면 for문을 존나 돌려야함
#### 다시 생각
# 처음부터 기준으로 만들어주고 정렬해주고
# 다른 기준으로 하면 중복이 안됨 왜냐면 중복되는 숫자가 없으니까
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    k = int(sys.stdin.readline())
    candidate = []
    for _ in range(k):
        score1 , score2 = map(int, sys.stdin.readline().split())
        candidate.append((score1, score2))
    sorted_candidate = sorted(candidate, key=lambda x:x[0])

    sum = 1
    minimum = sorted_candidate[0][1]

    for i in range(1,k):
        if sorted_candidate[i][1] < minimum:
            sum+=1
            minimum = sorted_candidate[i][1]
        else:
            pass
    print(sum)

