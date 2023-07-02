# n개만큼을 가진 리스트를 만든다 -> 한개씩 정수형
# 소수를 찾는 것들을 만든다 -> 다른 배열 2차원?
# 2중 for문으로?
# cnt 로 번째를 찾아서 그걸 pop으로 빼온다
N = 1000
n, k = map(int, input().split())
checking = []
check = [False, False] + ([True] * (N-1))
double_check =  [False, False] + ([True] * (N-1))
#checking은 소수다.
#문제 -> 한번 넣어준것이 다시 그 배수가 적용이 된다. => double check가 필요
def sosu(n):
    for i in range(2, n+1):
        # 처음부터 할때 check가 True고 double check 도 True여야한다
        if check[i] == True and double_check[i]==True:
            checking.append(i)
            double_check[i] = False

            # 뭐 사실 tuple로 제거해줘도 될듯
            #소수의 배들을 제거하고 다시는 쓰이지 않도록 double check해준다
            for j in range(i*2, n+1, i):
                check[j] = False
                if double_check[j] == True:
                    checking.append(j)
                    double_check[j] = False
sosu(n)
print(checking[k-1])