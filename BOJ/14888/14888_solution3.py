import sys
sys.stdin = open('BOJ/14888/14888_input.txt', 'r')

# 함수 출처: http://daplus.net/python-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EC%A3%BC%EC%96%B4%EC%A7%84-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%98-%EA%B0%80%EB%8A%A5%ED%95%9C-%EB%AA%A8%EB%93%A0-%EC%88%9C%EC%97%B4-%EC%B0%BE/
def lexico_permute_string(s):
    a = sorted(s)
    n = len(a) - 1
    while True:
        yield ''.join(a)

        #1. Find the largest index j such that a[j] < a[j + 1]
        for j in range(n-1, -1, -1):
            if a[j] < a[j + 1]:
                break
        else:
            return

        #2. Find the largest index k greater than j such that a[j] < a[k]
        v = a[j]
        for k in range(n, j, -1):
            if v < a[k]:
                break

        #3. Swap the value of a[j] with that of a[k].
        a[j], a[k] = a[k], a[j]

        #4. Reverse the tail of the sequence
        a[j+1:] = a[j+1:][::-1]

operator_dict = {
    0: '+',
    1: '-',
    2: '*',
    3: '%'
}


def divide(n1, n2):
    if n1 < 0:
        n1 = n1 * (-1)
        return n1 // n2 * (-1)
    else:
        return n1 // n2


n = int(input())
nums = list(map(int, input().split()))
oper_nums = list(map(int, input().split()))

## 1. 연산자 순열 만들기(중복 제거) ##
operator = []
for idx, op in enumerate(oper_nums):
    for i in range(op):
        operator.append(operator_dict[idx])

operator_p = []
for i in lexico_permute_string(operator):
    operator_p.append(i)


## 2. 연산 수행하기 ##
max_value = 100**11 * (-1)
min_value = 100**11

for ops in operator_p:
    result = nums[0]

    for idx, op in enumerate(ops, 1):
        if op == '+':
            result = result + nums[idx]
        elif op == '-':
            result = result - nums[idx]
        elif op == '*':
            result = result * nums[idx]
        else:
            result = divide(result, nums[idx])

    if result < min_value:
        min_value = result
    if result > max_value:
        max_value = result

print(max_value)
print(min_value)