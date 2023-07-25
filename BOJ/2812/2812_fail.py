# 시간초과
# 슬라이싱으로 숫자를 복사하는 과정, max함수와 index 메서드 호출 빈도가 많아 시간 초과가 난 것으로 추정된다.

import sys
sys.stdin = open('2812_input.txt')

N, k = map(int, input().split())
num = input()

answer = ''
front = 0
while k and N > k:
    # 가장 큰 숫자 인덱스
    cand = num[front:front + k + 1]
    max_num = max(cand)
    max_idx = cand.index(max_num)

    answer += max_num
    front += (max_idx + 1)
    k -= max_idx

if front < N and N != k:
    print(answer + num[front:])
else:
    print(answer)