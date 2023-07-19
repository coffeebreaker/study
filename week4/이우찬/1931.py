# 문제
# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

# 입력
# 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.

import copy
#input
N = int(input())
use_list = []
for i in range(N):
    input_str = input()
    elements = input_str.split()
    use = [int(element) for element in elements]
    use_list.append(use)

# 일단 처음은 후자가 가장 작은걸로 스타트
# 두번째부터는 앞의 list의 후자보다 늦은 전자보유 list중에서 후자가 가장 작은것
# 연달아서 반복

# 후자 최저 찾기
min_latter = 2**31-1
the_one = []
for i in range(N):
    if(min_latter>use_list[i][1]):
        min_latter = use_list[i][1]
        the_one = copy.deepcopy(use_list[i])
# the_one이 선발주자
res = 1

min_latter = 2**31-1
i = 0
# the_one 뒤의 놈들 중 후자가 가장 작은 놈. 근데? the_one의 후자보다 전자가 작다? pop하자. 그리고 N -= 1
while(N>1):
    while(i<N):
        if(use_list[i][0]<the_one[1]):
            use_list.pop(i)
            N -= 1
        else:
            if(use_list[i][1]<min_latter):
                min_latter = use_list[i][1]
                the_one = copy.deepcopy(use_list[i])
        i += 1
    else:
        res += 1
    i = 0

print(res-1)