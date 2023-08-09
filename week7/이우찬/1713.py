# 문제 실1 마자따!
# 월드초등학교 학생회장 후보는 일정 기간 동안 전체 학생의 추천에 의하여 정해진 수만큼 선정된다. 그래서 학교 홈페이지에 추천받은 학생의 사진을 게시할 수 있는 사진틀을 후보의 수만큼 만들었다. 추천받은 학생의 사진을 사진틀에 게시하고 추천받은 횟수를 표시하는 규칙은 다음과 같다.

# 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
# 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
# 비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 그 자리에 새롭게 추천받은 학생의 사진을 게시한다. 이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.
# 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
# 사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.
# 후보의 수 즉, 사진틀의 개수와 전체 학생의 추천 결과가 추천받은 순서대로 주어졌을 때, 최종 후보가 누구인지 결정하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 사진틀의 개수 N이 주어진다. (1 ≤ N ≤ 20) 둘째 줄에는 전체 학생의 총 추천 횟수가 주어지고, 셋째 줄에는 추천받은 학생을 나타내는 번호가 빈 칸을 사이에 두고 추천받은 순서대로 주어진다. 총 추천 횟수는 1,000번 이하이며 학생을 나타내는 번호는 1부터 100까지의 자연수이다.

# 출력
# 사진틀에 사진이 게재된 최종 후보의 학생 번호를 증가하는 순서대로 출력한다.

# frame이 다찼는가 == 0이 하나라도 있는가
def zero(frame):
    for j in frame:
        if j[0] == 0:
            return True
    return False

def exist(frame, finder):
    for j in frame:
        if j[0] == finder:
            j[1] += 1
            # j[2] = sequence
            return True
    return False

#input
N = int(input())
frame = [[0 for _ in range(3)] for _ in range(N)] #frame[0]==액자가 채워졌는가, frame[1]==추천수
M = int(input())
str = input()
ddabong = list(map(int, str.split()))
# 있던 놈들에 한해서만 sequence 적용. 있던 놈들은 sequence를 안올려야된다는 뜻.
sequence = 0
# 이후 sequence로 sort하면 됨

#돌리자
for i in range(M):
    #여기에 얘가 있는지가 우선. 있다면 추천수(frame[][1])를 1 올려야됨
    if exist(frame,ddabong[i]) == True:
        # frame = sorted(frame, key=lambda x: x[2])
        frame = sorted(frame, key=lambda x: x[2])
        frame = sorted(frame, key=lambda x: x[1])

    #여기서부턴 새로운 후보임
    #안에가 다 차있는지 확인
    else:
        sequence += 1
        frame.pop(0)
        frame.append([ddabong[i],1,sequence])
        frame = sorted(frame, key=lambda x: x[2])
        frame = sorted(frame, key=lambda x: x[1])

frame.sort()
res = []
for i in range(N):
    if frame[i][0]==0:
        pass
    else:
        res.append(frame[i][0])

print(*res)

# 5 7 1
# 1 1 3
# 2 3 1

# 7 5 1
# 1 2 3
# 3 2 1

# 9 5 1
# 1 2 3
# 4 2 1

# 5 1 9
# 2 3 3
# 2 1 4

# 1 5 9
# 3 3 3
# 1 2 4

# 4 5 9
# 1 3 3
# 5 2 4

# 6 5 9
# 1 3 3
# 6 2 4