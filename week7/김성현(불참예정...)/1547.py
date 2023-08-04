
cup = [False, True, False, False]

M = int(input())
for i in range(M):
    first, second = map(int, input().split())
    if cup[first] == True:
        cup[first]=False
        cup[second] = True
    elif cup[second] == True:
        cup[first] = True
        cup[second] = False
for i in range(4):
    if cup[i]==True:
        print(i)