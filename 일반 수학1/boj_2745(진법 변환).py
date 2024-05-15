# 진법 변환
# https://www.acmicpc.net/problem/2745

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()
answer = 0

for i, num in enumerate(n[::-1]):
    answer += num_list.index(num) * int(b) ** i

print(answer)


