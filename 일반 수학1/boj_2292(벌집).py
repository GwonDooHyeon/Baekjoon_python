# https://www.acmicpc.net/problem/2292

n = int(input())

count = 1
num = 2

if n == 1:
    print(1)
else:
    while num <= n:
        num = num + count * 6
        count += 1
    print(count)
