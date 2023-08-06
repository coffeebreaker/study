n = int(input())
switch = list(map(int, input().split()))
student_number = int(input())

def changing(sex,number, switch ):
    number = number-1
    if sex == 1:
        number = number+1
        k = n // number
        for i in range(1,k+1):
            switch[number*i-1] = 1-switch[number*i-1]
    else:
        switch[number] = 1- switch[number]
        a,b =number-1,number+1
        while a >= 0  and b < n:
            if switch[a] == switch[b]:
                switch[a] = 1 -switch[a]
                switch[b] = 1 -switch[b]
            a-=1
            b+=1
                


for i in range(student_number):
    sex, number = map(int, input().split())
    changing(sex, number, switch)
for i in range(0, (len(switch) + 19) // 20):
    for j in range(20):
        index = 20 * i + j
        if index < len(switch):
            print(switch[index], end=' ')
    print()  

# 이거 왜 4퍼에서 틀리는 거임?


