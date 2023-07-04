import sys
from math import sqrt
from collections import deque

sys.stdin = open('2981_input.txt')

# 유클리드 호제법을 통한 최대공약수 구하기
# n1 >= n2
def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)

# 약수 구하기
def cds(n):
    cds = deque()
    sqrt_value = sqrt(n)
    for i in range(2, int(sqrt_value) + 1):
        if n % i == 0:
            cds.append(i)
    
    
    start = len(cds) - 1
    
    # 제곱근이 약수일 경우 제곱근이 한 번 더 추가되지 않도록 인덱스 이동
    if sqrt_value in cds:
        start -= 1
    
    # 쌍을 이루는 약수 추가
    for j in range(start, -1, -1):
        cds.append(n // cds[j])
    
    # n 추가
    cds.append(n)
    return cds

N = int(sys.stdin.readline())

nums = deque()
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
nums = sorted(nums)

# 두 숫자의 차이를 저장할 deque
diff = deque()
for i in range(1, N):
    diff.append(nums[i] - nums[i - 1])

# 차이들의 최대공약수 구하기
now_gcd = 0
for i in range(N - 1):
    if now_gcd >= diff[i]:
        now_gcd = gcd(now_gcd, diff[i])
    else:
        now_gcd = gcd(diff[i], now_gcd)

# 약수 구하기
cds = cds(now_gcd)
cds = list(map(str, cds))
cds = ' '.join(cds)
print(cds)