test_case = int(input())
for i in range(test_case):
    N,M = map(int,input().split())
    list_n = list(map(int,input().split()))
    where_m = M
    count = 0
    while True:
        if list_n[0] == max(list_n):
            count += 1
            if where_m == 0:
                print(count)
                break
            list_n[0] = 0
            list_n.append(list_n.pop(0))
            if where_m == 0:
                where_m = len(list_n)-1
            else:
                where_m -= 1
        else:
            list_n.append(list_n.pop(0))
            if where_m == 0:
                where_m = len(list_n)-1
            else:
                where_m -= 1
