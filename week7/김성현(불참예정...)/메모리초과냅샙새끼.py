n, c = map(int, input().split())
mulgun = list(map(int, input().split()))

from itertools import combinations
count =1
combinations_list = []  # Renamed 'combination' to 'combinations_list'
for i in range(1, n+1):
    combinations_list.append(list(combinations(mulgun, i)))  # Use 'combinations' function correctly
    for comb in combinations_list[i-1]:
        if sum(comb) <=c:
            count +=1
print(count)