# 5525: IOIOI

# 첫 번째 I가 나오기 전까지의 O는 모두 제거
# I가 나오면 start, start 인덱스 기억해두기
# I가 나오면 IO 패턴이 반복될 때까지 슬라이싱
# IO 패턴이 끊기면 그 안에 O가 몇 개 있는지 판단
# if O가 M개면, M-N+1개가 답

import sys
sys.stdin = open('5525_input.txt')

N = int(input())
M = int(input())
s = input()

s.lstrip('O')
result = 0

base = 0

while True:
    base = s.find('I')
    if base == -1:
        break
    s = s[base:]

    start = 0
    end = 1
    is_end = False
    while s[start:end+1] == 'IO':
        if end == len(s):
            is_end = True
            break
        start += 2
        end += 2
    if is_end:
        # count_O = s[:end+1].count('O')
        count_I = (end+1) // 2
        if s[start] == 'I':
            count_I += 1
    else:
        # count_I = s[:start].count('O')
        count_I = start // 2
        if count_I and s[start - 1] == 'I':
            count_I += 1

    if count_I >= N:
        result += count_I - N
    print(s, count_I, start, end, result)

    if end >= len(s):
        break
    if not start:
        start += 1
    s = s[start:]
    # print(result, s)
print(result)