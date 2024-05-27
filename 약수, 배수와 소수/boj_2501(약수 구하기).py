# https://www.acmicpc.net/problem/2501

# 입력 받기
first, second = map(int, input().split())

# 약수를 저장할 리스트
list = []

# 1부터 n까지 돌며 약수를 찾음
for i in range(1, first + 1):
    if first % i == 0:
        list.append(i)

if len(list) < second:
    print(0)
else:
    print(list[second - 1])


