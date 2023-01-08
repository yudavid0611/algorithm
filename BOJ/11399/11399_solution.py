# 11399: ATM
# 가장 작은 숫자는 N번, 그다음 작은 숫자는 N-1번... 가장 큰 숫자는 1번 더해진다.


import sys
sys.stdin = open('11399_input.txt')

N = int(input())

times = list(map(int, input().split()))

times.sort()

result = 0

for i in range(N, 0, -1):
    result += i * times[N - i]

print(result)