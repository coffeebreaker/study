#부분합이 최대한 100에 가깝도록 만드는 것
#만약에 어떤 부분합이 다음에 오는 것을 포함하고 그 전것을 뛰어넘으면 빼줌. 그이후는 생각안해줘도 됨
values = []
for _ in range(10):
    values.append(input())
total = 0
for i in values:
    total +=i
    if total >=100:
        if total - 100 > 100 - (total -i):
            total -=i
        break
print(total)


