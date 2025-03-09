R, C = map(int, input().split())

while True:
    list1 = [[0] * C for _ in range(R)]
    list2 = [list(input()) for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if list2[i][j] == '*':
                # 좌상
                if (i - 1 >= 0 and j - 1 >= 0) and (list2[i - 1][j - 1] != '*'):
                    list1[i - 1][j - 1] += 1
                # 상
                if i - 1 >= 0 and list2[i - 1][j] != '*':
                    list1[i - 1][j] += 1
                # 우상
                if (i - 1 >= 0 and j + 1 < C) and (list2[i - 1][j + 1] != '*'):
                    list1[i - 1][j + 1] += 1
                # 좌
                if j - 1 >= 0 and list2[i][j - 1] != '*':
                    list1[i][j - 1] += 1
                # 우
                if j + 1 < C and list2[i][j + 1] != '*':
                    list1[i][j + 1] += 1
                # 좌하
                if (i + 1 < R and j - 1 >= 0) and (list2[i + 1][j - 1] != '*'):
                    list1[i + 1][j - 1] += 1
                # 하
                if i + 1 < R and list2[i + 1][j] != '*':
                    list1[i + 1][j] += 1
                # 우하
                if (i + 1 < R and j + 1 < C) and (list2[i + 1][j + 1] != '*'):
                    list1[i + 1][j + 1] += 1
    
    for i in range(R):
        for j in range(C):
            if list1[i][j] == 0 and list2[i][j] == '*':
                print('*', end='')
            else:
                print(list1[i][j], end='')
        print()


    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break
