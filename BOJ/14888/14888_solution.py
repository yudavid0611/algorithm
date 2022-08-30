import sys
sys.stdin = open('BOJ/14888/14888_input.txt', 'r')
import copy
from itertools import permutations
import math

operator_dict = {
    0: '+',
    1: '-',
    2: '*',
    3: '%'
}

def permutation(e, n, target):
    global op_idx
    if e == n:
        temp = copy.deepcopy(target)
        # if temp not in operator_p:
        #     operator_p.append(temp)
        operator_p[op_idx] = temp
        op_idx += 1
        
    else:
        for i in range(e, n):
            target[i], target[e] = target[e], target[i]
            permutation(e+1, n, target)
            target[i], target[e] = target[e], target[i]
    

def divide(n1, n2):
    if n1 < 0:
        n1 = n1 * (-1)
        return n1 // n2 * (-1)
    else:
        return n1 // n2


n = int(input())
nums = list(map(int, input().split()))
oper_nums = list(map(int, input().split()))

## 1. 연산자 순열 만들기 ##
operator = []
operator_p = [[0] * (n-1) for _ in range(math.factorial(n-1))]
for idx, op in enumerate(oper_nums):
    for i in range(op):
        operator.append(operator_dict[idx])

# for i in permutations(operator, n-1):
#     if i not in operator_p:
#         operator_p.append(i)

op_idx = 0
permutation(0, n-1, operator)

## 2. 연산 수행하기 ##
max_value = -1
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

