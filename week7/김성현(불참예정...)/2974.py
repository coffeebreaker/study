namu = list(map(int, input().split()))
answer = [1,2,3,4,5]
while True:
    for i in range(len(namu)-1):
        if namu[i] > namu[i+1]:
            namu[i],namu[i+1] = namu[i+1], namu[i]
            print(" ".join(map(str,namu)))
    if namu == answer:
        break