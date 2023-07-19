from queue import PriorityQueue
n = int(input())
meeting = PriorityQueue()
for _ in range(0, n) :
    a, b = map(int, input().split())
    meeting.put((b,a))
end = 0
count = 0
for _ in range(0, n) :
    b, a = meeting.get()
    if a >= end :
        end = b
        count += 1
print(count)