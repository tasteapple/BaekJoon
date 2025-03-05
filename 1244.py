switch_count = int(input())
switch_state = list(map(int, input().split()))
student_count = int(input())

for _ in range(student_count):
    student_sex, number = map(int, input().split())
    if student_sex == 1: # male
        for i in range(number - 1, switch_count, number):
            switch_state[i] = switch_state[i] ^ 1
    elif student_sex == 2: # female
        left = number - 1
        right = switch_count - number
        min_number = min(left, right)
        switch_state[number - 1] = switch_state[number - 1] ^ 1 
        if min_number == 0:
            continue
        for i in range(1, min_number + 1):
            if switch_state[(number - 1) - i] == switch_state[(number - 1) + i]:
                switch_state[(number - 1) - i] = switch_state[(number - 1) + i] = switch_state[(number - 1) - i] ^ 1
            else:
                break

for i in range(0, switch_count, 20):
    print(' '.join(map(str, switch_state[i:i+20])))
