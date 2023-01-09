# 1541: 잃어버린 괄호

import sys
from functools import reduce
sys.stdin = open('1541_input.txt')


s = input()
expression = s.split('-')
for i in range(len(expression)):
    now_exp = expression[i]
    now_exp_splited = now_exp.split('+')
    # 왼쪽에 붙은 0 제거
    now_exp_splited = list(map(lambda x: x.lstrip('0'), now_exp_splited))
    # 합 구하기
    now_new = reduce(lambda acc, cur: 
    acc + int(cur) if cur else acc, now_exp_splited, 0)

    if not i:
        result = now_new
    else:
        result -= now_new
    
print(result)