human = int(input())

check_enter = {}
enter_human = []

for _ in range(human):
    name, enter = input().split()
    check_enter[name] = enter

for name, enter in check_enter.items():
    if enter == 'enter':
        enter_human.append(name)

enter_human.sort(reverse=True)
for name in enter_human:
    print(name)
