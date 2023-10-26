import sys
sys.setrecursionlimit(10000000)
sys.stdin = open('9466_input.txt')
input = sys.stdin.readline

def dfs(student, num_member, turn):
    # result 초기화
    result = -1

    # 싸이클인 경우
    if selected[student][0] == 1 and selected[student][1] == turn:
        # 자기 자신을 선택한 경우
        if choices[student] == student:
            return 1
        return num_member - selected[student][2]
    
    # 방문 표시
    selected[student][0] = 1
    selected[student][1] = turn
    selected[student][2] = num_member
    
    # 아직 처리되지 않았거나, 같은 turn에서 처리된 친구일 경우
    if selected[choices[student]][0] == 0 or selected[choices[student]][1] == turn:
        result = dfs(choices[student], num_member+1, turn)
    
    return result

if __name__ == '__main__':
    T = int(input().rstrip())

    for _ in range(T):
        n = int(input().rstrip())
        choices = [0] + list(map(int, input().split()))
        
        # 모든 학생이 팀을 이루지 못했다고 가정하고,
        # 팀을 이룰 때마다 팀원 수만큼 answer에서 차감
        answer = n

        # 처리된 학생 표시
        selected = [[0, 0, 0] for _ in range(n + 1)]
        for student in range(1, n + 1):
            # 이미 처리된 학생인 경우 continue
            if selected[student][0] == 1:
                continue

            result = dfs(student, 1, student)

            # 팀이 이루어진 경우
            if result != -1:
                answer -= result
        
        print(answer)