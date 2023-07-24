target = int(input())
a = 300
b = 60
c = 10
a_count = 0
b_count = 0
c_count = 0
while True:
    if target >= 300 :
        target -= a
        a_count += 1
    elif target >= 60 :
        target -= b
        b_count += 1
    elif target >= 10 :
        target -= c
        c_count += 1
    elif target == 0 :
        break
    else :
        print(-1)
        exit()
print(a_count, b_count, c_count)