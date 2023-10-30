import sys
sys.stdin = open('7570_input.txt')
input = sys.stdin.readline

N = int(input().rstrip())
children = list(map(int, input().split()))

# children의 각 인덱스별 최대 시퀀스 저장
dp1 = [0] * (N + 1)

# 각 번호별 최대 시퀀스 저장
dp2 = [0] * (N + 1)

for idx, num in enumerate(children, 1):
    dp1[idx] = max(dp1[idx - 1], dp2[num - 1] + 1)
    dp2[num] = dp2[num - 1] + 1

print(N - dp1[-1])