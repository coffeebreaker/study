import sys
input = sys.stdin.readline
test_n = int(input())
count_list = []
for _ in range(0, test_n) :
    n = int(input())
    applicants = []
    for i in range(0, n) :
        a, b = map(int, input().split())
        applicants.append((a, b))
    applicants.sort()
    m = 1000001
    count = 0
    for i in applicants :
        if i[1] < m :
            m = i[1]
            count += 1
    count_list.append(count)
for i in count_list :
    print(i)