# https://www.acmicpc.net/problem/2720

# 테스트 케이스 개수
t = int(input())

# 예제 입력
for _ in range(t):
    c = int(input())
    for num in [25, 10, 5, 1]:
        print(c // num, end=' ')
        c = c % num