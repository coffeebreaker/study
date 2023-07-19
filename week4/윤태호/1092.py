# 문제
# 지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 모든 화물은 박스에 안에 넣어져 있다.

# 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다.

# 각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다.

# 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 각 크레인의 무게 제한이 주어진다.

# 이 값은 1,000,000보다 작거나 같다. 셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다.

# 넷째 줄에는 각 박스의 무게가 주어진다. 이 값도 1,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다. 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.
import sys

N = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))

# 모든 박스를 옮길 수 없는 경우
if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

# 각 크레인이 현재 옮겨야 하는 박스의 번호 (0부터 시작)
positions = [0] * N
checked = [False] * M

# 크레인과 박스를 내림차순 정렬
cranes.sort(reverse=True)
boxes.sort(reverse=True)

result = 0
count = 0

while True:
    if count == len(boxes):  # 박스를 다 옮겼다면 종료
        break
    for i in range(N):  # 모든 크레인에 대하여 각각 처리
        while positions[i] < len(boxes):
            # 아직 안 옮긴 박스 중에서, 옮길 수 있는 박스를 만날 때까지 반복
            if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1

print(result)
