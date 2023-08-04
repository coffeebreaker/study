#### checking을 리스트로 만들어 줘서 순서가 오름차순으로 바뀐다

check = [False] * 101
value = [0] * 101
checking = []
limit = int(input())
recommend = int(input())
student = list(map(int, input().split()))
def remove_duplicates_keep_first(lst):
    unique_lst = []
    seen_elements = set()

    for ele in lst:
        if ele not in seen_elements:
            seen_elements.add(ele)
            unique_lst.append(ele)

    return unique_lst



def how_many(checking, value):
    if not checking:
        return None

    min_value = min(value)
    min_index = None

    for idx in checking:
        if min_index is None or value[idx] < value[min_index]:
            min_index = idx
    return min_index




def cal(checking):
    
    a = 0
    b = limit-1

    while b < recommend-1:
        b += 1
        if check[student[b]] == True:
            value[student[b]] += 1
        else:
            # 만약에 사용을 안한거라면
            remove_duplicates_keep_first(checking)
            # 근데 아직 좀 비어있는 상태면 그냥 추가한다
            if len(checking) >= limit:
                least_popular_index = how_many(checking, value)
                if least_popular_index is not None:
                    check[least_popular_index] = False
                    value[least_popular_index] = 0
                    checking.remove(least_popular_index)
                    value[student[b]] += 1
                    check[student[b]] = True
                    checking.append(student[b])
                    a += 1
            else:
                value[student[b]] += 1
                check[student[b]] = True
                checking.append(student[b])
                a += 1

    # 출력부분
    for i in range(1, 101):
        if check[i] == True:
            print(i, end=' ')
# 그대로
if limit > recommend:
    student = (list(set(student)))
    for i in student:
        print(i, end=' ')
else:
    for i in range(limit):
        check[student[i]] = True
        value[student[i]] += 1
        checking.append(student[i])
        checking = remove_duplicates_keep_first(checking)
    cal(checking)