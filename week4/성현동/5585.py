remain = 1000 - int(input())

change = [500, 100, 50, 10, 5, 1]
idx = 0  # 10162랑 비슷. 현재 뺄 값의 인덱스, cnt 증가에 활용
cnt = 0

while remain > 0:
    if remain < change[idx]:  # 현재 뺄 값보다 잔돈이 작으면 인덱스 증가(뺼값 감소시킴)
        while remain < change[idx]:
            idx += 1

    remain -= change[idx]
    cnt += 1

print(cnt)
