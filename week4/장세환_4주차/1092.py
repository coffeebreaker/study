import sys
input = sys.stdin.readline
n = int(input())
crane = list(map(int,input().split()))
m = int(input())
weight = list(map(int,input().split()))

crane.sort(reverse=True)
weight.sort(reverse=True)
cnt = 0
if crane[0] < weight[0] :
    print(-1)
else :
    while weight :
        for i in crane :
            if  weight and i < weight[-1] :
                continue
            for j in weight :
                if i > j :
                    weight.remove(j)
                    break
        cnt +=1
    print((cnt))