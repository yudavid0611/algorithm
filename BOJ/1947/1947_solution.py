# 완전순열 문제
import sys
sys.stdin = open('1947_input.txt')
input = sys.stdin.readline

N = int(input().rstrip())

if N == 1:
    print(0)

else:
    dp = [0] * (N + 1)
    dp[2] = 1

    for i in range(3, N + 1):
        dp[i] = (i - 1) * (dp[i-2] + dp[i-1])  % 1000000000

    print(dp[N])