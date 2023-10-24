import sys
sys.setrecursionlimit(10000000)
sys.stdin = open('1937_input.txt')
input = sys.stdin.readline


def dfs(row, col):
    global answer
    
    # 이미 방문한 칸
    if visited[row][col] == 1:
        return
    
    # 아직 방문하지 않은 칸
    else:
        visited[row][col] = 1
        max_num = 0
        
        for d in delta:
            new_row = row + d[0]
            new_col = col + d[1]

            # 유효한 칸이고, 대나무가 더 많을 경우
            if 0 <= new_row < N and 0 <= new_col < N and forest[new_row][new_col] > forest[row][col]:
                dfs(new_row, new_col)

                # max_num 업데이트
                if dp[new_row][new_col] > max_num:
                    max_num = dp[new_row][new_col]

        # 현재 칸의 dp값 업데이트
        dp[row][col] = max_num + 1

        # answer 업데이트
        if dp[row][col] > answer:
            answer = dp[row][col]

if __name__ == '__main__':
    N = int(input().rstrip())

    forest = [list(map(int, input().split())) for _ in range(N)]

    # dp: 각 칸으로부터 이동할 수 있는 최대 경로 수
    dp = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    answer = 0

    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for i in range(N):
        for j in range(N):
            dfs(i, j)
    
    print(answer)