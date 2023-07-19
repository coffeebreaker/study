remain = int(input())

div = [300, 60, 10]  # 현재 뺄 값
cnt = [0, 0, 0]
idx = 0  # 현재 뺄 값의 인덱스, cnt 증가에 활용

while remain > 0:
    if 0 < remain < div[2]: # 뺀 나머지가 10미만이면 무슨 수를 써도 가능조합 안나옴
        print(-1)
        exit(0)
    elif remain < div[1]: # 나머지가 10~60이면 10으로 뺌
        idx = 2
    elif remain < div[0]: # 나머지가 60~300이면 60으로 뺌
        idx = 1

    remain -= div[idx]
    cnt[idx] += 1

print(cnt[0], cnt[1], cnt[2])
