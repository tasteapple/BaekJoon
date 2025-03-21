fibo_list = [0] * 491
fibo_list[0] = 0
fibo_list[1] = 1
for i in range(2, 491):
    fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]

while True:
    n = int(input())
    if n == -1:
        break
    print(f"Hour {n}: {fibo_list[n]} cow(s) affected")
