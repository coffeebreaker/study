frame_num = int(input())
rec_num = int(input())

frame_list = {}
on_frame = 0
order = 0
for n in [int(id) for id in input().split()]:
    if n in frame_list:
        frame_list[n][1] += 1
        continue
    elif on_frame >= frame_num:
        min_rec = min([value[1] for value in frame_list.values()])
        candidate = [(id, value[0]) for id, value in frame_list.items() if value[1] == min_rec]
        target = min(candidate, key=lambda x: x[1])
        del frame_list[target[0]]
        on_frame -= 1
    frame_list[n] = [order, 1]
    on_frame += 1
    order += 1

for id in sorted(frame_list.keys()):
    print(id, end=' ')