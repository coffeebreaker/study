N,K = map(int, input("N과 K를 입력해주세요: ").split())

res = 0
count = 0

arr = list(range(2,N+1))

while(True):
    i = 0
    while(True):        #P를 정하는 반복문
        if(arr[i]==0):
            i += 1
        else:
            break
    P = arr[i]          #P는 소수
    count += 1          #P 지우고 count 증가
    if(count==K):
        res = P
        break
    arr[i] = 0             
    while(i<len(arr)):     #P의 배수 지우는 반복문
        if(arr[i]==0):
            i += 1
            continue
        elif(arr[i]%P==0):  #P의 배수이면
            count += 1  #count 증가 
            if (count==K):  #K번째 지운수이니 반복 종료
                res = arr[i]
                break
            arr[i] = 0
            i += 1
        else:               #P의 배수가 아닐때는 그냥 넘어가
            i += 1
            continue
    if (count==K or count==(len(arr))):  #모든 수를 지웠거나 K번째 지웠다면 반복 종료
        break

print(res)