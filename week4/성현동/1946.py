import sys

input = sys.stdin.readline

for _ in range(int(input())):
    applicant_num = int(input())
    applicant_list = []
    for __ in range(applicant_num):
        doc, interview = map(int, input().split())
        applicant_list.append([doc, interview])

    applicant_list.sort()

    max_interview = applicant_list[0][1]
    accepted = 1

    for _, interview in applicant_list[1:]:
        if interview < max_interview:
            max_interview = interview
            accepted += 1

    print(accepted)
