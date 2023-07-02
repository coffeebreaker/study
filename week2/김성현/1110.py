n = int(input())
cnt =0
k = n
while True:
    a = n // 10
    b = n % 10
    c = a + b
    n = 10 * b + c % 10
    cnt +=1
    if(n == k):
        break
print(cnt)