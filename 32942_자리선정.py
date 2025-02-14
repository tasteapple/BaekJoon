X, C, K = map(int, input().split()) # X: 학생 수, C: 좌석 개수 K: 로그 갯수

student_list = [0] * X # 몇번 선택 했는지지
student_list2 = [0] * X # 실제 앉은 좌석석
sit_list = [0] * C # 선택 되었는지지

result = [tuple(map(int, input().split())) for _ in range(K)] # 순서, 자리, 학생 

result.sort()
# print(result)

for i in result:
    if sit_list[i[1] - 1] == 0:
        sit_list[i[1] - 1] = 1
        student_list[i[2] - 1] += 1
        if student_list[i[2] - 1] > 1:
            sit_list[student_list2[i[2] - 1] - 1] = 0
            student_list[i[2] - 1] -= 1
        student_list2[i[2] - 1] = i[1] 


print(sit_list)
print(student_list)
print(student_list2)

for i in range(X):
    if student_list2[i] != 0:
        print(i+1, student_list2[i])
