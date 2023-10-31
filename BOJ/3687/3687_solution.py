import sys
sys.stdin = open('3687_input.txt')
input = sys.stdin.readline

# 숫자를 표현하기 위한 성냥 개수
num_to_match = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

# 각 성냥 개수로 만들 수 있는 가장 작은 수
match_to_num = {
    2: '1',
    3: '7',
    4: '4',
    5: '2',
    6: '0',
    7: '8'
}

# 가장 큰 수 찾기
def find_max_num(n):
    answer = ''
    q, r = divmod(n, 2)
    
    # 짝수일 경우 몫만큼 1로 채움
    if r == 0:
        answer += '1' * q
    
    # 홀수일 경우 몫 - 1만큼 1로 채우고 앞에 7을 추가
    else:
        answer += '7' + '1' * (q - 1)
    
    return answer

# 가장 작은 수 찾기
def find_min_num(n):
    answer = ''
    
    # 최소 자리수 찾기
    q, r = divmod(n, 7)
    # 7의 배수이면 8을 채워서 return
    if r == 0:
        answer += match_to_num[7] * q
        return answer
    
    # 7의 배수가 아닐 경우 몫의 +1만큼이 최소 자리수
    else:
        len_min = q + 1

    for i in range(len_min - 1, -1, -1):
        # 앞으로 사용할 수 있는 성냥의 최대 개수
        max_matches = 7 * i

        for j in num_to_match.keys():
            # 첫 번째 자리에는 0이 오지 못함
            if j == '0' and i == len_min - 1:
                continue

            # 앞으로 사용할 수 있는 최대 개수 이하로 성냥을 사용할 수 있는 경우
            if 0 <= n - num_to_match[j] <= max_matches:
                answer += j
                n -= num_to_match[j]
                break
    
    # 남은 자리를 모두 8로 채움
    answer += '8' * i

    return answer

if __name__ == '__main__':
    T = int(input().rstrip())
    for _ in range(T):
        n = int(input().rstrip())
        print(find_min_num(n), find_max_num(n))