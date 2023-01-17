# 6064: 카잉 달력

import sys
sys.stdin = open('6064_input.txt')
from collections import defaultdict

T = int(input())

for _ in range(T):
    year2_visited = defaultdict(int)
    M, N, X, Y = list(map(int, input().split()))
    success = False
    idx = X - 1
    year2 = 1 + idx
    if year2 > N:
        year2 = year2 % N
        if not year2:
                year2 = N
    cycle = 0
    while True:
        if year2 == 0:
            break
        if year2_visited.get(year2):
            cycle += 1
            if cycle == len(year2_visited):
                break
        else:
            cycle = 0
            year2_visited[year2] = 1
        
        if year2 == Y:
            success = True
            break
        
        idx += M
        year2 += M
        if year2 > N:
            year2 = year2 % N
            if not year2:
                year2 = N

    if success:
        print(idx + 1)
    else:
        print(-1)