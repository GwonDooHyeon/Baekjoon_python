# https://www.acmicpc.net/problem/2869

up, down, height = map(int, input().split())

day = (height - down) // (up - down)

if (height - down) % (up - down) != 0:
    day = day + 1

print(day)

