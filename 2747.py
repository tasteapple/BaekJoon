count = int(input())

pibo_list = [0] * 46
pibo_list[0] = 0
pibo_list[1] = 1

for i in range(2, 46):
    pibo_list[i] = pibo_list[i - 1] + pibo_list[i - 2]

print(pibo_list[count])
