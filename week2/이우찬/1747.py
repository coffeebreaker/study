N = int(input())

cnt = 0   #소수 확인용
ans = 0   #답

while(ans==0):
    num_str = str(N)  # 정수를 문자열로 변환
    num_arr = []
    num_rev = []
    for digit in num_str:
        num_arr.append(int(digit))
        num_rev.append(int(digit))
    num_rev.reverse()
    if(num_arr==num_rev):#역순과 동일하노?
        if(N==1):
            pass
        elif(N==2):
            ans = 2
        else:
            for j in range(2, N): #소수 확인시작
                if(N%j != 0):
                    cnt += 1
                    if(cnt==(N-2)):
                        ans = N
                        break
                else:
                    break         #소수 아님
    num_arr.clear()
    num_rev.clear()
    N += 1
print(ans)