n = int(input())
total = int(input())
recommend = list(map(int, input().split()))
gallery = list()

def put_gallery(std_num, t):
    # 해당 학생이 갤러리에 있는 지 찾기
    for std in gallery:
        if std['std_num'] == std_num:
            std = std
            break
    else:
        std = None

    # 있으면 추천 수 증가, 없으면 뺄 거 빼고 새 액자 넣음
    if std:
        std['recommend'] += 1
    else:
        if len(gallery) == n:
            to_be_delete = gallery[0]
            for student in gallery[1:]:
                if student['recommend'] < to_be_delete['recommend']:
                    to_be_delete = student
                elif student['recommend'] == to_be_delete['recommend']:
                    if student['upload_at'] < to_be_delete['upload_at']:
                        to_be_delete = student
            id = gallery.index(to_be_delete)
            gallery[id] = {
                'std_num':std_num, 
                'recommend': 1, 
                'upload_at': t
            }
        else:
            gallery.append({
                'std_num':std_num, 
                'recommend': 1, 
                'upload_at': t
            })


for i in range(total):
    put_gallery(recommend[i], i)

num_list = sorted([std['std_num'] for std in gallery])
print(*num_list)