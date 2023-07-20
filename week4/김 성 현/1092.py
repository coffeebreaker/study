import sys
import copy
c = int(sys.stdin.readline())
if c<=0 or c>50:
    print(-1)
    sys.exit()
    
crain = list(map(int, sys.stdin.readline().split())) 
crain.sort(reverse=True)  

b = int(sys.stdin.readline())
if b<=0 or b>1000000:
    print(-1)
    sys.exit()
boxes = list(map(int, sys.stdin.readline().split()))

boxes.sort(reverse=True)  

boxes_min = min(boxes)
crain_copy = copy.deepcopy(crain) 

for i in crain_copy:
    if i < boxes_min:
        crain.remove(i)


if boxes[0] > crain[0]:
    print(-1)
    sys.exit()
else:
    time =0

    while boxes:
        if not boxes:
            break
        for a in crain:
            if not boxes:
                break
            for b in boxes:
                if a >= b:
                    boxes.remove(b)
                    if not boxes:
                        break
                    break
        time+=1

    print(time)
# 93퍼에서 indexerror가 뜬다 -> why? 같이 고민해보자 ㅎㅎ
