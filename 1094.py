X = int(input()) # 원하는 막대 길이

stick_list = [64]


while sum(stick_list) > X:
    tmp = stick_list[-1] // 2
    stick_list[-1] //= 2
    if sum(stick_list) < X:
        stick_list.append(tmp)
    
    
print(len(stick_list))