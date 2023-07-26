# 문제 골5 얘는 돌아는 가는데 뇌절왔어
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

# 출력
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

    # A C A Y  K P
    # 1 0 1 -1 5 2
    # 4 3 4
    # C A P C A K
    #double_list = [[1,4],[0,3],[1,4],[-1],[5],[2]]
    #dp = [[[1],[1]],[[1],[2]],[[2],[3]],[[1]],[[4]],[[3]]]

import copy
A_list = input()
A = [char for char in A_list]
B_list = input()
B = [char for char in B_list]
# A = ['A', 'C', 'A', 'Y', 'K', 'P']
# B = ['C', 'A', 'P', 'C', 'A', 'K']
# A = ['A', 'B', 'C', 'D', 'E', 'F']
# B = ['G', 'H', 'I', 'J', 'K', 'L']
if len(B)>=len(A):
    Short = A
    Long = B
else:
    Short = B
    Long = A

double_list = []

for i in range(len(Short)):
    same_list = []
    for j in range(len(Long)):
        if(Short[i]==Long[j]):
            same_list.append(j)
    if not same_list:
        double_list.append([-1])
    else:
        double_list.append(same_list)

minus_one = True
for element in double_list:
    if element != -1:
        minus_one = False
        break

if minus_one:
    print(0)
    exit()

dp = copy.deepcopy(double_list)
for inner_list in dp:
    for i in range(len(inner_list)):
        inner_list[i] = [1]

for i in range(1,len(double_list)):
    if double_list[i][0]==-1:
        pass
    else:
        for j in range(len(double_list[i])):
            minus = 1
            while(double_list[i-minus][0]==-1):
                minus += 1
            for k in range(len(double_list[i-minus])):
                if(double_list[i-minus][k]<double_list[i][j]):
                    dp[i][j][0] = max(dp[i][j][0],dp[i-minus][k][0]+1)

max_element = max(dp, key=lambda x: x[0])
print(max_element[0][0])
