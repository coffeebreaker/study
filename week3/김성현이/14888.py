MAX = 1000000000 + 1

N = int(input())
number = list(map(int, input().split()))
Operator = list(map(int, input().split()))

maxResult = -MAX
minResult = MAX


def DFS(plus, minus, multiply, divide, cnt, sum):
    global maxResult, minResult
    
    if cnt == N:
        maxResult = max(maxResult, sum)
        minResult = min(minResult, sum)
        return
    
    if plus > 0:
        DFS(plus - 1, minus, multiply, divide, cnt + 1, sum + number[cnt])
    if minus > 0:
        DFS(plus, minus - 1, multiply, divide, cnt + 1, sum - number[cnt])
    if multiply > 0:
        DFS(plus, minus, multiply - 1, divide, cnt + 1, sum * number[cnt])
    if divide > 0:
        DFS(plus, minus, multiply, divide - 1, cnt + 1, int(sum / number[cnt]))


DFS(Operator[0], Operator[1], Operator[2], Operator[3], 1, number[0])

print(maxResult)
print(minResult)

# 각각의 개수가 0이 될때까지 해준다 why ? 연산자 우선순위가 없기 때문이다
# 각각을 무작위로 넣어야 한다 어떻게 할까? -> 재귀 함수처럼? 해서 리스트에 넣어주기

#이거 왜 시발 안됨?
candidate = []
n = int(input())
values = (map(int, input().split()))
values = list(values)
calculate = (map(int, input().split()))
calculate = list(calculate)

def sunghyun(value2, index):
    if index == len(values):
        candidate.append(value2)
        return
    for i in range(4):
        if(calculate[i] > 0):
            calculate[i]-=1
            if(i==0):
                sunghyun(int(value2+values[index]), index+1)
            elif(i==1):
                sunghyun(int(value2-values[index]), index+1)
            elif(i==2):
                sunghyun(int(value2*values[index]), index+1)
            elif(i==3):
                sunghyun(int(value2//values[index]), index+1)
            calculate[i]+=1
    return
    
sunghyun(values[0], 1)

print(max(candidate))
print(min(candidate))