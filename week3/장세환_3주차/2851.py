ans = 0
total = 0
for i in range(10):
    total += int(input())
    if 100 - ans >= abs(100 - total) :
        ans = total
print(ans)