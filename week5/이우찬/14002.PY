# 문제 골4 얘도 되는데 틀렸대
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

#input
N = int(input())
string = input()
seq = list(map(int, string.split()))

#세보자
#   10 20 10 30 20 50
# 0  1  2  2  3  3  4
# 1        1  2  2  3
# 2              1  2

# num_list, count_list 두개 필요할듯.
#첫 인덱스부터 돌다가 작은수가 나오면 그때 1 append. for문으로 dp를 돌면서 그 수와 비교해서 그 수가 크면 count를 업시킴. 가장 작은수면 append. 
max_num = [[0]]
count_list = [0]

for i in range(len(seq)):
    #이번 숫자에 대해 list append 여부 결정
    min = 1001
    for k in range(len(max_num)):
        if(min>max_num[k][-1]):
            min = max_num[k][-1]
    if(min>seq[i]):         #max_num list의 수보다 작은 수가 나타났을때 새로운 수열 count 시작. append
        max_num.append([seq[i]])
        count_list.append(1)

    #max_num이랑 count 재설정
    for j in range(len(max_num)):
        if(seq[i]>max_num[j][-1]):  #숫자가 내 수열의 수보다 클때
            max_num[j].append(seq[i]) #max_num갈아치우고
            count_list[j] += 1  #count 올려주기
max_value = max(count_list)
max_index = count_list.index(max_value)

print(max_value)
for i in range(1, len(max_num[max_index])):
    if(i == len(max_num[max_index])):
        print(max_num[max_index][i])
    else:
        print(max_num[max_index][i], end=' ')
