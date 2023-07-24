# 문제
# 지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 모든 화물은 박스에 안에 넣어져 있다. 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다.

# 각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 각 크레인의 무게 제한이 주어진다. 이 값은 1,000,000보다 작거나 같다. 셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다. 넷째 줄에는 각 박스의 무게가 주어진다. 이 값도 1,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다. 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.

#틀렸대

#input
N = int(input())
crane = []
input_str = input()
elements = input_str.split()
num = [int(element) for element in elements]
crane.extend(num)
crane.sort(reverse=True)

M = int(input())
box = []
input_str = input()
elements = input_str.split()
num = [int(element) for element in elements]
box.extend(num)
box.sort(reverse=True)

crane_limit = [M-1]*N
checkbox = [True]*M

count = 0

if(max(crane)<max(box)):
    print(-1)
else:
    #자기가 할 수 있는 부분을 찾아야지
    for i in range(N):
        for j in range(M):
            if crane[i]>=box[j]:
                crane_limit[i]=j
                break
    #진행시켜야지
    while(True):
        for i in range(N):
            while(checkbox[crane_limit[i]]==False):    #이미 그 박스를 치웠으면 다음 칸으로
                if crane_limit[i]<M-1:                 #마지막 인덱스가 아닐때 다음으로 이동
                    crane_limit[i] += 1
                else:
                    break
            if crane_limit[i]<M:
                checkbox[crane_limit[i]] = False           #True면 치우고 False
        count += 1
        if all(element == 0 for element in checkbox):
            break
    print(count)