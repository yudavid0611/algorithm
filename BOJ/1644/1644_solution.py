import sys
from collections import deque
sys.stdin = open('1644_input.txt')

# 에라토스테네스의 체로 2부터 num까지의 모든 소수 구하기
def get_prime_numbers(num):
    prime_numbers = deque()
    nums = [0] * 2 + [1] * (num - 1)

    for i in range(2, N + 1):
        if nums[i]:
            prime_numbers.append(i)

            for j in range(i * 2, N + 1, i):
                nums[j] = 0
    return prime_numbers
    
N = int(input())
if N == 1:
    print(0)
else:
    # N까지의 소수 구하기
    prime_nums = get_prime_numbers(N)
    # 두 개의 포인터 초기화
    left = right = 0
    # left와 right 사이 값의 합을 저장할 변수
    sum_value = prime_nums[0]
    answer = 0

    while right < len(prime_nums):
        # 합이 N보다 작을 경우 left 이동
        if sum_value > N:
            sum_value -= prime_nums[left]
            left += 1
            continue
        
        # 합이 N과 같을 경우 answer + 1
        if sum_value == N:
            answer += 1

        # right를 옮기고 합에 prime_nums[right] 값 더해주기
        right += 1
        if right == len(prime_nums):
            break
        sum_value += prime_nums[right]
        
    print(answer)