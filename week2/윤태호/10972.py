# 문제
# 1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오.

# 사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

# N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.

# 1, 2, 3
# 1, 3, 2
# 2, 1, 3
# 2, 3, 1
# 3, 1, 2
# 3, 2, 1
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.

# 출력
# 첫째 줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력한다. 만약, 사전순으로 마지막에 오는 순열인 경우에는 -1을 출력한다.

N = int(input())
num_list = list(map(int, input().split()))


def next(num_list):
    if num_list == sorted(num_list, reverse=True):
        return -1

    for i in range(-1, -N-1, -1):

        if num_list[i:] == sorted(num_list[i:], reverse=True):
            continue

        else:
            new_list = [_ for _ in num_list[i+1:] if _ > num_list[i]]

            # new_list의 최솟값과 num_list[i]를 교환
            temp = num_list[num_list.index(min(new_list))]
            num_list[num_list.index(min(new_list))] = num_list[i]
            num_list[i] = temp
            # num_list[i+1:] 오름차순 정렬 후 합침
            first_half = num_list[:i+1]
            second_half = sorted(num_list[i+1:])
            return first_half + second_half


next_list = next(num_list)
if type(next_list) == list:
    for num in next_list:
        print(num, end=" ")
    print()
else:
    print(next_list)
