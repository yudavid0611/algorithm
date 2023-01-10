# 16953: A -> B

import sys
sys.stdin = open('16953_input.txt')

A, B = map(int, input().split())
min_calculation = B // A + 1

def find_min_calculation(v, now_calculation):
    global min_calculation
    if v == B:
        if now_calculation < min_calculation:
            min_calculation = now_calculation
    elif v < B:
        find_min_calculation(v * 2, now_calculation + 1)
        find_min_calculation(v * 10 + 1, now_calculation + 1)

find_min_calculation(A, 0)

if min_calculation == B // A + 1:
    print(-1)
else:
    print(min_calculation + 1)