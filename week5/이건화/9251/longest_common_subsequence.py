a = input()
b = input()
# b가 긴 놈
if len(a) > len(b) :
    a, b = b, a

lcs = []
for _ in range(len(b) + 1) :
    temp = [0] * (len(a) + 1)
    lcs.append(temp)

# i는 b이자
for i in range(1, len(b) + 1) :
    # j는 a
    for j in range(1, len(a) + 1) :
        if b[i - 1] == a[j - 1] :
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else :
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
print(lcs[len(b)][len(a)])