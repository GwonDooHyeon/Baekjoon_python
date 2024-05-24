# https://www.acmicpc.net/problem/1193
n = int(input())

count = 0
prevSum = 0

while n > prevSum:
    count = count + 1
    prevSum += count

# 끝의 라인에서 n까지의 거리
offset = prevSum - n

bunza = 0
bunmo = 0

if count % 2 == 0:
    bunza = count - offset
    bunmo = 1 + offset
else:
    bunza = 1 + offset
    bunmo = count - offset

print(f'{bunza}/{bunmo}')


