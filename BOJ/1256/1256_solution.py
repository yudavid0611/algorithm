import sys
from math import factorial
sys.stdin = open('1256_input.txt')
input = sys.stdin.readline

# 경우의 수 개수 구하기
def get_cases_of_position(n_a, n_z):
    numerator = factorial(n_a + n_z)
    denominator = factorial(n_a) * factorial(n_z)
    return int(numerator / denominator)

n, m, k = map(int, input().split())

# 사전에 등록될 단어 수보다 k가 클 경우 -1 return
n_cases_total = get_cases_of_position(n, m)
if k > n_cases_total:
    print(-1)

else:
    word = []

    word.append('a')
    n -= 1

    while True:
        # 현재 상태에서 가능한 경우의 수 개수 구하기
        n_cases = get_cases_of_position(n, m)

        # k가 여전히 더 크면 a를 z로 바꿔주기
        if k > n_cases:
            word.pop()
            n += 1
            word.append('z')
            m -= 1

            # a였을 때 가능한 경우의 수 빼주기
            k -= n_cases

        # k번째 단어가 현재 상태에서 도출되는 경우의 수 중 하나일 경우
        elif k < n_cases:
            word.append('a')
            n -= 1
        
        # k==n_cases일 경우 정답 찾기
        else:
            temp = 'a' * n + 'z' * m
            temp = sorted(temp, reverse=True)
            word.extend(temp)
            break

    print(''.join(word))