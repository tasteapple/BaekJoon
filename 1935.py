N = int(input())
list1 = list(input()) # 후위기수

alpa_dict = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'F' : 0, 'G' : 0, 'H' : 0, 'I' : 0, 'J' : 0, 'K' : 0, 'L' : 0, 'M' : 0, 'N' : 0, 'O' : 0, 'P' : 0, 'Q' : 0, 'R' : 0, 'S' : 0, 'T' : 0, 'U' : 0, 'V' : 0, 'W' : 0, 'X' : 0, 'Y' : 0, 'Z' : 0}

for i in range(N):
    alpa_dict[chr(ord('A') + i)] = int(input())

list2 = []
for i in list1:
    if i.isalpha():
        list2.append(alpa_dict[i])
    else:
        a = list2.pop()
        b = list2.pop()
        if i == '+':
            list2.append(b + a)
        elif i == '-':
            list2.append(b - a)
        elif i == '*':
            list2.append(b * a)
        elif i == '/':
            list2.append(b / a)

print('%.2f' % list2[0])
