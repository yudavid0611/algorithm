# 1946: 신입 사원

import sys
sys.stdin = open('1946_input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    people = [list(map(int, input().split())) for _ in range(N)]
    people.sort()
    min_value = N

    count = 0
    for i in range(N):
        now = people.pop(0)
        if now[1] < min_value:
            count += 1
        if now[1] < min_value:
             min_value = now[1]

    print(count)