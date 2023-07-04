inputs_line = input()
inputs = inputs_line.split()
n = int(inputs[0])
k = int(inputs[1])
#0, 1 : 소수 2 ~ n - 110은 소수 X(초기화)
a = [False, False] + [True] * (n-1)
#첫번째 True만 살린다.
count = 0
for i in range (2, n+1) :
    #첫번째만 살린다.
    if a[i] == True :
        for j in range(i, n+1, i) :
            if(a[j] == True) :
                a[j] = False
                count += 1
                if(count == k) :
                    print(j)
                    exit()
