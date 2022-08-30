import copy
import sys
sys.stdin = open('BOJ/14888/14888_input.txt', 'r')



def divide(n1, n2):
    if n1 < 0:
        n1 = n1 * (-1)
        return n1 // n2 * (-1)
    else:
        return n1 // n2


n = int(input())
nums = list(map(int, input().split()))
oper_nums = list(map(int, input().split()))
calculation = [[0] * 4 for _ in range(n-1)]
oper_nums_temp = copy.deepcopy(oper_nums)



max_value = -1
min_value = 100**11

breaking = False
while not breaking:
    result = nums[0]
    for idx, c in enumerate(calculation, 1):                # 연산 순회
        for idx2, op in enumerate(oper_nums_temp):          # 연산자 순회
            if op == 0 or c[idx2] == 1:                     # 연산자가 없거나, 이미 연산에서 사용한 연산인 경우,
                continue
            else:                                           # 연산자가 있고, 연산에서 사용하지 않은 연산인 경우,
                if idx2 == 0:
                    result = result + nums[idx]
                    oper_nums_temp[idx2] -= 1
                    c[idx2] = 1
                elif idx2 == 1:
                    result = result - nums[idx]
                    oper_nums_temp[idx2] -= 1
                    c[idx2] = 1
                elif idx2 == 2:
                    result = result * nums[idx]
                    oper_nums_temp[idx2] -= 1
                    c[idx2] = 1
                else:
                    result = divide(result, nums[idx])
                    oper_nums_temp[idx2] -= 1
                    c[idx2] = 1
                break
        else:
            if oper_nums_temp.count(0) != len(oper_nums_temp):
                breaking = True
                break
    else:
        if result < min_value:
            min_value = result
        if result > max_value:
            max_value = result
        
        oper_nums_temp = copy.deepcopy(oper_nums)

print(max_value)
print(min_value)

