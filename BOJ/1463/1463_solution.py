# 1463: 1로 만들기

# DP bottom-up 풀이
# 재귀함수로 구현 시 recursion error 발생 -> for문으로 구현
# top-down 형식으로도 풀어보기


import sys
sys.stdin = open('1463_input.txt')

# def dp(i):
#     if i > N:
#         return
#     else:
#         if not i % 3:
#             min_count[i] = min(min_count[i//3], min_count[i-1]) + 1
#         if not i % 2:
#             if min_count[i]:
#                 if min_count[i] > min_count[i//2] + 1:
#                     min_count[i] = min_count[i//2] + 1
#             else:
#                 min_count[i] = min(min_count[i//2], min_count[i-1]) + 1
#         if not min_count[i]:
#             min_count[i] = min_count[i-1] + 1
#         dp(i+1)
    
N = int(input())
min_count = [0] * (N + 1)
for i in range(2, N+1):
    if not i % 3:
        min_count[i] = min(min_count[i//3], min_count[i-1]) + 1
    if not i % 2:
        # 3으로도 나누어 떨어지는 값일 경우
        if min_count[i]:
            if min_count[i] > min_count[i//2] + 1:
                min_count[i] = min_count[i//2] + 1
        # 3으로 나누어 떨어지는 값이 아닐 경우
        else:
            min_count[i] = min(min_count[i//2], min_count[i-1]) + 1
    # 3과 2 어느 것으로도 나누어 떨어지지 않는 경우
    if not min_count[i]:
        min_count[i] = min_count[i-1] + 1
print(min_count[N])

