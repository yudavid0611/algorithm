import sys
from collections import deque
sys.stdin = open('2812_input.txt')

N, k = map(int, input().split())
num = input()
stack = deque()

stack.append(num[0])
num_idx = 1

while k and num_idx < N:
    now_num = num[num_idx]

    # 현재 숫자보다 작은 숫자 모두 stack에서 제거
    while stack and k and now_num > stack[-1]:
        stack.pop()
        k -= 1
    
    # 현재 숫자 스택에 넣기
    stack.append(now_num)
    num_idx += 1

# 제거된 숫자가 적을 경우
if k:
    stack = list(stack)
    print(''.join(stack[: len(stack) - k]))
else:
    print(''.join(stack) + num[num_idx: ])