room_number = input()
number_count = [0] * 9 # 0 ~ 8 6이랑 9는 뒤집어서 같은 걸로 사용 가능능

for number in room_number:
    if number == '9':
        number_count[6] += 1
    else:
        number_count[int(number)] += 1
number_count[6] = (number_count[6] + 1) // 2

print(max(number_count))
