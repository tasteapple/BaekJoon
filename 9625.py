list1 = [[0,0] for _ in range(46)]
list1[0] = [1, 0]
list1[1] = [0, 1]

for i in range(2, 46):
    list1[i][0] = list1[i-1][1]
    list1[i][1] = list1[i-1][1] + list1[i-1][0]

K = int(input())
print(list1[K][0], list1[K][1])
