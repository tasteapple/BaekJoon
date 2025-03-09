# 솔직히 어떻게 풀어야 할지 잘 모르겠다. 
# B배열을 재배열 하지 말라는 말이 정말 B를 재배열 하지 말라는건지 아니면 B를 건드리지 말라는 건지 모르겠다.
# B를 단지 재배열 하지 말라는거면 그냥 새로운 리스트를 만들어서 그거 쓰면 되는데 근데 그렇게 해도 돼? 라는 의문이 생긴다.

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum = 0

A.sort()
B.sort(reverse=True)

for i in range(N):
    sum += A[i] * B[i]
print(sum)
