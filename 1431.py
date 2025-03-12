N = int(input())
guitar_serial_list = [input() for _ in range(N)]
guitar_serial_list.sort(key=lambda x: (len(x), sum([int(i) for i in x if i.isdigit()]), x)) # 람다를 사용하여 3가지를 조건으로 전달

for guitar_serial in guitar_serial_list:
    print(guitar_serial)
