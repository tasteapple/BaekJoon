N = int(input())
last_card = [str(i) for i in range(1, N + 1)]
pop_card = []

while len(last_card) != 1:
    pop_card.append(last_card.pop(0))
    last_card.append(last_card.pop(0))

print(' '.join(pop_card + last_card))
