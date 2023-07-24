meeting_num = int(input())
meeting_list = []

for _ in range(meeting_num):
    start, end = map(int, input().split())
    meeting_list.append([start, end]) # [시작,종료] 리스트를 원소로 갖는 회의 리스트 준비

meeting_list.sort(key=lambda x: (x[1], x[0]))
# 종료시간 기준 오름차순, 종료시간 동일시 시작시간 오람차순 정렬
# 최대한 일찍 종료될수록, 더 많은 회의가 뒤에 잡힐 수 있고,
# 종료시간이 같은 경우, 일찍 시작하는 것을 먼저 고르도록 해야 시작종료시간이 동일한 애들까지 포함해 계산할 수 있다
# ex) [2,3][3,3] 이 모두 회의에 들어가려면 시작시간이 오름차순 정렬되어야 한다

cnt = 1 # 정렬되었으므로 첫번째 회의는 무조건 포함
cur = 0 # 현재 회의 인덱스(다음 회의 인덱스 next와 비교 예정)
for next in range(cur + 1, meeting_num):
    if meeting_list[cur][1] <= meeting_list[next][0]: #다음회의가 현재회의와 시간이 겹치지 않는다면
        cur = next
        cnt += 1

print(cnt)
