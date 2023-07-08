height = []
for i in range(9) :
    i = int(input())
    height.append(i)
fake = sum(height) - 100
for i in range (9) :
    for j in range(i + 1 , 9) :
        if height[i] + height[j] == fake :
            dwarf = [height[i],height[j]]
for i in dwarf :
    height.remove(i)
height.sort()
for i in height :
    print(i)