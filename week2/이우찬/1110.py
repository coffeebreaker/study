num = int(input("정수: "))

count = 0   #사이클 세주기
first = num
while(True):
    if(num<10): #만약 한자리수면 그냥 그대로임
        add = num
    else:   #아니면 각자리수 더해야지
        add = num//10 + num%10
    num = add%10 + num%10*10    #새로운 수 생성
    count += 1  #한사이클 적립
    if num == first:    #초기값과 같으면 끝
        break

print(count)