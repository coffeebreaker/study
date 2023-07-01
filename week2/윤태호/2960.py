# 문제
# 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.

# 이 알고리즘은 다음과 같다.

# 2부터 N까지 모든 정수를 적는다.
# 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
# N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N, max(1, K) < N ≤ 1000)

# 출력
# 첫째 줄에 K번째 지워진 수를 출력한다.

N, K = map(int, input().split())

num_list = [_ for _ in range(2, N+1)]

count = 0
while True:
    # 현재 리스트에서 가장 작은 값 P 탐색
    P = num_list.pop(0)

    # count 하나 늘리고 K와 같은 지 검사
    count += 1
    if count == K:
        print(P)
        break

    # P의 배수 삭제
    i = 2
    while P*i <= N:
        # P의 배수가 이미 삭제된 수라면 continue
        if P*i not in num_list:
            i += 1
            continue

        # P의 배수 삭제
        num_list.remove(P*i)

        # count 하나 늘리고 K와 같은 지 검사
        count += 1
        if count == K:
            print(P*i)
            break

        # while문 돌리기
        i += 1

    # 위에서 count == K 여서 종료된 경우 바깥 while문 종료
    if count == K:
        break

    # num_list가 빈 배열이라면 while문 종료
    if not num_list:
        break
