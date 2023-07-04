#1110
init = int(input())
result = init
cnt = 0

while True:
    tens = result // 10
    ones = result % 10
    new_digit = (tens + ones) % 10
    result = ones * 10 + new_digit
    cnt += 1
    if result == init:
        break

print(cnt)
