import sys
from itertools import combinations
sys.stdin = open('15684_input.txt')
input = sys.stdin.readline


# 결과 확인
def check():
    for col in range(1, N + 1):
        start = [1, col]
        
        # 사다리 이동
        while start[0] < H + 1:
            # 왼쪽과 연결되는 가로선이 있을 경우
            if lines[start[0]][start[1] - 1] == 1:
                start[1] -= 1
            
            # 오른쪽과 연결되는 가로선이 있을 경우
            elif lines[start[0]][start[1]] == 1:
                start[1] += 1

            # 아래로 이동
            start[0] += 1

        # 시작 칼럼과 도착 칼럼이 다를 경우
        if start[1] != col:
            return False
    
    else:
        return True


if __name__ == '__main__':
    N, M, H = map(int, input().split())

    lines = [[0] * (N + 1) for _ in range(H + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        lines[a][b] = 1

    # 가로선을 추가로 놓을 수 있는 위치 구하기
    possible = [[i, j] for j in range(1, N) for i in range(1, H + 1)
                    if lines[i][j] == 0]
    
    # 가로선을 추가로 놓지 않았을 때 체크
    if check():
        print(0)
    
    else:
        # 정답을 구했을 시 for문 탈출을 위한 flag
        flag = False
        for i in range(1, 4):
            combination = list(combinations(possible, i))
            for c in combination:
                # 사다리 추가
                for j in range(i):
                    lines[c[j][0]][c[j][1]] = 1
                
                # 정답 여부 체크
                if check():
                    print(i)
                    flag = True
                    break
                
                # 사다리 원위치
                else:
                    for j in range(i):
                        lines[c[j][0]][c[j][1]] = 0
            if flag:
                break
        else:
            print(-1)