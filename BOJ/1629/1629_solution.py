import sys
sys.stdin = open('1629_input.txt')

# 모듈러 연산의 곱의 성질을 이용하여 c로 나눈 나머지를 return
def div_con(a, n, c):
    if n == 1:
        return a % c
    else:
        if n % 2 == 0:
            num = div_con(a, n//2, c)
            num = num ** 2 % c
        else:
            num = div_con(a, (n-1)//2, c)
            num = num ** 2 * a % c
    return num

A, B, C = map(int, sys.stdin.readline().split())
print(div_con(A, B, C))