price = int(input())
change = 1000 - price
count = 0
while True :
    if change >= 500 :
        count += 1
        change -= 500
    elif change >= 100 :
        count += 1
        change -= 100
    elif change >= 50 :
        count += 1
        change -= 50
    elif change >= 10 :
        count += 1
        change -= 10
    elif change >= 5 :
        count += 1
        change -= 5
    elif change >= 1 :
        count += 1
        change -= 1
    else :
        break
print(count)