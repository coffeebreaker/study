import heapq

N = int(input())
cards = [int(input()) for _ in range(N)]

# 우선순위 큐로 변환
heapq.heapify(cards)

result = 0

while len(cards) > 1: # 카드 묶음이 하나 이상 남았을 때
    # 가장 작은 두 묶음 꺼내기
    sum_value = heapq.heappop(cards) + heapq.heappop(cards)
    result += sum_value
    heapq.heappush(cards, sum_value)

print(result)
