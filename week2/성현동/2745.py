num, base = input().split()
base = int(base)

total = 0
for cnt, s in enumerate(num[::-1]):
    if s.isdigit():
        value = int(s)
    else:
        value = (ord(s) - ord('A') + 10)
    total += value * (base ** cnt)

print(total)
