# 9251: LCS


import sys
sys.stdin = open('9251_input.txt')

# 고정
s1 = input()
# 순회
s2 = input()

dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]

for i in range(1, len(s2)+1):
    s2_idx = i-1
    for j in range(1, len(s1)+1):
        s1_idx = j-1
        # 같으면 +1
        if s2[s2_idx] == s1[s1_idx]:
            dp[i][j] += dp[i-1][j-1] + 1
        # 다르면 왼쪽 값과 이전 행의 현재 열의 값 중 큰 값
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])