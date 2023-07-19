import sys
sys.setrecursionlimit(100000)

n = int(input())
m = 0
arr = []
for i in range(0, n) :
    temp_list = list(map(int, input().split()))
    arr.append(temp_list)
    temp_m = max(temp_list)
    m = max(temp_m, m)
# sink : True (잠겼다) 
#  : True (방문했다)
# check : True (갈 수 있다)
def north_check(sink, i, j) :
    if i == 0 :
        return False
    elif sink[i - 1][j] == True :
        return False
    return True

def east_check(sink, i, j) :
    if j == n - 1 :
        return False
    elif sink[i][j + 1] == True :
        return False
    return True
    

def west_check(sink, i, j) :
    if j == 0:
        return False
    elif sink[i][j - 1] == True :
        return False
    return True

def south_check(sink, i, j) :
    if i == n - 1 :
        return False
    elif sink[i + 1][j] == True :
        return False
    return True

def find(sink, i, j) :
    sink[i][j] = True
    #사방면이 막혔을 경우
    if not north_check(sink, i, j) and not west_check(sink, i, j) and not east_check(sink, i, j) and not south_check(sink, i, j) :
        return
    if north_check(sink, i, j):
        find(sink, i - 1, j)
    if east_check(sink, i, j):
        find(sink, i, j + 1)
    if west_check(sink, i, j):
        find(sink, i, j - 1)
    if south_check(sink, i, j):
        find(sink, i + 1, j)

def sink_check(flags, height) :
    for i in range(0, n) :
        for j in range(0, n) :
            if arr[i][j] <= height :
                flags[i][j] = True

def safety_zone(height) :
    sink = []
    #초기화
    for i in range(n) : 
        temp = [False] * (n)
        sink.append(temp)
    #물잠기는 곳 확인
    sink_check(sink, height)
    ans = 0
    for i in range(0, n) :
        for j in range(0, n) :
            if sink[i][j] == False:
                # print("searching")
                find(sink, i, j)
                ans += 1
    return ans
ans = 0
for i in range(0, m + 1) :
    ans = max(safety_zone(i), ans)
print(ans)