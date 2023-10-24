import sys
sys.stdin = open('11049_input.txt')
input = sys.stdin.readline


N = int(input().rstrip())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for interval in range(1, N):
    for start in range(0, N - interval):
        dp[start][start + interval] = 2 ** 31
        for pointer in range(start, start + interval):
            dp[start][start + interval] = min(dp[start][start + interval], dp[start][pointer] + dp[pointer + 1][start + interval] + matrix[start][0] * matrix[pointer][1] * matrix[start + interval][1])

print(dp[0][-1])